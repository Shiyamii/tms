# load and run tms.py
import os
from database.database_connect import DatabaseConnect
from src.backlog import Backlog
from src.gui import GUI
from src.interface import Interface
from src.tms import TMS
from src.db import DB
from dotenv import load_dotenv

if __name__ == "__main__":
    if os.path.exists(".env.local"):
        load_dotenv(dotenv_path=".env.local")
    else:
        load_dotenv()

    interface = None
    if os.getenv("INTERFACE") == "gui":
        interface = GUI()
    else:
        interface = Interface()
    data = None
    if os.getenv("DATA") == "database":
        data = DB(DatabaseConnect())
    else:
        data = Backlog()
    tms = TMS(interface, data)
    tms.main()
