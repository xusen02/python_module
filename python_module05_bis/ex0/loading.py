import pandas as pd
from importlib.metadata import version, PackageNotFoundError

def main() -> None:
    print("\nREAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    reagents = [
        ("pandas", "pandas", "Data manipulation ready"),
        ("numpy", "numpy", "Numerical computation ready"),
    ]

    all_present = True

    for package, module_name, description in reagents:
        try:
            import importlib
            importlib.import_module(module_name)
            installed_version = version(package)

            print(
                f"[OK] {package} ({installed_version})"
                f"- {description}"
            )
        except (ImportError, PackageNotFoundError):
            print(f"[MISSING] {package} is not installed")
            all_present = False
        except Exception as error:
            print(f"[ERROR] Unexpected issue with {package}: {error}")
            all_present = False


    print("\npip vs Poetry:")
    print(
        " requirements.txt declares what to install; pip resolves it at install time."
        " pyproject.toml declares the same constraints, and Poetry pins the resolved"
        " versions in poetry.lock so every install is identical."
    )
    print()
    if all_present:
        print("All reagents present and accounted for.")
    else:
        print("Some reagents are missing. Please run your package manager.")


if __name__ == "__main__":
    main()
