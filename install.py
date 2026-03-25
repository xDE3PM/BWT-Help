import subprocess
import sys
import os
import shutil

PACKAGE_NAME = "bwt-uploader"


def is_installed():
    return shutil.which(PACKAGE_NAME) is not None


def install_or_upgrade():
    try:
        if is_installed():
            choice = input(f"'{PACKAGE_NAME}' is already installed. Upgrade it? (y/n): ").strip().lower()
            if choice != "y":
                print("Skipping upgrade.\n")
                return

            print(f"Upgrading '{PACKAGE_NAME}'...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", PACKAGE_NAME])

        else:
            print(f"Installing '{PACKAGE_NAME}'...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", PACKAGE_NAME])

        print("Done.\n")

    except subprocess.CalledProcessError as e:
        print("Installation/Upgrade failed.")
        sys.exit(e.returncode)


def get_config_path():
    while True:
        config_path = input("Enter config path: ").strip().strip('"')

        if not config_path:
            print("Config path cannot be empty.\n")
            continue

        if not os.path.exists(config_path):
            print("File does not exist. Try again.\n")
            continue

        if not os.path.isfile(config_path):
            print("Not a valid file. Try again.\n")
            continue

        return config_path


def run_uploader(config_path):
    try:
        print(f"\n🚀 Running: {PACKAGE_NAME} -C {config_path}\n")
        subprocess.check_call([PACKAGE_NAME, "-C", config_path])
        print("\nExecution completed successfully.")

    except FileNotFoundError:
        print(f"Command '{PACKAGE_NAME}' not found.")
        sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"{PACKAGE_NAME} failed with exit code {e.returncode}.")
        sys.exit(e.returncode)


def main():
    print("=== BWT Uploader Runner ===\n")

    install_or_upgrade()
    config_path = get_config_path()
    run_uploader(config_path)


if __name__ == "__main__":
    main()
