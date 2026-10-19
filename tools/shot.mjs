import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';

const [url, out, mode = 'mobile', script = ''] = process.argv.slice(2);
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const port = 9300 + Math.floor(Math.random() * 500);
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', `--remote-debugging-port=${port}`,
  `--user-data-dir=/tmp/blog-shot-${port}`, 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));

let target;
for (let i = 0; i < 50 && !target; i++) {
  try { target = (await (await fetch(`http://127.0.0.1:${port}/json`)).json()).find(t => t.type === 'page'); }
  catch { await sleep(200); }
}
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise(r => ws.addEventListener('open', r));
let id = 0; const pending = new Map();
ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (pending.has(m.id)) { pending.get(m.id)(m.result); pending.delete(m.id); } });
const send = (method, params = {}) => new Promise(r => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });

const mobile = mode === 'mobile';
const W = mobile ? 390 : 1280, H = mobile ? 844 : 800;
await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: mobile ? 2 : 1, mobile });
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: process.env.SCHEME || 'light' }] });
await send('Page.enable');
await send('Page.navigate', { url });
await sleep(1500);
if (script) { await send('Runtime.evaluate', { expression: script }); await sleep(400); }
const over = await send('Runtime.evaluate', { expression: 'document.documentElement.scrollWidth + "/" + innerWidth', returnByValue: true });
const m = await send('Page.getLayoutMetrics');
const h = Math.ceil(m.cssContentSize.height);
await send('Emulation.setDeviceMetricsOverride', { width: W, height: h, deviceScaleFactor: mobile ? 2 : 1, mobile });
await sleep(300);
const shot = await send('Page.captureScreenshot', { format: 'png' });
writeFileSync(out, Buffer.from(shot.data, 'base64'));
console.log(out, 'scrollWidth/innerWidth=' + over.result.value, 'height=' + h);
ws.close(); chrome.kill();
process.exit(0);
