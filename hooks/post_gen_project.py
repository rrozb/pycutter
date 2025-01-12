import os
import sys


def remove_cursor_config():
    """Remove .cursor file if not needed."""
    if "{{ cookiecutter.include_cursor_config }}" == "no":
        os.remove(".cursor")


def main():
    remove_cursor_config()


if __name__ == "__main__":
    main()
