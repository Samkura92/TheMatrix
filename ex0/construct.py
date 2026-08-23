import site
import sys
import os


def comparaison() -> None:
    if sys.prefix == sys.base_prefix:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment! "
              "The machines can see everything you install.")
        print()
        print("To enter the construc, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env/Scripts/activate # On Windows")
        print()
        print("Then run this program again")
    else:
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment! Safe to "
              "install packages without affecting the global system.")
        print()
        print(f"Package installation path: {site.getsitepackages()[0]}")


if __name__ == "__main__":
    comparaison()
