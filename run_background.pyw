import sys
import os
import subprocess

# Auto-activate .venv if not already running in it
base_dir = os.path.dirname(os.path.abspath(__file__))
venv_python = os.path.join(base_dir, ".venv", "Scripts", "pythonw.exe")

# Check if the current interpreter is the venv one
# We compare normalized paths to be safe
if os.path.exists(venv_python) and os.path.normcase(sys.executable) != os.path.normcase(venv_python):
    # Re-launch the script using the venv pythonw
    # subprocess.Popen detaches the new process, keeping it hidden (because of pythonw)
    subprocess.Popen([venv_python, __file__] + sys.argv[1:])
    sys.exit(0)

# Ensure the root directory is in sys.path
sys.path.append(base_dir)

from src.main import main

if __name__ == "__main__":
    # In .pyw, there is no console, so prints won't show anywhere unless redirected.
    # We just run the main loop.
    main()
