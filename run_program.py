# load and run tms.py
from src.interface import Interface
from src.tms import TMS

if __name__ == "__main__":
    tms = TMS(Interface())
    tms.main()
