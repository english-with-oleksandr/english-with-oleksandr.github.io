import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'img')
INK = '#2b2b33'
SKIN = '#f6c9a0'
HAIR = '#8b5a2b'
SHIRT = '#4a90e2'
PANTS = '#34495e'


def svg(name, w, h, body):
    s = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
         'stroke="%s" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
         % (w, h, INK, body))
    with open(os.path.join(OUT, name + '.svg'), 'w') as f:
        f.write(s)


def head(cx=60, cy=38):
    return (
        f'<circle cx="{cx}" cy="{cy}" r="24" fill="{SKIN}"/>'
        f'<path d="M{cx-25} {cy-2} Q{cx-24} {cy-30} {cx} {cy-27} Q{cx+24} {cy-30} {cx+25} {cy-2} '
        f'Q{cx+14} {cy-14} {cx} {cy-16} Q{cx-14} {cy-14} {cx-25} {cy-2}Z" fill="{HAIR}"/>'
        f'<circle cx="{cx-8}" cy="{cy+2}" r="2.5" fill="{INK}" stroke="none"/>'
        f'<circle cx="{cx+8}" cy="{cy+2}" r="2.5" fill="{INK}" stroke="none"/>'
        f'<path d="M{cx-8} {cy+11} Q{cx} {cy+18} {cx+8} {cy+11}" fill="none"/>'
        f'<circle cx="{cx-15}" cy="{cy+9}" r="3.5" fill="#f19a8a" stroke="none" opacity=".7"/>'
        f'<circle cx="{cx+15}" cy="{cy+9}" r="3.5" fill="#f19a8a" stroke="none" opacity=".7"/>'
    )


def legs(cx=60, top=114):
    return (
        f'<rect x="{cx-18}" y="{top}" width="14" height="34" rx="4" fill="{PANTS}"/>'
        f'<rect x="{cx+4}" y="{top}" width="14" height="34" rx="4" fill="{PANTS}"/>'
        f'<path d="M{cx-21} {top+34} h18 v6 h-20 Z" fill="{INK}"/>'
        f'<path d="M{cx+3} {top+34} h18 v6 h-18 Z" fill="{INK}"/>'
    )


def shirt(cx=60):
    return f'<path d="M{cx-22} 66 Q{cx} 60 {cx+22} 66 L{cx+24} 118 L{cx-24} 118 Z" fill="{SHIRT}"/>'


def kid_hold():
    arms = (
        f'<path d="M40 72 Q30 92 46 100" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<path d="M80 72 Q90 92 74 100" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<circle cx="47" cy="100" r="6" fill="{SKIN}"/>'
        f'<circle cx="73" cy="100" r="6" fill="{SKIN}"/>'
    )
    svg('kid-hold', 120, 160, legs() + shirt() + arms + head())
    svg('kid-hands', 120, 160,
        f'<path d="M40 86 Q34 96 46 100" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<path d="M80 86 Q86 96 74 100" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<circle cx="45" cy="99" r="7" fill="{SKIN}"/><circle cx="75" cy="99" r="7" fill="{SKIN}"/>')


def kid_point():
    arms = (
        f'<path d="M40 72 Q34 92 38 108" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<circle cx="38" cy="110" r="6" fill="{SKIN}"/>'
        f'<path d="M78 72 L106 68" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<path d="M104 62 h6 a6 6 0 0 1 0 12 h-6 Z" fill="{SKIN}"/>'
        f'<path d="M110 64 h10 a2.5 2.5 0 0 1 0 5 h-10" fill="{SKIN}"/>'
    )
    svg('kid-point', 125, 160, legs() + shirt() + arms + head())


def kid_up():
    arms = (
        f'<path d="M40 72 Q32 90 36 106" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<path d="M80 72 Q88 90 84 106" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<circle cx="36" cy="108" r="6" fill="{SKIN}"/><circle cx="84" cy="108" r="6" fill="{SKIN}"/>'
    )
    arrow = '<path d="M108 120 V40 M96 54 L108 40 L120 54" fill="none" stroke="#27ae60" stroke-width="6"/>'
    svg('stand-up', 130, 160, legs() + shirt() + arms + head() + arrow)


def kid_sit():
    chair = (
        '<rect x="28" y="60" width="10" height="70" rx="3" fill="#b9773b"/>'
        '<rect x="28" y="104" width="70" height="10" rx="3" fill="#b9773b"/>'
        '<rect x="30" y="114" width="8" height="36" fill="#9a5f2c"/>'
        '<rect x="88" y="114" width="8" height="36" fill="#9a5f2c"/>'
    )
    body = (
        f'<path d="M44 62 Q62 56 80 62 L82 106 L44 106 Z" fill="{SHIRT}"/>'
        f'<rect x="56" y="96" width="44" height="13" rx="5" fill="{PANTS}"/>'
        f'<rect x="88" y="100" width="13" height="40" rx="5" fill="{PANTS}"/>'
        f'<path d="M86 140 h20 v6 h-20 Z" fill="{INK}"/>'
        f'<path d="M76 70 Q90 84 84 96" fill="none" stroke="{SHIRT}" stroke-width="11"/>'
        f'<circle cx="84" cy="98" r="6" fill="{SKIN}"/>'
    )
    arrow = '<path d="M118 40 V112 M106 98 L118 112 L130 98" fill="none" stroke="#e67e22" stroke-width="6"/>'
    svg('sit-down', 140, 160, chair + body + head(62, 36) + arrow)


def objects():
    svg('book', 100, 100,
        '<rect x="22" y="16" width="58" height="70" rx="5" fill="#e74c3c"/>'
        '<rect x="22" y="16" width="12" height="70" rx="4" fill="#c0392b"/>'
        '<rect x="44" y="32" width="26" height="12" rx="2" fill="#fff6e5"/>')
    svg('robot', 100, 100,
        '<path d="M50 6 V16" fill="none"/><circle cx="50" cy="6" r="4" fill="#e74c3c"/>'
        '<rect x="30" y="16" width="40" height="28" rx="6" fill="#bdc3c7"/>'
        '<circle cx="41" cy="30" r="5" fill="#5dade2"/><circle cx="59" cy="30" r="5" fill="#5dade2"/>'
        '<rect x="24" y="48" width="52" height="34" rx="6" fill="#95a5a6"/>'
        '<rect x="40" y="56" width="20" height="12" rx="2" fill="#f4d03f"/>'
        '<path d="M24 56 L12 70 M76 56 L88 70" fill="none" stroke-width="6"/>'
        '<rect x="32" y="82" width="12" height="14" rx="2" fill="#7f8c8d"/>'
        '<rect x="56" y="82" width="12" height="14" rx="2" fill="#7f8c8d"/>')
    svg('watch', 100, 100,
        '<rect x="38" y="4" width="24" height="92" rx="6" fill="#a0522d"/>'
        '<circle cx="50" cy="50" r="24" fill="#f5f5f5"/>'
        '<path d="M50 50 V36 M50 50 L60 56" fill="none"/>'
        '<circle cx="50" cy="50" r="2.5" fill="#2b2b33"/>')
    svg('cake', 100, 100,
        '<rect x="14" y="58" width="72" height="30" rx="5" fill="#a0522d"/>'
        '<rect x="20" y="36" width="60" height="24" rx="5" fill="#f5b7d2"/>'
        '<path d="M20 46 q7 8 15 0 q7 8 15 0 q7 8 15 0 q7 8 15 0" fill="none" stroke="#fff" stroke-width="4"/>'
        '<rect x="34" y="18" width="6" height="18" fill="#5dade2"/><rect x="60" y="18" width="6" height="18" fill="#f4d03f"/>'
        '<path d="M37 8 q4 5 0 9 q-4 -4 0 -9Z" fill="#f39c12"/><path d="M63 8 q4 5 0 9 q-4 -4 0 -9Z" fill="#f39c12"/>')
    svg('pencil', 100, 100,
        '<path d="M18 74 L66 26 L78 38 L30 86 Z" fill="#f4d03f"/>'
        '<path d="M66 26 L72 20 Q78 16 82 22 L84 32 L78 38 Z" fill="#f1948a"/>'
        '<path d="M18 74 L30 86 L12 92 Z" fill="#f5deb3"/>'
        '<path d="M12 92 L15 83 L21 89 Z" fill="#2b2b33"/>')
    svg('present', 100, 100,
        '<rect x="16" y="40" width="68" height="50" rx="4" fill="#e74c3c"/>'
        '<rect x="12" y="30" width="76" height="14" rx="3" fill="#c0392b"/>'
        '<rect x="44" y="30" width="12" height="60" fill="#f4d03f"/>'
        '<path d="M50 30 Q30 8 26 22 Q24 32 50 30 Q76 32 74 22 Q70 8 50 30Z" fill="#f4d03f"/>')
    svg('ball', 100, 100,
        '<circle cx="50" cy="50" r="38" fill="#3498db"/>'
        '<path d="M16 36 Q50 50 84 36 M18 66 Q50 52 82 66 M50 12 Q36 50 50 88" fill="none" stroke="#fff" stroke-width="4"/>'
        '<circle cx="50" cy="50" r="38" fill="none"/>')
    svg('car', 100, 100,
        '<path d="M8 66 V52 Q8 44 18 42 L30 40 L40 26 Q42 24 46 24 H66 Q70 24 72 28 L80 42 Q92 44 92 54 V66 Z" fill="#e74c3c"/>'
        '<path d="M44 30 H56 V42 H36 Z" fill="#aed6f1"/><path d="M60 30 H68 L74 42 H60 Z" fill="#aed6f1"/>'
        '<circle cx="28" cy="68" r="11" fill="#2b2b33"/><circle cx="28" cy="68" r="4" fill="#bdc3c7"/>'
        '<circle cx="72" cy="68" r="11" fill="#2b2b33"/><circle cx="72" cy="68" r="4" fill="#bdc3c7"/>')
    svg('frog', 100, 100,
        '<ellipse cx="50" cy="64" rx="36" ry="26" fill="#58b947"/>'
        '<circle cx="32" cy="34" r="14" fill="#58b947"/><circle cx="68" cy="34" r="14" fill="#58b947"/>'
        '<circle cx="32" cy="34" r="7" fill="#fff"/><circle cx="68" cy="34" r="7" fill="#fff"/>'
        '<circle cx="33" cy="35" r="3" fill="#2b2b33" stroke="none"/><circle cx="69" cy="35" r="3" fill="#2b2b33" stroke="none"/>'
        '<path d="M30 62 Q50 78 70 62" fill="none"/>'
        '<ellipse cx="50" cy="82" rx="22" ry="7" fill="#a9dc76"/>')
    svg('teacher', 100, 120,
        '<path d="M30 70 Q50 62 70 70 L74 116 H26 Z" fill="#c0392b"/>'
        '<path d="M26 40 Q24 12 50 12 Q76 12 74 40 Q78 62 70 66 L66 40 H34 L30 66 Q22 62 26 40Z" fill="#d35400"/>'
        f'<circle cx="50" cy="40" r="19" fill="{SKIN}"/>'
        '<path d="M32 36 Q50 22 68 36 Q60 26 50 26 Q40 26 32 36Z" fill="#d35400"/>'
        '<circle cx="42" cy="42" r="6" fill="none" stroke-width="2.5"/><circle cx="58" cy="42" r="6" fill="none" stroke-width="2.5"/>'
        '<path d="M48 42 H52" fill="none" stroke-width="2.5"/>'
        '<path d="M44 52 Q50 57 56 52" fill="none"/>'
        '<rect x="62" y="84" width="22" height="28" rx="2" fill="#2e86c1"/>')
    svg('door-open', 100, 120,
        '<rect x="20" y="8" width="56" height="104" fill="#3b3a40"/>'
        '<path d="M20 8 L44 16 V104 L20 112 Z" fill="#c68642"/>'
        '<circle cx="38" cy="62" r="3" fill="#f4d03f"/>'
        '<path d="M58 60 H92 M82 50 L92 60 L82 70" fill="none" stroke="#27ae60" stroke-width="5"/>')
    svg('window-close', 120, 110,
        '<rect x="16" y="10" width="88" height="80" rx="3" fill="#aed6f1"/>'
        '<path d="M60 10 V90 M16 50 H104" fill="none"/>'
        '<rect x="10" y="88" width="100" height="10" rx="2" fill="#c68642"/>'
        '<path d="M4 50 H30 M22 42 L30 50 L22 58 M116 50 H90 M98 42 L90 50 L98 58" fill="none" stroke="#e67e22" stroke-width="5"/>')
    svg('doll', 100, 120,
        '<path d="M30 62 Q50 54 70 62 L82 108 H18 Z" fill="#9b59b6"/>'
        '<path d="M30 62 L70 62" fill="none"/>'
        '<path d="M28 34 Q26 8 50 8 Q74 8 72 34 Q80 50 74 58 Q66 46 66 34 H34 Q34 46 26 58 Q20 50 28 34Z" fill="#f4d03f"/>'
        f'<circle cx="50" cy="36" r="18" fill="{SKIN}"/>'
        '<path d="M32 30 Q50 16 68 30 Q58 22 50 22 Q42 22 32 30Z" fill="#f4d03f"/>'
        '<circle cx="43" cy="37" r="2.5" fill="#2b2b33" stroke="none"/><circle cx="57" cy="37" r="2.5" fill="#2b2b33" stroke="none"/>'
        '<path d="M44 45 Q50 50 56 45" fill="none"/>'
        '<circle cx="37" cy="43" r="3" fill="#f19a8a" stroke="none" opacity=".7"/><circle cx="63" cy="43" r="3" fill="#f19a8a" stroke="none" opacity=".7"/>'
        f'<rect x="36" y="106" width="9" height="10" rx="2" fill="{SKIN}"/><rect x="55" y="106" width="9" height="10" rx="2" fill="{SKIN}"/>'
        '<path d="M30 64 L20 86 M70 64 L80 86" fill="none" stroke="#9b59b6" stroke-width="8"/>')
    svg('bag', 100, 100,
        '<path d="M34 30 Q34 12 50 12 Q66 12 66 30" fill="none" stroke-width="5"/>'
        '<rect x="18" y="28" width="64" height="62" rx="12" fill="#e67e22"/>'
        '<rect x="28" y="54" width="44" height="26" rx="6" fill="#d35400"/>'
        '<path d="M28 62 H72" fill="none"/>'
        '<circle cx="50" cy="44" r="4" fill="#f4d03f"/>')
    svg('door', 100, 120,
        '<rect x="22" y="8" width="56" height="104" rx="3" fill="#c68642"/>'
        '<rect x="30" y="18" width="40" height="34" rx="2" fill="#b07434"/>'
        '<rect x="30" y="62" width="40" height="40" rx="2" fill="#b07434"/>'
        '<circle cx="68" cy="60" r="4" fill="#f4d03f"/>')
    svg('window', 120, 110,
        '<rect x="16" y="10" width="88" height="80" rx="3" fill="#aed6f1"/>'
        '<path d="M60 10 V90 M16 50 H104" fill="none"/>'
        '<rect x="10" y="88" width="100" height="10" rx="2" fill="#c68642"/>')
    svg('chair', 100, 100,
        '<rect x="24" y="8" width="10" height="56" rx="3" fill="#b9773b"/>'
        '<rect x="24" y="54" width="56" height="10" rx="3" fill="#b9773b"/>'
        '<rect x="26" y="64" width="8" height="30" fill="#9a5f2c"/><rect x="70" y="64" width="8" height="30" fill="#9a5f2c"/>')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    kid_hold(); kid_point(); kid_up(); kid_sit(); objects()
    print(len(os.listdir(OUT)), 'files')
