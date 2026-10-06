#!/usr/bin/env python3
"""Prueft deployments.json gegen die vier verbundenen Seiten.

deployments.json ist die einzige Zuordnungsdatei zwischen Use-Case-Board,
Supply Atlas, Firmenseite (AI_Companys) und Wiki (blackbeard_wikki). Ein
umbenannter Kartenname oder Atlas-Standort bricht die Links still, ohne
Fehlermeldung auf den Seiten. Dieses Skript findet solche Brueche.

Geprueft wird:
  - jeder Use-Case-Slug ist eine Karte im Board
  - jeder {"site": ...}-Ort und jeder Standort in companies.relations steht im Atlas
  - eigene Orte haben Name, Land, gueltige Koordinaten, Text de/en und eine https-Quelle
  - jeder Ticker (names, operators, use_cases, relations, wiki) hat eine Firmenseite
  - companies.cards nennt die Karten mit ihrem aktuellen Namen
  - jeder Wiki-Pfad existiert und hat einen Titel in wiki.entries

Quellen sind standardmaessig die veroeffentlichten Seiten; jede laesst sich
durch eine lokale Datei oder einen lokalen Klon ersetzen.

    python3 werkzeuge/verbund_pruefen.py
    python3 werkzeuge/verbund_pruefen.py --atlas ../Supply_Atlas3D/index.html \\
        --firmen ../AI_Companys/nvidia-oekosystem.html --wiki ../blackbeard_wikki

Ausgang 0 = alles in Ordnung, 1 = mindestens ein Fehler.
"""
import argparse
import json
import os
import re
import sys
import urllib.request

HIER = os.path.dirname(os.path.abspath(__file__))
BOARD = os.path.join(HIER, "..", "index.html")
DEP = os.path.join(HIER, "..", "deployments.json")
ATLAS = "https://mendeltem.github.io/Supply_Atlas3D/"
FIRMEN = "https://mendeltem.github.io/AI_Companys/nvidia-oekosystem.html"
WIKI_ROH = "https://raw.githubusercontent.com/mendeltem/blackbeard_wikki/main/knowledge/"


def lesen(quelle):
    if re.match(r"https?://", quelle):
        with urllib.request.urlopen(quelle, timeout=60) as r:
            return r.read().decode("utf-8")
    with open(quelle, encoding="utf-8") as f:
        return f.read()


def slug(name):
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", name.lower()))


def karten(html):
    """Kartenname en/de je Slug aus dem UC-Array des Boards."""
    teil = html[html.index("const UC = ["):html.index("const URLS")]
    aus = {}
    for m in re.finditer(r'U\(\d+,"[^"]*","\w+",\d,"\w+",\s*E\("((?:[^"\\]|\\.)*)","((?:[^"\\]|\\.)*)"\)', teil):
        aus[slug(m.group(1))] = {"en": m.group(1), "de": m.group(2)}
    return aus


def standorte(html):
    namen = set()
    for arr in ("MINES", "PLANTS", "DCS", "PROC", "POWER", "HUBS", "MEM"):
        i = html.index("const %s =" % arr)
        j = html.index("\n];", i)
        namen.update(re.findall(r'\{n:"([^"]+)"', html[i:j]))
    return namen


def ticker(html):
    m = re.search(r'id="daten" type="application/json">(.*?)</script>', html, re.S)
    return set(json.loads(m.group(1))["firmen"])


def wiki_da(wurzel, pfad):
    if re.match(r"https?://", wurzel):
        try:
            with urllib.request.urlopen(urllib.request.Request(wurzel + pfad, method="HEAD"), timeout=30):
                return True
        except Exception:
            return False
    return os.path.exists(os.path.join(wurzel, "knowledge", pfad))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dep", default=DEP)
    ap.add_argument("--board", default=BOARD)
    ap.add_argument("--atlas", default=ATLAS)
    ap.add_argument("--firmen", default=FIRMEN)
    ap.add_argument("--wiki", default=WIKI_ROH, help="lokaler Klon von blackbeard_wikki oder Roh-URL des Ordners knowledge/")
    a = ap.parse_args()

    d = json.loads(lesen(a.dep))
    k = karten(lesen(a.board))
    st = standorte(lesen(a.atlas))
    tk = ticker(lesen(a.firmen))
    fehler, hinweise = [], []

    for s, u in d["use_cases"].items():
        if s not in k:
            fehler.append("use_cases: Slug %s ist keine Karte" % s)
        if not u.get("places"):
            fehler.append("use_cases.%s: keine Orte" % s)
        for i, p in enumerate(u.get("places", [])):
            wo = "use_cases.%s.places[%d]" % (s, i)
            if "site" in p:
                if p["site"] not in st:
                    fehler.append("%s: Standort '%s' fehlt im Atlas" % (wo, p["site"]))
                continue
            for f in ("n", "c", "la", "lo", "en", "de", "src"):
                if not p.get(f) and p.get(f) != 0:
                    fehler.append("%s (%s): Feld %s fehlt" % (wo, p.get("n", "?"), f))
            if not (-90 <= p.get("la", 999) <= 90 and -180 <= p.get("lo", 999) <= 180):
                fehler.append("%s (%s): Koordinaten ausserhalb" % (wo, p.get("n")))
            if p.get("src") and not p["src"].startswith("https://"):
                hinweise.append("%s (%s): Quelle ohne https" % (wo, p.get("n")))
            if not re.fullmatch(r"[A-Z]{3}", p.get("c", "")):
                fehler.append("%s (%s): Land '%s' ist kein ISO-3-Code" % (wo, p.get("n"), p.get("c")))

    c = d.get("companies", {})
    alle = set(c.get("names", {}))
    for t in alle - tk:
        fehler.append("companies.names: %s hat keine Firmenseite" % t)
    for t in set(c.get("operators", {})) - alle:
        fehler.append("companies.operators: %s fehlt in names" % t)
    for s, ts in c.get("use_cases", {}).items():
        if s not in k:
            fehler.append("companies.use_cases: Slug %s ist keine Karte" % s)
        for t in set(ts) - alle:
            fehler.append("companies.use_cases.%s: %s fehlt in names" % (s, t))
        kk = c.get("cards", {}).get(s)
        if not kk:
            fehler.append("companies.cards: Name fuer %s fehlt" % s)
        elif s in k and (kk.get("en") != k[s]["en"] or kk.get("de") != k[s]["de"]):
            hinweise.append("companies.cards.%s: Name weicht von der Karte ab (%s / %s)" % (s, kk.get("en"), kk.get("de")))
    for t, rs in c.get("relations", {}).items():
        if t not in alle:
            fehler.append("companies.relations: %s fehlt in names" % t)
        for r in rs:
            if r["role"] not in c.get("roles", {}):
                fehler.append("companies.relations.%s: Rolle %s ohne Text in roles" % (t, r["role"]))
            for n in r["sites"]:
                if n not in st:
                    fehler.append("companies.relations.%s: Standort '%s' fehlt im Atlas" % (t, n))

    w = d.get("wiki")
    if w:
        pfade = set()
        for s, ps in w.get("use_cases", {}).items():
            if s not in k:
                fehler.append("wiki.use_cases: Slug %s ist keine Karte" % s)
            pfade.update(ps)
        for t, ps in w.get("companies", {}).items():
            if t not in alle:
                fehler.append("wiki.companies: %s fehlt in companies.names" % t)
            pfade.update(ps)
        at = w.get("atlas", {})
        pfade.update(at.get("ai_use", []))
        for ps in at.get("layers", {}).values():
            pfade.update(ps)
        for p in sorted(pfade):
            if p not in w.get("entries", {}):
                fehler.append("wiki.entries: Titel fuer %s fehlt" % p)
            if not wiki_da(a.wiki, p):
                fehler.append("wiki: %s existiert nicht" % p)

    orte = sum(len(u["places"]) for u in d["use_cases"].values())
    print("%d Karten im Board, %d mit Orten (%d Orte), %d Atlas-Standorte, %d Firmenseiten"
          % (len(k), len(d["use_cases"]), orte, len(st), len(tk)))
    print("%d Karten mit Firmenlinks, %d mit Wiki-Links" % (len(c.get("use_cases", {})), len((w or {}).get("use_cases", {}))))
    for h in hinweise:
        print("Hinweis: " + h)
    for f in fehler:
        print("FEHLER: " + f)
    print("in Ordnung" if not fehler else "%d Fehler" % len(fehler))
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
