"""Записує mp3 для кожної фрази з data-say / data-answer на сторінках блогу.

    python3 -m venv /tmp/tts && /tmp/tts/bin/pip install edge-tts
    /tmp/tts/bin/python tools/voice.py

Голос — en-GB-LibbyNeural. Наявні файли не перезаписуються.
"""
import asyncio
import glob
import html
import os
import re

import edge_tts

ROOT = os.path.join(os.path.dirname(__file__), '..')
OUT = os.path.join(ROOT, 'audio')
VOICE = 'en-GB-LibbyNeural'


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def phrases():
    found = set()
    for page in glob.glob(os.path.join(ROOT, '*', 'index.html')):
        for m in re.finditer(r'data-(?:say|answer)="([^"]+)"', open(page, encoding='utf-8').read()):
            found.add(html.unescape(m.group(1)))
    return sorted(found)


async def main():
    os.makedirs(OUT, exist_ok=True)
    for text in phrases():
        path = os.path.join(OUT, slug(text) + '.mp3')
        if os.path.exists(path):
            continue
        await edge_tts.Communicate(text, VOICE).save(path)
        print(slug(text))


asyncio.run(main())
