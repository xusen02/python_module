import sys
import os


def check_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def get_environment_name() -> bool | None:
    if check_virtual_environment():
        return os.path.basename(sys.prefix)
    return None


def display_laboratory_status() -> None:
    print("\nLABORATORY STATUS:", end=" ")

    if check_virtual_environment():
        print("The laboratory is sealed\n")
    else:
        print("You are working in the open\n")

    print(f"Current Python: {sys.executable}")

    env_name = get_environment_name()

    if env_name:
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print()
        print("Reagent installation path:")

        # Display the package installation location
        import sysconfig
        print(sysconfig.get_path("purelib"))

    else:
        print("Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    display_laboratory_status()
