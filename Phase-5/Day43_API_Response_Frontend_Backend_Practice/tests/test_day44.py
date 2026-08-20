import os
import pytest

mysql = pytest.importorskip("mysql.connector")


def test_database_configured():
    required = ["DB_HOST", "DB_USER", "DB_NAME"]
    missing = [key for key in required if not os.getenv(key)]
    if missing:
        pytest.skip("Set DB_HOST, DB_USER, and DB_NAME to run the live MySQL test.")
