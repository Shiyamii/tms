# load and run tms.py
from src.backlog import Backlog
from src.gui import GUI
from src.interface import Interface
from src.tms import TMS
from src.db import DB

if __name__ == "__main__":
    tms = TMS(GUI(), DB())
    tms.main()
