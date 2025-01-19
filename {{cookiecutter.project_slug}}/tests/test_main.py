{% if cookiecutter.project_type == "api" %}from fastapi.testclient import TestClient
from {{ cookiecutter.project_slug }}.main import app

client = TestClient(app)

def test_read_root() -> None:
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to {{ cookiecutter.project_name }}!"}
{% else %}
def test_placeholder() -> None:
    """Placeholder test."""
    assert True

{% endif %}