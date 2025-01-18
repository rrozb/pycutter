{% if cookiecutter.project_type == "api" %}
import tomllib
from fastapi import FastAPI

from {{cookiecutter.project_slug}}.config import settings

_ = settings
VERSION = tomllib.load(open("pyproject.toml", "rb"))["project"]["version"]
app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.project_description }}",
    version=VERSION,
)

@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Welcome to {{ cookiecutter.project_name }}!"}
{% else %}
from {{cookiecutter.project_slug}}.config import settings

_ = settings

def main() -> None:
    """Main function."""
    print("Welcome to {{ cookiecutter.project_name }}!")

if __name__ == "__main__":
    main()

{% endif %}