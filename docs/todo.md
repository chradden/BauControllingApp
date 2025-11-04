
# 🧭 To-Do Liste – Bau-Controlling App (MVP)

# 🧭 To-Do Liste – Bau-Controlling App (MVP)

---

## 🏁 Setup & Infra
- [ ] Repo anlegen (`baucontrolling-app`) mit LICENSE (MIT) & README  
- [ ] `.cursorrules` für Vibe-Coding Regeln hinzufügen (Tests, kleine Commits, Security)  
- [ ] Entwicklungsstack aufsetzen: FastAPI + PostgreSQL + React/Tailwind + Auth (OAuth2)  
- [ ] CI/CD einrichten (GitHub Actions oder Replit Deploy)  

---

## 🧩 Data Layer
- [ ] Tabellen erstellen: Project, DIN276CostGroup, BudgetLine, Contract, Invoice …  
- [ ] Alembic-Migrations generieren + Basis-Seed (DIN 276 Kostengruppen)  
- [ ] CRUD Endpoints (REST oder GraphQL)  
- [ ] Unit-Tests für Models & API  

---

## 🧱 Core Features
- [ ] Projekt-Stammdaten-Formular mit Upload (Bauantrag, Genehmigung)  
- [ ] Budget-Baseline je KG anlegen und ändern  
- [ ] Vertragsverwaltung + Nachtragsmanagement  
- [ ] Rechnungseingang (UI + Backend) mit Upload (XRechnung/PDF)  
- [ ] OCR-Stub integrieren (z. B. Tesseract oder Azure Form Recognizer)  
- [ ] Rechnungs-Zeilen → Kostengruppe zuordnen  
- [ ] Prüfworkflow (Status, Kommentare, Freigabe)  
- [ ] Audit-Trail (wer / wann / was)  

---

## 🧠 Automatische Prüfungen
- [ ] Duplikat-Check (Hash aus Rechnungsnr + IBAN + Betrag + Datum)  
- [ ] Budget-Check pro Kostengruppe (Hard/Soft-Limit)  
- [ ] Vertrags-Bezug prüfen (Three-Way-Match)  
- [ ] Steuer-Check (USt 0/7/19, Reverse Charge)  

---

## 📊 Dashboard & Reports
- [ ] Soll/Ist/Forecast Tabelle & Visualisierung (D3 oder Recharts)  
- [ ] Ampel-Logik für Budget-Abweichungen  
- [ ] Cash-Flow-Grafik (Monat / Quartal)  
- [ ] Export: Schlussverwendungsnachweis (PDF/Excel Template-Merge)  
- [ ] Export: DATEV Buchungssätze (CSV)  

---

## 🔒 Governance & Security
- [ ] Rollen & Rechte (Bauleitung, Prüfung, Controlling, GF)  
- [ ] Auth + Session Handling  
- [ ] Logging & AuditTrail Middleware  
- [ ] DSGVO-Konforme Datenspeicherung  
- [ ] Security Audit nach OWASP Top 10  

---

## 🧰 Nice to Have (Nach MVP)
- [ ] Mobiles Baustellen-Logbuch (Fotos, Sprachnotizen)  
- [ ] Mängel-Verfolgung & Ticketing  
- [ ] KI-gestützte OCR-Korrektur & LV-Zuordnung  
- [ ] Portfolio-Cockpit (mehrere Projekte + Risiko-Ampeln)  

---

## 🧭 Arbeitsweise (Vibe-Coding)
- Plan → Scaffold → Execute → Refine → Commit  
- Debug-Log (`debug-log.md`) führen  
- Security-Audits (`security-audit.md`) führen  
- Nach jedem Feature: Tests schreiben & Commit < 300 LOC  
- Automatisierte Checks bei Pull Requests  

---

**Letztes Update:** 2025-11-04
