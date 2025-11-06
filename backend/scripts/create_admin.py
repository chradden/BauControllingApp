import os
import getpass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import all models to ensure relationships are resolved
from app.models import Base
from app.models.user import User, UserRole
from app.models.project import Project
from app.models.contract import Contract
from app.models.contract_cost import ContractCostAssignment
from app.models.invoice import Invoice
from app.models.invoice_line import InvoiceLine
from app.models.budget import BudgetLine
from app.models.din276 import DIN276CostGroup
from app.models.approval import InvoiceApproval
from app.models.funding import FundingCase
from app.core.security import hash_password
from dotenv import load_dotenv

# .env laden
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError('DATABASE_URL nicht gefunden!')
if DATABASE_URL.startswith('postgresql+asyncpg'):
    DATABASE_URL = DATABASE_URL.replace('+asyncpg', '+psycopg2')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def main():
    print("Admin-User anlegen:")
    email = input("E-Mail: ")
    name = input("Name: ")
    password = getpass.getpass("Passwort: ")

    # Validate password length (bcrypt limit)
    if len(password.encode('utf-8')) > 72:
        print("Fehler: Das Passwort ist zu lang. Maximal 72 Bytes erlaubt.")
        return

    # Setup database connection
    db_url = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/baucontrolling')
    if '+asyncpg' in db_url:
        db_url = db_url.replace('+asyncpg', '')
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Check if user already exists
    if session.query(User).filter_by(email=email).first():
        print("Fehler: Es existiert bereits ein Benutzer mit dieser E-Mail-Adresse")
        return

if __name__ == "__main__":
    main()
