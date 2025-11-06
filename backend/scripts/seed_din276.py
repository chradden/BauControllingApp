import os
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# .env laden
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError('DATABASE_URL nicht gefunden!')
if DATABASE_URL.startswith('postgresql+asyncpg'):
    DATABASE_URL = DATABASE_URL.replace('+asyncpg', '+psycopg2')

Base = declarative_base()

class DIN276CostGroup(Base):
    __tablename__ = 'din276_cost_groups'
    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    parent_id = Column(Integer, ForeignKey('din276_cost_groups.id'))
    level = Column(Integer, nullable=False)

# Seed-Daten (alle Ebenen, wie in den Migrationen)
SEED_DATA = [
    # Level 1
    dict(id=1, code='100', name='Grundstück und Erschließung', description='Kosten für Grundstück, Erschließung und Rechte am Grundstueck', parent_id=None, level=1),
    dict(id=2, code='200', name='Vorbereitung des Bauvorhabens', description='Planung, Gutachten, Bodenuntersuchungen etc.', parent_id=None, level=1),
    dict(id=3, code='300', name='Bauwerk – Baukonstruktion', description='Tragwerk, Wände, Decken, Dach', parent_id=None, level=1),
    dict(id=4, code='400', name='Technische Anlagen', description='HKL, Elektro, Förderanlagen', parent_id=None, level=1),
    dict(id=5, code='500', name='Außenanlagen', description='Parkanlagen, Wege, Zufahrten', parent_id=None, level=1),
    dict(id=6, code='600', name='Ausstattung', description='Einbaumöbel, spezielle Ausstattungen', parent_id=None, level=1),
    dict(id=7, code='700', name='Baunebenkosten', description='Honorare, Gebühren, Versicherungen', parent_id=None, level=1),
    # Level 2
    dict(id=8, code='100.1', name='Grundstückskosten', description='Kaufpreis, Vermessung, Erschließungskosten (Untergruppe 100)', parent_id=1, level=2),
    dict(id=9, code='200.1', name='Planung & Voruntersuchungen', description='Architektur, Fachplanung, Gutachten (Untergruppe 200)', parent_id=2, level=2),
    dict(id=10, code='300.1', name='Gründung', description='Fundamente, Pfähle, Bodenverbesserung', parent_id=3, level=2),
    dict(id=11, code='300.2', name='Rohbau', description='Wände, Decken, Stützen, Betonarbeiten', parent_id=3, level=2),
    dict(id=12, code='300.3', name='Dach', description='Dacheindeckung, Dachkonstruktion', parent_id=3, level=2),
    dict(id=13, code='400.1', name='Heizung', description='Heizungsanlage und Verteilung', parent_id=4, level=2),
    dict(id=14, code='400.2', name='Sanitär', description='Sanitärinstallationen, Abwasser', parent_id=4, level=2),
    dict(id=15, code='400.3', name='Elektro', description='Elektroinstallation, Verteiler, Leitungen', parent_id=4, level=2),
    # Level 3
    dict(id=16, code='300.2.1', name='Innenwände - Trockenbau/Stein', description='Innenwände, Trennwände, nicht-tragend', parent_id=11, level=3),
    dict(id=17, code='300.2.2', name='Außenwände - Verblendung/Isolation', description='Außenwandaufbauten, Wärmeverbundsysteme', parent_id=11, level=3),
    dict(id=18, code='300.3.1', name='Dacheindeckung - Material', description='Dacheindeckung, Abdichtung, Unterkonstruktion', parent_id=12, level=3),
    dict(id=19, code='400.3.1', name='Beleuchtung', description='Allgemeinbeleuchtung, Notbeleuchtung', parent_id=15, level=3),
    dict(id=20, code='400.3.2', name='Stromversorgung & Verteiler', description='Versorgungsleitungen, Hauptverteiler', parent_id=15, level=3),
    dict(id=21, code='100.1.1', name='Anschluss- und Erschließungskosten', description='Anschlussleitungen, Aufschließungskosten', parent_id=8, level=3),
    dict(id=22, code='200.1.1', name='Genehmigungsplanung', description='Genehmigungen, Baugenehmigungen, Behördenwege', parent_id=9, level=3),
]

def main():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        for entry in SEED_DATA:
            obj = session.query(DIN276CostGroup).filter_by(code=entry['code']).first()
            if obj:
                # Update falls sich Name, Beschreibung, Parent oder Level geändert hat
                updated = False
                for k in ['name', 'description', 'parent_id', 'level']:
                    if getattr(obj, k) != entry[k]:
                        setattr(obj, k, entry[k])
                        updated = True
                if updated:
                    print(f"Update: {entry['code']} -> {entry['name']}")
                else:
                    print(f"Skip (exists, unverändert): {entry['code']}")
            else:
                obj = DIN276CostGroup(**entry)
                session.add(obj)
                print(f"Insert: {entry['code']} -> {entry['name']}")
        session.commit()
        print("DIN276 Seed abgeschlossen.")
    except Exception as e:
        session.rollback()
        print(f"Fehler: {e}")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    main()
