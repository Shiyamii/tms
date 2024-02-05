# load and run tms.py
from src.backlog import Backlog
from src.interface import Interface
from src.tms import TMS
from src.db import DB

if __name__ == "__main__":
    DB()
    # tms = TMS(Interface(), Backlog())
    # tms.main()
