import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith('_'):
    print(f"{ERROR_COLOR}ERROR: Project slug '{project_slug}' cannot start with an underscore{RESET_ALL}")
    sys.exit(1)

print(f"{MESSAGE_COLOR}Creating project with slug '{project_slug}'")
print(f"Creating project at {os.getcwd()}{RESET_ALL}")
