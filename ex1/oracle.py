import os
from dotenv import load_dotenv
import sys

def print_env_info() -> dict[str, str | None]:
    env: dict[str, str | None] = {
        "Mode": os.environ.get("MATRIX_MODE"),
        "Database": os.environ.get("DATABASE_URL"),
        "API Access": os.environ.get("API_KEY"),
        "Log Level": os.environ.get("LOG_LEVEL"),
        "Remote Network": os.environ.get("ZION_ENDPOINT")
    }
    return env

def hardcoded_secrets_det(status) -> bool:
    try:
        with open(os.path.abspath(__file__), "r") as file:
            content = file.read()
    except OSError:
        return False
    for key in ("Database", "API Access"):
        value = status[key]
        if value and value in content:
            return True
    return False

def ignor_env(status) -> bool:
    if not os.path.exists(".gitignore"):
        return False
    try:
        with open(".gitignore", "r",) as file:
            content = file.read()
    except OSError:
        return False
    return ".env" in content


def produ_override(status) -> bool:
    if status["Mode"] != "production":
        return True
    if status["Log Level"] == "DEBUG":
        return True
    if status["Database"] and "localhost" in status["Database"]:
        return True
    return False


def security_check(status) -> None:
    print("Configuration security check:")
    if hardcoded_secrets_det(status):
        print("[WARNING] Hardcoded secrets detected!")
    else:
        print("[OK] No hardcoded secrets detected")

    if ignor_env(status):
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file did NOT ignored by git")

    if produ_override(status):
        print("[OK] Production overrides available")
    else:
        print("[WARNING] Production overrides unavailable")


def development_status(status: dict[str,str | None]) -> None:
    if status["Database"]:
        print("Database: Connected to local instance")
    else:
        print("Database: Cannot connect to database, please check url",
              file=sys.stderr)

    if status["API Access"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated", file=sys.stderr)

    if status["Log Level"]:
        print(f"Log Level: {status['Log Level']}")
    else:
        print("Log Level: DEBUG", file=sys.stderr)

    if status["Remote Network"]:
        print("Remote Network: Online")
    else:
        print("Remote Network: Undetected", file=sys.stderr)


def production_status(status: dict[str,str | None]) -> None:
    if status["Database"]:
        print("Database: Connected to database")
    else:
        print("Database: Cannot connect to database, program stop",
              file=sys.stderr)
        sys.exit(1)

    if status["API Access"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated, program stop", file=sys.stderr)
        sys.exit(1)

    if status["Log Level"]:
        print(f"Log Level: {status['Log Level']}")
    else:
        print("Log Level: PRODUCTION", file=sys.stderr)

    if status["Remote Network"]:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline", file=sys.stderr)


def main():
    load_dotenv()
    print("\nORACLE STATUS: Consulting the configuration...\n")
    status = print_env_info()
    print("Configuration loaded:")
    if status["Mode"] == "development":
        print("Mode: development")
        development_status(status)
    elif status["Mode"] == "production":
        print("Mode: production")
        production_status(status)
    elif status["Mode"] is None:
        print("[WARNING] Mode is blank, default 'development'")
        status["Mode"] = "development"
        development_status(status)
    else:
        print("[ERROR] Mode Not Found....", file=sys.stderr)
    print()
    security_check(status)
    print()
    print("The Oracle sees all configurations.")



if __name__ == "__main__":
    main()
