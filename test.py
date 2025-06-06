import os.path
from datetime import datetime

import macActionControl


if __name__ == "__main__":
    path = macActionControl.screenshot()
    print(f"Screenshot saved to {path}")