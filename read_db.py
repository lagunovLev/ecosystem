from main import *


if __name__ == '__main__':
    db = Database("db.csv")
    e = db.read_ecosystem(Logger())
    e.display()
