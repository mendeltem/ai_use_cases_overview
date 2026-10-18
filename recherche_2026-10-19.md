# Recherche neue Use Cases (Stand 2026-10-19)

15 Kandidaten, gegen die bestehenden Karten auf Dubletten geprüft (Stichwortsuche in index.html). Schlaganfall-Triage existiert bereits (Cluster 5, Viz.ai/Brainomix) → nur Update-Hinweis. CR = Firmenangabe (company-reported).
Format: Name EN / DE · Anbieter · Cluster · Reife · Datenlage (3/2/1) · Wachstum · Rechenlast

## A. Empfehlung: aufnehmen

### Medizin (Cluster 5)

1. **Sepsis early warning / Sepsis-Frühwarnung im Krankenhaus** · Bayesian Health (TREWS), UCSD (COMPOSER), Prenosis; Epic als Gegenbeispiel · 5 · prod · 3 · steady · 1/inf
   - TREWS (Nature Medicine, Jul 2022): 590.736 Patienten in 5 Kliniken. Bei 6.877 Sepsis-Fällen ging eine Alarmbestätigung innerhalb von 3 h mit −3,3 Prozentpunkten Mortalität einher (relativ −18,7 %, KI 9,4–27,0 %); Erkennung median 5,7 h früher. Beobachtungsstudie, kein RCT; Confounding-Kritik; Interessenkonflikte über die Ausgründung. COMPOSER (UCSD, npj Digit Med, Jan 2024): Vorher-nachher-Studie, n=6.217, Mortalität −1,9 Prozentpunkte (relativ −17 %).
   - Gegenbeispiel Epic Sepsis Model (JAMA Intern Med, Jun 2021): AUC 0,63, übersah ~2/3 der Sepsis-Fälle. Prenosis Sepsis ImmunoScore: erste FDA-De-Novo-Zulassung für KI-Sepsisdiagnostik (3.4.2024).
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC9512693 · https://medrxiv.org/content/10.1101/2022.08.08.22278526v2 · https://pmc.ncbi.nlm.nih.gov/articles/PMC8218233 · https://doaj.org/article/b461fc4226524012bf4fd58623c0aec8 · https://www.techtarget.com/pharmalifesciences/news/366607927/FDA-Authorizes-AI-Sepsis-Prediction-Detection-Tool
2. **Autonomous diabetic retinopathy screening / Autonomes Netzhaut-Screening bei Diabetes** · Digital Diagnostics (LumineticsCore, ehem. IDx-DR), Eyenuk (EyeArt), Google (ARDA) · 5 · prod · 3 · strong · 2/inf
   - IDx-DR 2018: erste FDA-Zulassung für autonome KI-Diagnose; Pivotalstudie n=900, Sensitivität 87,2 %, Spezifität 90,7 %. ACCESS-RCT (Nature Comms, Jan 2024, Jugendliche, n=164): Untersuchung abgeschlossen bei 100 % mit KI vs. 22 % mit Überweisung.
   - Google ARDA: prospektive Studie Thailand (Lancet Digit Health 2022), Sensitivität 91,4 % vs. 84,8 % bei Netzhautspezialisten; >600.000 Screenings (Okt 2024, CR). Zahl „>1 Mio. Patienten“ (2026) nur über Sekundärquelle gesehen → nicht verwenden.
   - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10784572/ · https://www.digitaldiagnostics.com/fda-permits-marketing-of-lumineticscore-formerly-known-as-idx-dr-for-automated-detection-of-diabetic-retinopathy-in-primary-care/ · https://research.google/pubs/real-time-diabetic-retinopathy-screening-by-deep-learning-in-a-multisite-national-screening-programme-a-prospective-interventional-cohort-study · https://blog.google/company-news/inside-google/around-the-globe/google-asia/arda-diabetic-retinopathy-india-thailand/
3. **Speech neuroprostheses / Sprach-Neuroprothesen (BCI)** · Stanford/BrainGate, UCSF, UC Davis, Neuralink, Synchron · 5 · research/pilot · 3 · strong · 2/edge+inf
   - Willett (Nature 2023): 62 Wörter/min; Metzger (Nature 2023): 78 Wörter/min mit Avatar; Card (NEJM 2024, ALS): 97,5 % Genauigkeit über 8,4 Monate, 125.000-Wort-Vokabular; Wairagkar (Nature 2025): Stimmsynthese mit ~25 ms Latenz. Alles Einzelfälle (1–2 Probanden).
   - Neuralink: 21 Teilnehmende (Jan 2026, CR via Reuters); Synchron COMMAND: 6 Patienten, 12 Monate ohne schwere gerätebezogene Ereignisse.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC9882398 · https://med.stanford.edu/news/all-news/2023/08/brain-implant-speech-als.html · https://pubmed.ncbi.nlm.nih.gov/39141853/ · https://pmc.ncbi.nlm.nih.gov/articles/PMC12369848/ · https://www.aol.com/articles/elon-musks-neuralink-says-21-183038116.html

### Natur & Kultur (Vorschlag neue Cluster, alternativ 7)

4. **Vesuvius Challenge – reading the Herculaneum scrolls / Herculaneum-Rollen lesen** · Vesuvius Challenge, Univ. Kentucky (Seales) · neu „Kultur“ · pilot · 2 · strong · 2/train+inf
   - 2023 Grand Prize 700.000 $: 15 Spalten, >2.000 griechische Zeichen. Titel gelesen: PHerc. 172 (2025), PHerc. 139 (Philodemos, Über die Götter). 25.06.2026: PHerc. 1667 als erste Rolle vollständig virtuell entrollt und gelesen (~20–22 Spalten; nur Preprint, Spaltenzahl je nach Quelle verschieden). Grand Prize 2027: 1 Mio. $ für eine ganze Rolle mit ≤8 h Handarbeit.
   - https://scrollprize.org/prizes · https://scrollprize.org/firstscroll · https://scrollprize.substack.com/p/60000-first-title-prize-awarded · https://archaeologymag.com/2026/07/herculaneum-scroll-read-for-the-first-time/ · https://www.ccs.uky.edu/ai-reads-an-entire-vesuvius-charred-scroll-for-the-first-time/
5. **AI-discovered Nazca geoglyphs / KI-entdeckte Nazca-Geoglyphen** · Yamagata-Universität, IBM Research · neu „Kultur“ · research · 3 · steady · 1/train+inf
   - PNAS, Sept 2024: 303 neue figurative Geoglyphen in einer Feldsaison (2022/23), bis dahin waren seit den 1940ern 430 bekannt. Die KI schlug ~1.300 Kandidaten vor, 178 der Funde direkt. Zahlen aus Abstract und Presse, Paper selbst nicht geöffnet.
   - https://doi.org/10.1073/pnas.2407652121 · https://archaeologymag.com/2024/09/ai-uncovers-303-new-nazca-geoglyphs-in-peru/ · https://heise.de/-9958445
6. **Camera-trap AI / KI für Kamerafallen** · Google + Conservation International (Wildlife Insights, SpeciesNet), MegaDetector · neu „Natur“ · prod · 2 · steady · 1/inf
   - SpeciesNet seit März 2025 Open Source: trainiert mit >65 Mio. Bildern, >2.000 Labels (CR). Wildlife Insights: >35 Mio. Trainingsbilder, 1.295 Arten (CR; Artenzahlen je nach Quelle widersprüchlich). Keine plattformweite Zahl zur Wirkung.
   - https://techcrunch.com/2025/03/03/google-releases-speciesnet-an-ai-model-designed-to-identify-wildlife/ · https://github.com/google/cameratrapai · https://www.wildlifeinsights.org/about-wildlife-insights-ai
7. **Deforestation alerts / Entwaldungs-Warnungen per Satellit** · Univ. Maryland (GLAD), Wageningen (RADD), WRI/Global Forest Watch · neu „Natur“ (alt. 7) · prod · 3 · steady · 2/inf
   - Moffette et al., Nature Climate Change 2021 (22 Länder, 2011–2018): In Afrika ging der Waldverlust dort, wo Organisationen GLAD-Alerts abonniert hatten, um 18 % zurück. Wert des vermiedenen CO₂ ~149–696 Mio. $. In Asien und Südamerika kein robuster Effekt. RADD (Radar) sieht durch Wolken, ~50 Tropenländer.
   - EarthRanger (Wilderei-Abwehr) höchstens als Nebensatz: >900 Standorte (CR), aber kein Wirkungsnachweis.
   - https://doi.org/10.1038/s41558-020-00956-w · https://geog.umd.edu/featured-content/estimated-annual-value-glad-alerts-lowering-deforestation-rates-149-696-million · https://www.wur.nl/en/research/products-services/radd-forest-disturbance-alert · https://www.globalforestwatch.org/blog/data/integrated-deforestation-alerts

### Medien & Alltag

8. **Recommender systems / Empfehlungsalgorithmen** · Meta, YouTube, Netflix, TikTok · 15 · prod · 2 (Wirkung peer-reviewed) · steady · 3/train+inf
   - Meta Q4/2025 (Call 28.01.2026, CR): Reels-Watchtime USA +>30 % ggü. Vorjahr, Facebook-Video +7 % Views durch Ranking. Guess et al., Science 2023: chronologischer statt algorithmischer Feed senkte die Nutzungszeit deutlich, kein messbarer Effekt auf Polarisierung.
   - „YouTube 70 %“ (2018) und „Netflix 80 %“ sind alt → nur als historisch kennzeichnen. Meta-Zahlen nur aus Sekundärzusammenfassungen des Calls.
   - https://www.marketbeat.com/instant-alerts/meta-platforms-q4-earnings-call-highlights-2026-01-28/ · https://csmapnyu.org/research/academic-research/how-do-social-media-feed-algorithms-affect-attitudes-and-behavior-in-an-election-campaign · https://www.tubefilter.com/2018/01/11/youtube-most-watch-time-driven-by-recommendations/
9. **Automated content moderation / Automatisierte Inhaltsmoderation** · alle sehr großen Plattformen unter dem DSA; Meta, TikTok · 9 (alt. 18) · prod · 3 · steady · 3/inf
   - DSA-Transparenzdatenbank (rollierend 180 Tage, Okt 2026): 4,41 Mrd. Begründungen von 375 Plattformen, 41 % vollautomatisch entschieden. Volumen stark von Marktplätzen dominiert (z. B. Google Shopping).
   - TikTok H2/2025 EU (CR): ~112 Mio. Entfernungen, 93,8 % ohne menschliche Prüfung. Meta Jan 2025: Automatik nur noch für schwere Verstöße; Fehlentscheidungen USA ~−50 %, zugleich weniger Entfernungen (CR).
   - https://transparency.dsa.ec.europa.eu/ · https://www.globaldatinginsights.com/news/tiktok-112-million-violative-pieces-of-content-removed-in-h2-2025/ · https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/ · https://smex.org/meta-claims-hate-speech-is-low-but-so-is-the-bar/
10. **Electronic line calling & semi-automated offside / Elektronische Linienrichter & halbautomatisches Abseits** · Hawk-Eye (Sony), Genius Sports, FIFA · 15 (oder neu „Sport“) · prod · 2 · strong · 2/edge
    - Wimbledon 2025: erstmals in 147 Jahren keine Linienrichter; >300 nicht mehr gebraucht, ~70 bleiben als Match Assistants. ATP: seit 2025 elektronische Linienentscheidung bei allen Turnieren. Panne am 06.07.2025: System eine Spielhälfte lang aus (Bedienfehler).
    - FIFA-WM 2022: 12 Tracking-Kameras, 29 Körperpunkte, 50 Messungen/s. Premier League: halbautomatisches Abseits seit 12.04.2025, ~30 s kürzere Checks angepeilt (Prognose, nicht gemessen).
    - https://www.espn.com/tennis/story/_/id/36312616/atp-dropping-line-judges-use-all-electronic-calls-2025 · https://www.skysports.com/tennis/news/12040/13393402/wimbledon-officials-apologise-to-players-after-line-calling-technology-turned-off-in-malfunction-on-centre-court · https://inside.fifa.com/technical/media-releases/semi-automated-offside-technology-to-be-used-at-fifa-world-cup-2022-tm · https://trainingground.guru/premier-league-to-introduce-semi-automated-offsides-on-april-12th/
11. **AI dubbing & synthetic voices / KI-Synchronisation & synthetische Stimmen** · YouTube, ElevenLabs, Amazon Prime Video · 15 (alt. 18) · early→prod · 2 · explosive · 2/inf
    - YouTube Auto Dubbing (CR): seit Dez 2024, 27 Sprachen; >6 Mio. Zuschauer pro Tag sehen ≥10 Min. auto-synchronisierte Inhalte (Dez 2025). ElevenLabs: 11 Mrd. $ Bewertung (Feb 2026), ARR >330 Mio. $ Ende 2025 (CR). Prime Video: Pilot mit 12 Titeln (März 2025). Netflix weglassen (keine Primärquelle).
    - https://blog.youtube/creator-and-artist-stories/youtube-auto-dubbing-explained/ · https://ppc.land/youtube-auto-dubbing-tops-6m-daily-viewers-expands-to-27-languages · https://tech.eu/2026/02/04/elevenlabs-raises-500m-says-building-towards-ipo/ · https://aboutamazon.com/news/entertainment/prime-video-ai-dubbing-english-spanish

## B. Optional (dünnere Belege)

12. AI hearing aids / KI-Hörgeräte mit DNN-Chip (Phonak Audéo Sphere Infinio, Aug 2024) · 5 · prod · 2 — DEEPSONIC-Chip, 22 Mio. Trainingsbeispiele, „bis 10 dB SNR“ (alles CR); keine unabhängige peer-reviewte Messung am Seriengerät gefunden. https://www.sonova.com/en/media/phonak-elevates-sound-quality-new-infinio-portfolio-introducing-paradigm-shift-real-time-ai · https://hearingreview.com/hearing-products/hearing-aids/phonak-launches-infinio-hearing-aid-with-real-time-ai
13. Bioacoustics / Bioakustik (BirdNET, Merlin, Rainforest Connection, Project CETI) · neu „Natur“ · prod/research · 2 — BirdNET: >2,2 Mio. Beitragende (PLOS Biol 2022), >6.000 Arten (CR); Arbimon >150 Mio. Minuten Audio (CR); CETI: „phonetisches Alphabet“ der Pottwale (Nat Commun 2024). Keine aktuellen Nutzerzahlen. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9239458/ · https://birdnet.cornell.edu/ · https://www.projectceti.org/blog-posts/sperm-whale-phonetic-alphabet-proposed-for-the-first-time
14. Live captions & sign-language AI / Live-Untertitel & Gebärdensprach-KI (Google Live Transcribe, SignGemma, Wiener Linien „Iris“) · 14 · prod/research · 1 — keine aktuellen Nutzerzahlen; der Deutsche Gehörlosen-Bund warnt vor Avataren statt Dolmetschern. Eher verwerfen. https://www.wienerlinien.at/news/weltneuheit-testbetrieb-unseres-geb%C3%A4rdenavatars-iris-startet · https://dglb.de/wp-content/uploads/2024/05/01_2024-Pressemitteilung_Gebaerdensprach-Avatare.pdf

## C. Update für bestehende Karte

15. Stroke triage AI (Cluster 5, schon vorhanden): neue Quelle Lancet Digital Health, 3.12.2025 — 26 NHS-Kliniken, Thrombektomie-Rate mit Brainomix 2,3 % → 4,6 % vs. 1,6 % → 2,6 % ohne (Beobachtungsstudie). Viz LVO Stepped-Wedge-RCT (JAMA Neurol 2023): −11,2 min bis Leistenpunktion, kein Unterschied im 90-Tage-Ergebnis. https://www.brainomix.com/brain/artificial-intelligence-imaging-decision-support-for-acute-stroke-treatment-in-england-a-prospective-observational-study/ · https://pmc.ncbi.nlm.nih.gov/articles/PMC12596299

## Vorschlag neue Cluster
- 21 Natur & Artenschutz (Kamerafallen, Entwaldungs-Warnungen, ggf. Bioakustik)
- 22 Kulturerbe & Archäologie (Vesuvius, Nazca)
