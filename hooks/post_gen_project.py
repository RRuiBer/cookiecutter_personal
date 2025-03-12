import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR} En progreso")
print(f"Iniciando un nuevo repositorio git")

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])

print(f"{MESSAGE_COLOR}Repositorio git creado{RESET_ALL}")
