#!/bin/sh
# art.sh <name> "<subject>" [seed] — акварельна ілюстрація в стилі блогу, FLUX.1-schnell локально (mflux).
# Встановлення один раз: див. SKILL.md 2 класу, розділ «Онлайн-сторінка уроку».
ST="children's picture book illustration, soft watercolor style, cute, simple plain white background, no text, no letters"
OUT="$(dirname "$0")/../img/art"
TMP="$HOME/.cache/blog-gen/out"
mkdir -p "$OUT" "$TMP"
"$HOME/.cache/mflux-venv/bin/mflux-generate" --model dhairyashil/FLUX.1-schnell-mflux-4bit --base-model schnell \
  --steps 4 --seed "${3:-7}" --width 768 --height 768 --prompt "$2, $ST" --output "$TMP/$1.png" >/dev/null 2>&1 &&
ffmpeg -y -loglevel error -i "$TMP/$1.png" -vf scale=480:480 -q:v 4 "$OUT/$1.jpg" && echo "$OUT/$1.jpg"
