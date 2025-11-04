from app.schemas.project import ProjectCreate
from app.schemas.contract import ContractCreate
from app.schemas.invoice import InvoiceCreate
from app.schemas.user import UserCreate


def test_project_create_schema():
    p = ProjectCreate(name="Test Project", description="x")
    data = p.model_dump()
    assert data["name"] == "Test Project"


def test_contract_create_schema():
    c = ContractCreate(project_id=1, contractor="ACME", value=1234.5)
    data = c.model_dump()
    assert data["project_id"] == 1


def test_invoice_create_schema():
    i = InvoiceCreate(contract_id=1, amount=99.9)
    data = i.model_dump()
    assert data["contract_id"] == 1


def test_user_create_schema():
    u = UserCreate(email="a@b.com", password="secret")
    data = u.model_dump()
    assert data["email"] == "a@b.com"
