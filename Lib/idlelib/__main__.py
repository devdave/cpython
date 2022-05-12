"""
IDLE main entry point

Run IDLE as python -m idlelib
"""
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))

import idlelib.pyshell
idlelib.pyshell.main()
# This file does not work for 2.7; See issue 24212.
