
# 🧱 Bau-Controlling App (DIN 276 + Fördermittel-Nachweis)
(Version 0.1 – MVP, 2025-11-04)
# 🧱 Bau-Controlling App (DIN 276 + Fördermittel-Nachweis)

**Projektname:** Bau-Controlling App  
**Version:** 0.1 (MVP)  
**Datum:** 2025-11-04  
**Autor:** Christian Radden  
**Zielplattform:** Web (App, Desktop first)  
**Technologien:** FastAPI + PostgreSQL + React/Tailwind + Auth (OAuth2)  
**Lizenz:** MIT  

---

## 🎯 Ziel
Ein zentrales System zur durchgängigen Kontrolle von Bauprojekten:  
vom Bauantrag → Budgetierung → Vergabe → Rechnungsprüfung → Zahlung → Schlussverwendungsnachweis.  

---

## 🚧 Problemstellung
- Kein einheitlicher Soll/Ist-Überblick über Baukosten.  
- Rechnungen werden manuell geprüft → Fehler, Doppelzahlungen.  
- Förder-Schlussverwendungsnachweise aufwendig und fehleranfällig.  

---

## 🌟 Zielnutzer
- Bauherren & Projektsteuerer  
- Bauleitung & Fachplanung  
- Controlling & Rechnungsprüfung  
- Geschäftsführung  

---

## ✅ Erfolgskriterien
| KPI | Zielwert |
|-----|-----------|
| Erfassungszeit pro Rechnung | < 5 min (inkl. OCR & Zuordnung) |
| Doppelzahlungen | 0 |
| Automatisierte Nachweis-Generierung | 100 % |
| Prüfhistorie dokumentiert | 100 % |

---

## 🧩 Kern-Funktionalitäten (MVP)
1. **Projekt-Stammdaten** – Bauantrag, Genehmigung, Förderkennzeichen  
2. **Kostenstruktur (DIN 276)** – Baselines, Forecast, Abweichungen  
3. **Verträge & Nachträge** – Lose, Auftragnehmer, Nachtragsmanagement  
4. **Rechnungseingang** – Upload (XRechnung / PDF), OCR, Zuordnung zur Kostengruppe  
5. **Prüfworkflow** – sachliche + rechnerische Prüfung, Freigabe, Audit-Trail  
6. **Automatische Checks** – Dubletten, Budgetüberschreitung, Vertragsbezug  
7. **Dashboard** – Soll/Ist/Forecast, Ampeln, Cash-Flow  
8. **Schlussverwendungsnachweis-Export** – automatisch befüllte Vorlage  

---

## 💡 Should-Have (später)
- Aufmaß & Abnahmeprotokolle  
- Nachtrags-Genehmigungs-Workflow  
- Vergabe-Übersichten & Berichte  
- Portfolio-Cockpit (Mehr-Projekt)  
- DATEV-Export & Schnittstelle  

---

## 🧱 Datenmodell (Entwurf)
**Tabellen (Hauptobjekte):**
- `Project`  
- `DIN276CostGroup`  
- `BudgetLine`  
- `Contract` ↔ `ChangeOrder`  
- `Invoice` ↔ `InvoiceLine` ↔ `Approval` ↔ `Payment`  
- `Measurement` ↔ `InvoiceLine`  
- `FundingCase` ↔ `Disbursement`  
- `User`, `Role`, `AuditLog`

---

## 🔁 Workflows
1. **Projektanlage** → Bauantrag, Baseline-Budget  
2. **Vergabe/Vertrag** → LV-Import, Vertragswert  
3. **Rechnungseingang** → OCR, Auto-Check, Prüfung, Freigabe  
4. **Controlling** → Dashboard, Abweichungs-Analyse  
5. **Projektabschluss** → Schlussrechnung, Nachweis-Export  

---

## 🛡 Governance & Compliance
- Vier-Augen-Prinzip bei Rechnungsprüfung  
- Änderungs-Historie pro Dokument  
- DSGVO-konforme Datenhaltung  
- Revisionssichere Ablage (Versionierung, Zeitstempel)  
- Rollen/Rechte: Bauleitung / Controlling / GF / Prüfung  

---

## 🔗 Integrationen
| Richtung | Schnittstelle | Format |
|-----------|----------------|---------|
| Import | XRechnung / ZUGFeRD | XML/PDF |
| Import | LV / Budget | CSV/Excel |
| Export | DATEV Buchungssätze | CSV |
| Export | Schlussverwendungsnachweis | Word/PDF-Template |

---

## ⚙️ Nicht-funktionale Anforderungen
- **Revisionssicherheit**, **Verschlüsselung**, **Audit-Trail**  
- **Mandantenfähigkeit** & **Multi-Projekt-Support**  
- **API-First** (Struktur für spätere App-Integration)  
- **Performante Suche und Filterung**  
- **Tests & Security-Audits** (OWASP 10)  

---

## 🔮 Risiken & Abhängigkeiten
- OCR-Qualität bei Rechnungen  
- Unterschiedliche Förder-Templates  
- Nutzerdisziplin bei LV-Pflege  
- Abhängigkeit von DATEV-Export-Mapping  

---

## 📅 Nächste Schritte (MVP-Sprint)
1. Basis-Stack + Auth einrichten  
2. Datenmodell & Migrations  
3. CRUD für Projekt + Kosten + Rechnung  
4. Prüfworkflow + Audit-Trail  
5. Dashboard + Export-Template  

---

**Letztes Update:** 2025-11-04  
