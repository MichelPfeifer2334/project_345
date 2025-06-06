import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.database import Base
from backend.app.main import app, get_db
from fastapi.testclient import TestClient
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "app"))
# SQLite als Testdatenbank im Speicher (keine echte DB auf Festplatte)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Engine für Test-Datenbnak (SQLite im Speicher)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# SessionMaker für Tests
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 1. Datenbank einrichten: Erstelle Tebellen zu Beginn des Tests und lösche sie danach
@pytest.fixture(scope="session", autouse=True)
def setup_db():
    # Erstelle alle Tabellen aus der Base
    Base.metadata.create_all(bind=engine)
    yield
    # Tabellen nach Test wieder löschen
    Base.metadata.drop_all(bind=engine)

# 2. Test-DB Session für jeden Test
@pytest.fixture(scope="session")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# 4. Test-Client
@pytest.fixture()
def client():
    return TestClient(app)

# 3. Dependency Override für get_db: Testdatenbank verwenden
@pytest.fixture(scope="session", autouse=True)
def override_get_db(db):
    app.dependency_overrides[get_db] = lambda: db




