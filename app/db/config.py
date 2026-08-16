#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class Configurations:

    NAME = "configurations"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            motherboard  INTEGER NOT NULL,
            cpu INTEGER NOT NULL,
            hard-drive INTEGER,
            hard-drive-qty INTEGER,
            solid-drive INTEGER NOT NULL,
            solid-drive-qty INTEGER NOT NULL,
            ram INTEGER NOT NULL,
            ram-qty INTEGER NOT NULL,
            gpu INTEGER,
            case INTEGER NOT NULL,
            cooler INTEGER NOT NULL,
            network-card INTEGER,
            psu INTEGER,
            os INTEGER
        )
    """

    # SEED_DATA = """
    #     INSERT INTO note (title, pinned, body)
    #     VALUES
    #         ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
    #         ("Shopping List", 0, "Milk\nBread\nEggs\nCheese"),
    #         ("Meeting Notes", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
    #         ("Recipe: Pasta", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy!"),
    #         ("Important!",    1, "Remember to backup your database regularly.")
    # """

# Add more table classes here...

class Motherboards:

    NAME = "motherboards"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            platform TEXT NOT NULL,
            sata-ports INTEGER NOT NULL,
            pcie-ports INTEGER NOT NULL,
            m2-ports INTEGER NOT NULL,
            ram-gen TEXT NOT NULL,
            ram-slots INTEGER NOT NULL,
            ram-qty INTEGER NOT NULL,
            image TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO motherboards (name, cost, url, platform, sata-ports, pcie-ports, m2-ports, ram-gen, ram-slots, ram-qty)
        VALUES
            ("MSI B550M", 201.25, "https://www.pbtech.co.nz/product/MBDMSI4904278/MSI-B550M-PRO-VDH-WIFI-mATX-Motherboard-For-AMD-3r", "AM4", 4, 1, 2, "DDR4", 4)
            ("ASUS B860M-PLUS", 378.35, "https://www.pbtech.co.nz/product/MBDASU62412/ASUS-TUF-GAMING-B860M-PLUS-WIFI-MATX-Motherboard-S", "LGA1851", 4, 1, 3, "DDR5", 4)
    """

class HardDrives:

    NAME = "harddrives"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            powerdraw INTEGER NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            rpm INTEGER NOT NULL,
            image TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO harddrives (name, powerdraw, cost, url, capacity, rpm)
        VALUES
            ("Seagate BarraCuda 2TB", 5, 282 .97, "https://www.pbtech.co.nz/product/HDDSE2206/Seagate-BarraCuda-2TB-35-Internal-HDD-SATA3-6Gbs?qr=product_option", 2, 7200)
            ("WD Red Plus 4TB", 5, 481 .37, "https://www.pbtech.co.nz/product/HDDWD22403/WD-Red-Plus-4TB-35-Internal-HDD-SATA3---128MB-Cach", 4, 5400)
    """
class Cpus:

    NAME = "cpus"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            powerdraw INTEGER NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            platform TEXT NOT NULL,
            maxram INTEGER NOT NULL,
            image TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO cpus (name, powerdraw, cost, url, maxram, platform)
        VALUES
            ("Intel Core Ultra 5 245K", 159, 424.35, "https://www.pbtech.co.nz/product/CPUIT155245K/Intel-Core-Ultra-5-245K-CPU-14-Cores--14-Threads", 192, "LGA1851")
            ("Ryzen 5 5600", 65, 263.35, "https://www.pbtech.co.nz/product/CPUAMD05600/AMD-Ryzen-5-5600-CPU-6-Core--12-Thread---Max-Boost", 128, "AM4")
    """

class SolidDrives:

    NAME = "soliddrives"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            powerdraw INTEGER NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            capacity TEXT NOT NULL,
            speed INTEGER NOT NULL,
            image TEXT NOT NULL
        )
    """

class Ram:

    NAME = "ram"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            generation TEXT NOT NULL,
            speed INTEGER NOT NULL,
            image TEXT NOT NULL
        )
    """

class Gpus:

    NAME = "gpus"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            powerdraw INTEGER NOT NULL,
            image TEXT NOT NULL
        )
    """

class Case:

    NAME = "case"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            hard-drive-trays INTEGER NOT NULL,
            image TEXT NOT NULL
        )
    """

class Cooler:

    NAME = "cooler"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
        )
    """

class NetworkCard:

    NAME = "networdcard"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            speed INTEGER NOT NULL,
            image TEXT NOT NULL
        )
    """

class PowerSupply:

    NAME = "powersupply"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            power INTEGER NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            image TEXT NOT NULL
        )
    """

class OS:

    NAME = "os"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            image TEXT NOT NULL
        )
    """
#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    Configurations,
    Motherboards,
    HardDrives,
    Cpus,
    SolidDrives,
    Ram,
    Gpus,
    Case,
    Cooler,
    NetwordCard,
    PowerSupply,
    OS
]

