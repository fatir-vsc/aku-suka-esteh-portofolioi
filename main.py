import sqlite3
from config import *
from logic import DB_Manager

if __name__ == "__main__":
    db_manager = DB_Manager(DATABASE)
    db_manager.create_tables()