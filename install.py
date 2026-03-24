import subprocess
import sys
import os
import shutil


def is_installed():
    return shutil.which("bwt-uploader") is not None


def install_package():
    if is_installed():
        print("'bwt-uploader' is already installed. Skipping installation.\n")
        return

    try:
        print("Installing 'bwt-uploader'...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "bwt-uploader"])
        print("Installation completed.\n")
    except subprocess.CalledProcessError as e:
        print("Installation failed.")
        sys.exit(e.returncode)


def run_uploader(config_path):
    if not config_path:
        print("Config path cannot be empty.")
        sys.exit(1)

    if not os.path.exists(config_path):
        print(f"Config file does not exist: {config_path}")
        sys.exit(1)

    if not os.path.isfile(config_path):
        print(f"Invalid config file: {config_path}")
        sys.exit(1)

    try:
        print(f"Executing: bwt-uploader -C {config_path}")
        subprocess.check_call(["bwt-uploader", "-C", config_path])
        print("Execution completed successfully.")
    except FileNotFoundError:
        print("Command 'bwt-uploader' not found.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"bwt-uploader failed with exit code {e.returncode}.")
        sys.exit(e.returncode)


def main():
    install_package()
    config_path = input("Enter config path: ").strip()
    run_uploader(config_path)


if __name__ == "__main__":
    main()
