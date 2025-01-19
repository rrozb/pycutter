import os


def remove_cursor_config():
    """Remove .cursor and .coderabbit.yaml files if not needed."""
    if "{{ cookiecutter.include_cursor_config }}" == "no":
        os.remove(".cursor")
    if "{{ cookiecutter.include_coderabbit_config }}" == "no":
        os.remove(".coderabbit.yaml")


def main():
    remove_cursor_config()


if __name__ == "__main__":
    main()
