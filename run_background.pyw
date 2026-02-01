import sys
import os

# Ensure the root directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.main import main

if __name__ == "__main__":
    # In .pyw, there is no console, so prints won't show anywhere unless redirected.
    # We just run the main loop.
    main()
