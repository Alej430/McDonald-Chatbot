# OVIX AI Solutions: reel "Credito d'imposta IA 2027"

Reel Instagram verticale **1080×1920, 39,6 s, 30 fps, H.264 + AAC**, realizzato con **Higgsfield** (B-roll video Seedance 2.5, voce ElevenLabs via Higgsfield TTS) e montato con `build_reel.py` (Python + Pillow + ffmpeg). Usa il **logo ufficiale ovix.ai** e la palette che ne deriva. **Target: tutte le PMI** (hotel, negozi, studi professionali, ristoranti, servizi).

**Video finale (libreria Higgsfield):**
https://d2ol7oe51mr4n9.cloudfront.net/user_3Idb8TU2BuPB6hkrdEycqt5ydNQ/d1a6182f-1834-47dc-bd60-2969d83cdad2.mp4

| Brand | Valore |
|---|---|
| Logo | `ovix.ai`, "ovix." in bianco e "ai" in giallo su nero (media Higgsfield `06967df8…`) |
| Giallo | `#FFD400` |
| Nero | `#0C0C0C` |
| Bianco | `#FFFFFF` |
| Font | Montserrat Black / Bold, sans geometrica pesante e coerente col lettering del logo |

---

## 1. Le 5 varianti di gancio

1. **"Lo sai che dal 2027 potresti avere fino al 30% di credito d'imposta sull'intelligenza artificiale?"** ✅ *scelta*
2. "Lo sai che lo Stato potrebbe restituirti fino al 30% di quello che spendi per l'IA nella tua attività?"
3. "Lo sai che il tuo assistente AI, dal 2027, potrebbe costarti fino al 30% in meno?"
4. "Lo sai che nella nuova manovra c'è un credito d'imposta sull'IA che quasi nessun titolare conosce?"
5. "Lo sai che hotel, negozi e studi professionali potrebbero avere un credito d'imposta sull'IA dal 2027?"

**Perché la n. 1.** Nei primi due secondi mette insieme tre elementi concreti: una data (2027), un numero (30%) e un beneficio comprensibile (credito d'imposta). Si apre con "Lo sai che…" e contiene già sia "potresti" sia "fino al", quindi resta prudente senza perdere forza. Le altre sono più deboli o più rischiose:
- la 2 ("restituirti") suggerisce un rimborso, che non è corretto: il credito si usa solo in compensazione;
- la 3 ("costarti meno") suona come una promessa di risparmio;
- la 4 è curiosa ma non dà un numero;
- la 5 lascia intendere che queste categorie siano sicuramente incluse, e non è verificato; inoltre restringe il pubblico, mentre il target sono tutte le PMI.

---

## 2. Script completo, scena per scena

| # | Tempo | Scena (B-roll Higgsfield) | Voce |
|---|---|---|---|
| 1 | 0,0–5,8 s | **Gancio.** Direttrice di un piccolo hotel, alla reception di sera, legge il telefono e si sorprende (push-in lento). | "Lo sai che dal 2027 potresti avere fino al 30% di credito d'imposta sull'intelligenza artificiale?" |
| 2 | 5,8–10,4 s | **La notizia.** Ripresa dall'alto: documento di bilancio, calcolatrice, espresso, una mano gira pagina. | "Lo prevede il disegno di legge di bilancio, ora in Parlamento: non è ancora legge." |
| 3 | 10,4–14,6 s | **Cosa riguarda.** Titolare di un negozio, dopo la chiusura, consulta il tablet al bancone. | "Riguarda gli abbonamenti a servizi cloud, anche di intelligenza artificiale." |
| 4 | 14,6–19,0 s | **OVIX.** Macro di uno smartphone: una chat di assistenza risponde in automatico (bolle gialle e grigie). | "Noi di OVIX offriamo assistenti AI e automazioni in abbonamento," |
| 5 | 19,0–23,6 s | **OVIX.** Studio professionale (commercialista, architetto…): la professionista sorride davanti a una dashboard, arriva una notifica. | "…conformi ad AI Act e GDPR: servizi che potrebbero rientrare." |
| 6 | 23,6–30,4 s | **Urgenza vera.** Clessidra con sabbia dorata su fondo nero. | "I fondi sono limitati, trenta milioni l'anno, e le regole non ci sono ancora. Chi si informa prima, arriva preparato." |
| 7 | 30,4–34,4 s | **CTA.** Ripresa aerea di un borgo valdostano all'ora blu, con le Alpi innevate. | "Seguimi per gli aggiornamenti e scrivimi in DM per capire se la tua attività potrebbe rientrare." |
| 8 | 34,4–39,6 s | **Chiusura.** Fondo nero con logo ovix.ai, CTA e disclaimer. | "Intanto, parlane col tuo commercialista." |

---

## 3. Testo per la generazione della voce

Generata con Higgsfield `text2speech_v2` (motore ElevenLabs, voce preset "Julian"). Durata 42,1 s, portata a circa 38,3 s in montaggio con `atempo=1.10`, che accelera senza cambiare il tono. Ritmo da reel, pause naturali sui punti.

> Lo sai che dal 2027 potresti avere fino al 30% di credito d'imposta sull'intelligenza artificiale? Lo prevede il disegno di legge di bilancio, ora in Parlamento: non è ancora legge. Riguarda gli abbonamenti a servizi cloud, anche di intelligenza artificiale. Noi di OVIX offriamo assistenti AI e automazioni in abbonamento, conformi ad AI Act e GDPR: servizi che potrebbero rientrare. I fondi sono limitati, trenta milioni l'anno, e le regole non ci sono ancora. Chi si informa prima, arriva preparato. Seguimi per gli aggiornamenti e scrivimi in DM per capire se la tua attività potrebbe rientrare. Intanto, parlane col tuo commercialista.

---

## 4. Testi a schermo (titoli grandi in alto)

| # | Etichetta (pillola gialla) | Titolo | Riga sotto |
|---|---|---|---|
| 1 | LO SAI CHE… | FINO AL 30% DI CREDITO D'IMPOSTA SULL'IA? | dal 2027 · se la legge verrà approvata |
| 2 | LA NOTIZIA | DDL BILANCIO 2027 | 🔴 IN PARLAMENTO · NON ANCORA LEGGE |
| 3 | COSA RIGUARDA | ABBONAMENTI CLOUD E IA | costi 2027 · 2028 · 2029 |
| 4 | OVIX · PER OGNI PMI | ASSISTENTI AI 24/7 | sito · WhatsApp · Telegram |
| 5 | IN ABBONAMENTO | AUTOMAZIONI SU MISURA | conformi AI Act e GDPR → potrebbero rientrare |
| 6 | PERCHÉ ORA | FONDI LIMITATI | 30 mln €/anno · regole da definire |
| 7 | HOTEL · NEGOZI · STUDI · PMI | SEGUI E SCRIVICI IN DM | per capire se la tua attività potrebbe rientrare |
| 8 | (chiusura) | logo ovix.ai · "AI Solutions per le PMI · Aosta" | SEGUI PER GLI AGGIORNAMENTI · SCRIVICI IN DM · Prima di tutto, parlane col tuo commercialista. |

I **sottotitoli** della voce sono bruciati nel video: Montserrat Black 64 px, bianco su box nero semitrasparente, all'altezza di circa 1300 px, fuori dalle aree coperte dall'interfaccia di Instagram. Numeri e parole chiave (30%, 2027, AI/IA, OVIX, DM, legge, potrebbe…) sono evidenziati in giallo.

---

## 5. Indicazioni visive

- **Stile.** Low-key cinematografico: interni caldi di sera con accenti gialli, coerenti col giallo `#FFD400` del logo. Contrasto alto, ombre profonde, nero come colore dominante del brand.
- **Inquadrature.**
  - Gancio: primo piano con push-in lento, e titolo e sottotitolo già visibili dal fotogramma 0 per fermare lo scroll.
  - Poi un'alternanza di dettagli (documento, smartphone in macro, clessidra) e mezze figure di titolari di PMI di settori diversi: hotel, negozio, studio professionale. Così ogni impresa può riconoscersi, non una sola nicchia.
  - CTA: ripresa aerea della Valle d'Aosta per il legame col territorio.
- **Transizioni.** Tagli netti a ritmo di voce (ogni 4–5 s, 7 s sulla clessidra per dare peso all'urgenza). Fade-in di 0,18 s su titoli e sottotitoli, fade in apertura della chiusura.
- **Brand presence.** Badge con il logo ovix.ai in alto a sinistra su pillola nera per tutto il video; logo grande nella chiusura.
- **Leggibilità.** Titoli 118–128 px Montserrat Black con contorno nero, sfumatura scura in alto dietro ai titoli, sottotitoli grandi in box. Le aree di sicurezza di Instagram sono rispettate: niente testo nei 250 px in basso né sul lato destro dei pulsanti.
- **Audio.** Voce normalizzata a −14 LUFS. Consiglio di aggiungere in app un **audio di tendenza strumentale a volume basso (10–15%)**: Instagram tende a premiarlo e non serve generare musica.

---

## 6. Caption

```
Lo sai che dal 2027 potresti avere fino al 30% di credito d'imposta sull'intelligenza artificiale? 🤖

Il DDL di bilancio 2027, approvato dal Consiglio dei ministri il 28 ottobre, è ora in Parlamento: NON è ancora legge.

Cosa prevede, in parole semplici:
✅ un credito d'imposta fino al 30% sui canoni di abbonamento a servizi cloud, comprese soluzioni di intelligenza artificiale
✅ per i costi del 2027, 2028 e 2029
✅ utilizzabile solo in compensazione
⚠️ fondi limitati: 30 milioni di euro l'anno
⚠️ le modalità di accesso arriveranno con un decreto attuativo, non ancora pubblicato

Hotel, negozi, studi professionali, ristoranti, attività di servizi: noi di OVIX AI Solutions lavoriamo con le PMI e offriamo in abbonamento assistenti AI che rispondono ai tuoi clienti 24/7 su sito, WhatsApp e Telegram, automazioni su misura (come le risposte alle recensioni) e gestionali personalizzati, nel rispetto di AI Act e GDPR. Sono servizi che POTREBBERO rientrare nell'agevolazione, se la legge verrà approvata e se le regole attuative lo confermeranno.

👉 Seguici per gli aggiornamenti
👉 Scrivici in DM per capire se la tua attività potrebbe rientrare
👉 Intanto parlane col tuo commercialista: è lui a poter verificare se e come l'agevolazione si applica al tuo caso.

ℹ️ Contenuto informativo, non costituisce consulenza fiscale. Il credito d'imposta non è garantito: dipende dall'approvazione definitiva della legge e dal decreto attuativo.

#creditodimposta #intelligenzaartificiale #leggedibilancio2027 #manovra2027 #agevolazionifiscali #piccoleimprese #pmi #partitaiva #commercialista #innovazionedigitale #assistenteai #chatbot #automazione #AIAct #GDPR #pmiitaliane #hotel #hotellerie #negozi #retail #studiprofessionali #liberiprofessionisti #ristoranti #turismo #aosta #valledaosta #vda #aostavalley #impresevaldostane #ovixai
```

---

## 7. Disclaimer a schermo (ultima scena)

> Contenuto informativo. Il DDL di bilancio 2027 non è ancora legge: il credito d'imposta è solo previsto e le modalità di accesso dipendono da un decreto attuativo non ancora emanato. L'applicabilità alla tua attività e ai singoli servizi va verificata con il tuo commercialista. OVIX non garantisce l'accesso all'agevolazione.

---

## 8. Come renderizzare

Il progetto è eseguibile con `build_reel.py`, che crea titoli, sottotitoli, badge e chiusura con Pillow e poi monta tutto con ffmpeg.

**Struttura attesa della cartella di lavoro:**
```
WORKDIR/
  clips/clip1.mp4 … clip7.mp4   # B-roll Higgsfield (vedi tabella sotto)
  vo.mp3                        # voce Higgsfield
  logo_src.png                  # logo ovix.ai 1920x1080 su nero
```

**Comandi:**
```bash
pip install pillow          # ffmpeg deve essere installato (apt/brew install ffmpeg)
./fetch_assets.sh WORKDIR   # scarica clip, voce e logo da Higgsfield
python3 build_reel.py WORKDIR ovix_reel_credito_ia.mp4
```
Servono i font Montserrat (Black, Bold, Medium), che si scaricano gratis da Google Fonts e vanno messi in `~/.fonts`.

**Per modificare:**
- tempi delle scene: `SCENES`;
- sottotitoli: `CAPTIONS`;
- titoli: `TITLES`;
- disclaimer: `DISCLAIMER`;
- velocità della voce: `VO_TEMPO`.

**Asset Higgsfield usati:**

| File | Contenuto | Job / media id |
|---|---|---|
| clip1.mp4 | hotel, direttrice sorpresa | `c2ffc96d-81a7-4872-83b5-2ee2d44d71c1` |
| clip2.mp4 | documento di bilancio | `9ca5215c-2357-4677-aac2-07ca94f66c90` |
| clip3.mp4 | negozio, titolare con tablet | `3e62acf4-8d71-4be0-a8ff-48b0b2a76e38` |
| clip4.mp4 | smartphone con chat AI | `09069151-6cf1-4037-a0fd-b4f653bdc827` |
| clip5.mp4 | studio professionale | `021456ea-7c9a-4976-aac1-216a94d32886` |
| clip6.mp4 | clessidra | `3eb26ff4-828a-4f72-9d80-f79bdb0a85be` |
| clip7.mp4 | Valle d'Aosta, ora blu | `e7959c2c-9009-41da-a08d-b00414766825` |
| vo.mp3 | voce italiana | `68045838-60ed-429a-964b-400fbd0d8346` |
| logo_src.png | logo ovix.ai | media `06967df8-9fbb-4040-ad61-ea8e91ab061b` |
| **output** | reel finale (versione PMI) | media `d1a6182f-1834-47dc-bd60-2969d83cdad2` |

Le clip sono state generate in 720p e portate a 1080×1920 in montaggio. Per una versione più nitida si possono rigenerare in 1080p con gli stessi prompt (circa 80 crediti per clip) e rilanciare lo script.

---

## Controllo finale di conformità

Ho riletto tutte le frasi di voce, testi a schermo e caption:

- **Il credito non è mai presentato come certo.** Si usano sempre "potresti", "fino al 30%", "se la legge verrà approvata", "non è ancora legge", "regole da definire".
- **Nessuna garanzia sui servizi OVIX.** Si dice solo che sono servizi che "potrebbero rientrare", e il disclaimer precisa che "OVIX non garantisce l'accesso all'agevolazione".
- **Nessun riferimento puntuale all'allegato.** Non compaiono né lettere né numeri; le cifre usate sono solo quelle verificate (30%, 2027–2029, 30 milioni l'anno).
- **Nessuna promessa di risparmio o guadagno.** Ho scartato le varianti di gancio "restituirti" e "costarti meno" per questo motivo.
- **Rimando al commercialista** presente in voce, chiusura, disclaimer e caption.

Due frasi riviste in corsa:
- "OVIX offre proprio questo" è diventata "Noi di OVIX offriamo…", per non suggerire una corrispondenza certa con la norma.
- Al posto di un'idea di rimborso ("restituirti", gancio 2), la caption precisa "utilizzabile solo in compensazione".

---

## Note operative

- **Verifiche prima della pubblicazione.**
  - La data del 28 ottobre 2026 per l'approvazione in Consiglio dei ministri e i dettagli dell'art. 12 sono riportati come forniti nel brief. Ricontrollali subito prima di pubblicare, perché il testo può cambiare durante l'esame parlamentare.
  - La voce è in prima persona ("Seguimi… scrivimi"), mentre la grafica e la caption usano "Seguici / Scrivici", più adatto a una pagina aziendale. Se preferisci uniformare, si cambia una riga.
