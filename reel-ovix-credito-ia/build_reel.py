#!/usr/bin/env python3
"""
OVIX AI Solutions - Reel "Credito d'imposta IA 2027" (1080x1920, ~39 s)

Monta il reel finale a partire da:
  WORKDIR/clips/clip1.mp4 ... clip7.mp4   (B-roll verticali generati con Higgsfield)
  WORKDIR/vo.mp3                          (voce italiana generata con Higgsfield TTS)
  WORKDIR/logo_src.png                    (logo ovix.ai 1920x1080 su nero)

Requisiti: python3 + Pillow, ffmpeg, font Montserrat ExtraBold/Bold (o Metropolis).
Uso:  python3 build_reel.py WORKDIR [OUTPUT.mp4]
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
YELLOW = (255, 212, 0)        # #FFD400 - giallo del logo ovix.ai
BLACK = (12, 12, 12)          # #0C0C0C - nero del logo
WHITE = (255, 255, 255)
RED = (230, 57, 70)

VO_TEMPO = 1.10               # voce leggermente accelerata: 42.1 s -> ~38.3 s
TOTAL = 39.6                  # durata finale del reel (s)

FONT_DIRS = ["/usr/share/fonts/truetype/higgsfield", "/usr/share/fonts/truetype",
             "/usr/share/fonts", os.path.expanduser("~/.fonts")]


def find_font(names):
    for d in FONT_DIRS:
        for root, _, files in os.walk(d):
            for n in names:
                if n in files:
                    return os.path.join(root, n)
    raise SystemExit(f"Font non trovato: {names}")


F_BLACK = find_font(["Montserrat-Black.ttf", "Montserrat-ExtraBold.ttf", "Metropolis-ExtraBold.ttf"])
F_BOLD = find_font(["Montserrat-Bold.ttf", "Montserrat-ExtraBold.ttf", "Metropolis-ExtraBold.ttf"])
F_REG = find_font(["Montserrat-Medium.ttf", "Montserrat-Regular.ttf", "Montserrat-Bold.ttf",
                   "Montserrat-ExtraBold.ttf", "Metropolis-ExtraBold.ttf"])

# ---------------------------------------------------------------------------
# MONTAGGIO VIDEO: (clip, inizio, fine) sulla timeline finale, in secondi
# ---------------------------------------------------------------------------
SCENES = [
    ("clip1.mp4", 0.0, 5.8),    # Gancio - direttrice di hotel sorpresa dal telefono
    ("clip2.mp4", 5.8, 10.4),   # La notizia - documento di bilancio
    ("clip3.mp4", 10.4, 14.6),  # Cosa riguarda - titolare di negozio con tablet
    ("clip4.mp4", 14.6, 19.0),  # OVIX - assistente AI risponde alle 2 di notte
    ("clip5.mp4", 19.0, 23.6),  # OVIX - automazioni, studio professionale
    ("clip6.mp4", 23.6, 30.4),  # Urgenza - clessidra, fondi limitati
    ("clip7.mp4", 30.4, 34.4),  # CTA - Aosta / Valle d'Aosta
    (None, 34.4, TOTAL),        # Chiusura - logo + disclaimer (grafica)
]

# ---------------------------------------------------------------------------
# SOTTOTITOLI (testo autoriale, tempi sulla voce accelerata)
# ---------------------------------------------------------------------------
CAPTIONS = [
    (0.00, 1.25, "Lo sai che dal 2027"),
    (1.25, 3.05, "potresti avere fino al 30%"),
    (3.05, 4.15, "di credito d'imposta"),
    (4.15, 5.90, "sull'intelligenza artificiale?"),
    (6.05, 7.95, "Lo prevede il DDL di bilancio,"),
    (7.95, 9.10, "ora in Parlamento:"),
    (9.10, 10.50, "non è ancora legge."),
    (10.60, 12.00, "Riguarda gli abbonamenti"),
    (12.00, 14.50, "a servizi cloud, anche di IA."),
    (14.70, 15.85, "Noi di OVIX offriamo"),
    (15.85, 17.60, "assistenti AI e automazioni"),
    (17.60, 18.70, "in abbonamento,"),
    (18.70, 21.50, "conformi ad AI Act e GDPR:"),
    (21.50, 23.50, "servizi che potrebbero rientrare."),
    (23.65, 25.10, "I fondi sono limitati,"),
    (25.10, 26.30, "30 milioni l'anno,"),
    (26.30, 28.20, "e le regole non ci sono ancora."),
    (28.35, 30.60, "Chi si informa prima, arriva preparato."),
    (30.90, 32.45, "Seguimi per gli aggiornamenti"),
    (32.45, 33.20, "e scrivimi in DM"),
    (33.20, 34.40, "per capire se la tua attività potrebbe rientrare."),
    # dalle 34.4 s la chiusura mostra a schermo "parlane col tuo commercialista" + disclaimer
]

# ---------------------------------------------------------------------------
# TESTI A SCHERMO (titoli grandi in alto, scena per scena)
#   (inizio, fine, kicker giallo, titolo, sottotitolo, stile)
# ---------------------------------------------------------------------------
TITLES = [
    (0.0, 5.8, "LO SAI CHE…", "FINO AL 30%\nDI CREDITO\nD'IMPOSTA SULL'IA?", "dal 2027 · se la legge verrà approvata", "hook"),
    (5.8, 10.4, "LA NOTIZIA", "DDL BILANCIO\n2027", "IN PARLAMENTO · NON ANCORA LEGGE", "warn"),
    (10.4, 14.6, "COSA RIGUARDA", "ABBONAMENTI\nCLOUD E IA", "costi 2027 · 2028 · 2029", "std"),
    (14.6, 19.0, "OVIX · PER OGNI PMI", "ASSISTENTI AI\n24/7", "sito · WhatsApp · Telegram", "std"),
    (19.0, 23.6, "IN ABBONAMENTO", "AUTOMAZIONI\nSU MISURA", "conformi AI Act e GDPR\n→ potrebbero rientrare", "std"),
    (23.6, 30.4, "PERCHÉ ORA", "FONDI\nLIMITATI", "30 mln €/anno · regole da definire", "std"),
    (30.4, 34.4, "HOTEL · NEGOZI · STUDI · PMI", "SEGUI\nE SCRIVICI\nIN DM", "per capire se la tua attività potrebbe rientrare", "std"),
]

DISCLAIMER = ("Contenuto informativo. Il DDL di bilancio 2027 non è ancora legge: "
              "il credito d'imposta è solo previsto e le modalità di accesso dipendono "
              "da un decreto attuativo non ancora emanato. L'applicabilità alla tua "
              "attività e ai singoli servizi va verificata con il tuo commercialista. "
              "OVIX non garantisce l'accesso all'agevolazione.")


# ---------------------------------------------------------------------------
def run(cmd):
    print("+", " ".join(cmd) if isinstance(cmd, list) else cmd, flush=True)
    subprocess.run(cmd, check=True)


def wrap(draw, text, font, max_w):
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            t = (cur + " " + w).strip()
            if draw.textlength(t, font=font) <= max_w:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, font, fill, stroke=0, stroke_fill=BLACK, lh=1.12, center=True):
    asc, desc = font.getmetrics()
    step = int((asc + desc) * lh)
    for ln in lines:
        tw = draw.textlength(ln, font=font)
        xx = (W - tw) / 2 if center else x
        draw.text((xx, y), ln, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
        y += step
    return y


def pill(draw, cx, y, text, font, bg, fg, pad=(28, 14)):
    tw = draw.textlength(text, font=font)
    asc, desc = font.getmetrics()
    h = asc + desc
    x0 = cx - tw / 2 - pad[0]
    draw.rounded_rectangle([x0, y, x0 + tw + 2 * pad[0], y + h + 2 * pad[1]], radius=(h + 2 * pad[1]) // 2, fill=bg)
    draw.text((x0 + pad[0], y + pad[1]), text, font=font, fill=fg)
    return y + h + 2 * pad[1]


def make_logo(src, out_dir):
    im = Image.open(src).convert("RGB")
    # ritaglio automatico del logo sul fondo nero
    bbox = Image.eval(im.convert("L"), lambda p: 255 if p > 40 else 0).getbbox()
    logo = im.crop(bbox)
    # il logo resta su fondo nero (#0C0C0C): lo usiamo solo su superfici nere del brand
    logo = logo.convert("RGB")
    logo.save(os.path.join(out_dir, "logo_crop.png"))
    return logo


def overlay_badge(logo, out):
    """Piccolo logo fisso in alto a sinistra su pillola nera (brand presence)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    lw = 200
    lg = logo.convert("RGB").resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    x, y = 56, 120
    d.rounded_rectangle([x - 22, y - 16, x + lw + 22, y + lg.height + 16], radius=24, fill=BLACK + (255,))
    img.paste(lg, (x, y))
    img.save(out)


def overlay_title(t, out):
    _, _, kicker, title, sub, style = t
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # scurimento morbido in alto per leggibilità
    grad = Image.new("L", (1, 900))
    for i in range(900):
        grad.putpixel((0, i), int(190 * (1 - i / 900) ** 1.6))
    shade = Image.new("RGBA", (W, 900), BLACK + (0,))
    shade.putalpha(grad.resize((W, 900)))
    img.alpha_composite(shade, (0, 0))

    y = 300
    y = pill(d, W / 2, y, kicker, ImageFont.truetype(F_BOLD, 40), YELLOW, BLACK) + 30
    size = 118 if style == "hook" else 128
    tf = ImageFont.truetype(F_BLACK, size)
    lines = wrap(d, title, tf, W - 120)
    while max(d.textlength(l, font=tf) for l in lines) > W - 100:
        size -= 6
        tf = ImageFont.truetype(F_BLACK, size)
        lines = wrap(d, title, tf, W - 120)
    fill = WHITE
    y = text_block(d, 0, y, lines, tf, fill, stroke=6, lh=1.02) + 18
    sf = ImageFont.truetype(F_BOLD, 42)
    if style == "warn":
        pill(d, W / 2, y, sub, sf, RED, WHITE)
    else:
        sl = wrap(d, sub, sf, W - 160)
        text_block(d, 0, y, sl, sf, YELLOW, stroke=4, lh=1.2)
    img.save(out)


def overlay_caption(text, out):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(F_BLACK, 64)
    lines = wrap(d, text, f, W - 200)
    asc, desc = f.getmetrics()
    step = int((asc + desc) * 1.1)
    y0 = 1300
    bh = step * len(lines) + 36
    bw = max(d.textlength(l, font=f) for l in lines) + 70
    d.rounded_rectangle([(W - bw) / 2, y0 - 18, (W + bw) / 2, y0 - 18 + bh], radius=28, fill=BLACK + (175,))
    for i, l in enumerate(lines):
        tw = d.textlength(l, font=f)
        # numeri e parole chiave in giallo
        x = (W - tw) / 2
        for word in l.split(" "):
            key = any(k in word for k in ("30", "2027", "IA", "AI", "OVIX", "DM", "commercialista", "potrebbe", "limitati", "legge"))
            d.text((x, y0 + i * step), word, font=f, fill=YELLOW if key else WHITE)
            x += d.textlength(word + " ", font=f)
    img.save(out)


def end_card(logo, out):
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    lw = 760
    lg = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    img.paste(lg, ((W - lw) // 2, 330))
    y = 330 + lg.height + 40
    y = text_block(d, 0, y, ["AI Solutions per le PMI · Aosta"], ImageFont.truetype(F_BOLD, 44), (200, 200, 200)) + 70
    y = pill(d, W / 2, y, "SEGUI PER GLI AGGIORNAMENTI", ImageFont.truetype(F_BLACK, 46), YELLOW, BLACK) + 26
    y = pill(d, W / 2, y, "SCRIVICI IN DM", ImageFont.truetype(F_BLACK, 46), WHITE, BLACK) + 50
    y = text_block(d, 0, y, wrap(d, "Prima di tutto, parlane col tuo commercialista.", ImageFont.truetype(F_BOLD, 46), W - 160),
                   ImageFont.truetype(F_BOLD, 46), WHITE) + 70
    d.line([(120, y), (W - 120, y)], fill=(70, 70, 70), width=2)
    y += 36
    df = ImageFont.truetype(F_REG, 30)
    text_block(d, 0, y, wrap(d, DISCLAIMER, df, W - 220), df, (175, 175, 175), lh=1.35)
    img.save(out)


def main():
    work = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    out_mp4 = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else os.path.join(work, "ovix_reel_credito_ia.mp4"))
    tmp = os.path.join(work, "build")
    os.makedirs(tmp, exist_ok=True)

    logo = make_logo(os.path.join(work, "logo_src.png"), tmp)
    overlay_badge(logo, os.path.join(tmp, "badge.png"))
    end_card(logo, os.path.join(tmp, "endcard.png"))
    for i, t in enumerate(TITLES):
        overlay_title(t, os.path.join(tmp, f"title{i}.png"))
    for i, c in enumerate(CAPTIONS):
        overlay_caption(c[2], os.path.join(tmp, f"cap{i}.png"))

    # 1) normalizza ogni scena a 1080x1920 / 30fps / durata esatta (rallenta se serve)
    segs = []
    for i, (clip, a, b) in enumerate(SCENES):
        dur = b - a
        seg = os.path.join(tmp, f"seg{i}.mp4")
        if clip is None:
            vf = (f"scale={W}:{H},zoompan=z='min(1+0.0006*on,1.04)':d={int(dur*FPS)+5}:s={W}x{H}:fps={FPS},"
                  f"fade=in:st=0:d=0.35")
            run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", os.path.join(tmp, "endcard.png"),
                 "-t", f"{dur:.3f}", "-vf", vf, "-r", str(FPS), "-pix_fmt", "yuv420p", "-an", seg])
        else:
            src = os.path.join(work, "clips", clip)
            sd = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                                "-of", "csv=p=0", src]).decode().strip())
            factor = max(1.0, dur / (sd - 0.05))
            vf = (f"setpts={factor:.4f}*PTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                  f"eq=contrast=1.05:saturation=1.05,fps={FPS}")
            if i == 0:
                vf += ",fade=in:st=0:d=0.15"
            run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-t", f"{dur:.3f}", "-vf", vf,
                 "-pix_fmt", "yuv420p", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", seg])
        segs.append(seg)

    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{s}'\n" for s in segs)
    base = os.path.join(tmp, "base.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", base])

    # 2) overlay: badge, titoli, sottotitoli (fade-in 0.2 s)
    inputs = ["-i", base]
    layers = [("badge.png", 0.0, SCENES[-1][1])]
    layers += [(f"title{i}.png", t[0], t[1]) for i, t in enumerate(TITLES)]
    layers += [(f"cap{i}.png", c[0], c[1]) for i, c in enumerate(CAPTIONS)]
    fc, last = [], "0:v"
    for k, (png, a, b) in enumerate(layers, start=1):
        inputs += ["-loop", "1", "-t", f"{b - a:.3f}", "-i", os.path.join(tmp, png)]
        fc.append(f"[{k}:v]format=rgba,fade=in:st=0:d=0.18:alpha=1,setpts=PTS+{a:.3f}/TB[o{k}]")
        fc.append(f"[{last}][o{k}]overlay=0:0:eof_action=pass:enable='between(t,{a:.3f},{b:.3f})'[v{k}]")
        last = f"v{k}"

    # 3) audio: voce accelerata (senza cambio di tono) + normalizzazione loudness
    ai = len(layers) + 1
    inputs += ["-i", os.path.join(work, "vo.mp3")]
    fc.append(f"[{ai}:a]atempo={VO_TEMPO},loudnorm=I=-14:TP=-1.5:LRA=11,apad[a]")
    run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(fc),
         "-map", f"[{last}]", "-map", "[a]", "-t", f"{TOTAL:.3f}", "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", out_mp4])
    print("OK ->", out_mp4)


if __name__ == "__main__":
    main()
