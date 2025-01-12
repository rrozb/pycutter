{% if cookiecutter.project_type == "api" %}
from fastapi import FastAPI

app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.project_description }}",
    version="0.1.0",
)

@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Welcome to {{ cookiecutter.project_name }}!"}
{% else %}
def main() -> None:
    """Main function."""
    print("Welcome to {{ cookiecutter.project_name }}!")

if __name__ == "__main__":
    main()

{% endif %}