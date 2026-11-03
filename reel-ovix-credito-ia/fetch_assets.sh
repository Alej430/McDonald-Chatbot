#!/usr/bin/env bash
# Scarica da Higgsfield gli asset usati dal reel nella cartella di lavoro indicata.
set -euo pipefail
W="${1:-work}"
mkdir -p "$W/clips"
G=https://d8j0ntlcm91z4.cloudfront.net/user_3Idb8TU2BuPB6hkrdEycqt5ydNQ
M=https://d2ol7oe51mr4n9.cloudfront.net/user_3Idb8TU2BuPB6hkrdEycqt5ydNQ
curl -fsSL -o "$W/clips/clip1.mp4" "$G/hf_20261103_085915_c2ffc96d-81a7-4872-83b5-2ee2d44d71c1.mp4"
curl -fsSL -o "$W/clips/clip2.mp4" "$G/hf_20261103_082240_9ca5215c-2357-4677-aac2-07ca94f66c90.mp4"
curl -fsSL -o "$W/clips/clip3.mp4" "$G/hf_20261103_085438_3e62acf4-8d71-4be0-a8ff-48b0b2a76e38.mp4"
curl -fsSL -o "$W/clips/clip4.mp4" "$G/hf_20261103_082940_09069151-6cf1-4037-a0fd-b4f653bdc827.mp4"
curl -fsSL -o "$W/clips/clip5.mp4" "$G/hf_20261103_085438_021456ea-7c9a-4976-aac1-216a94d32886.mp4"
curl -fsSL -o "$W/clips/clip6.mp4" "$G/hf_20261103_082250_3eb26ff4-828a-4f72-9d80-f79bdb0a85be.mp4"
curl -fsSL -o "$W/clips/clip7.mp4" "$G/hf_20261103_082249_e7959c2c-9009-41da-a08d-b00414766825.mp4"
curl -fsSL -o "$W/vo.mp3"          "$G/hf_20261103_082447_68045838-60ed-429a-964b-400fbd0d8346.mp3"
curl -fsSL -o "$W/logo_src.png"    "$M/06967df8-9fbb-4040-ad61-ea8e91ab061b.png"
echo "Asset scaricati in $W"
