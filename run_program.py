# load and run tms.py
from src.backlog import Backlog
from src.interface import Interface
from src.tms import TMS

if __name__ == "__main__":
    tms = TMS(Interface(), Backlog())
    tms.main()
