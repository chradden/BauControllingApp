import sys
import types

# When running tests in the dev container the sqlalchemy package may not be
# installed. We only need to import the FastAPI app to inspect OpenAPI paths,
# so create a minimal mock of the bits the app imports at module import time.
sql_mock = types.SimpleNamespace()
sql_mock.ext = types.SimpleNamespace()
sql_mock.ext.asyncio = types.SimpleNamespace(AsyncSession=object, create_async_engine=lambda *a, **k: None, async_sessionmaker=lambda *a, **k: None)
sql_mock.orm = types.SimpleNamespace(relationship=lambda *a, **k: None, DeclarativeBase=type("Base", (), {}))
sql_mock.Column = lambda *a, **k: None
sql_mock.Integer = int
sql_mock.String = str
sql_mock.Text = str
sql_mock.Date = object
sql_mock.ForeignKey = lambda *a, **k: None
sql_mock.Numeric = lambda *a, **k: float
sql_mock.Boolean = bool
sql_mock.select = lambda *a, **k: None

sys.modules["sqlalchemy"] = sql_mock
sys.modules["sqlalchemy.ext"] = sql_mock.ext
sys.modules["sqlalchemy.ext.asyncio"] = sql_mock.ext.asyncio
sys.modules["sqlalchemy.orm"] = sql_mock.orm

from fastapi.testclient import TestClient
from app.main import app


def test_openapi_includes_routes():
    client = TestClient(app)
    r = client.get("/openapi.json")
    assert r.status_code == 200
    data = r.json()
    paths = set(data.get("paths", {}).keys())
    # basic endpoints added by routers
    assert "/projects" in paths
    assert "/contracts" in paths
    assert "/invoices" in paths
    assert "/users" in paths
