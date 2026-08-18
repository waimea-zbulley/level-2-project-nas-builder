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
            image TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO motherboards (name, cost, url, platform, sata-ports, pcie-ports, m2-ports, ram-gen, ram-slots, size)
        VALUES
            ("MSI B550M", 201.25, "https://www.pbtech.co.nz/product/MBDMSI4904278/MSI-B550M-PRO-VDH-WIFI-mATX-Motherboard-For-AMD-3r", "AM4", 4, 1, 2, "DDR4", 4,)
            ("ASUS B860M-PLUS", 378.35, "https://www.pbtech.co.nz/product/MBDASU62412/ASUS-TUF-GAMING-B860M-PLUS-WIFI-MATX-Motherboard-S", "LGA1851", 4, 1, 3, "DDR5", 4,)
            ("ASUS Z890 AYW", 516 .35, "https://www.pbtech.co.nz/product/MBDASU62521/ASUS-Z890-AYW-GAMING-WIFI-W-ATX-Motherboard-Suppor", "LGA1851", 4, 4, 4, "DDR5", 4,)
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
            image TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO harddrives (name, powerdraw, cost, url, capacity, rpm)
        VALUES
            ("Seagate BarraCuda 2TB", 5, 282 .97, "https://www.pbtech.co.nz/product/HDDSE2206/Seagate-BarraCuda-2TB-35-Internal-HDD-SATA3-6Gbs?qr=product_option", 2000, 7200)
            ("WD Red Plus 4TB", 5, 481 .37, "https://www.pbtech.co.nz/product/HDDWD22403/WD-Red-Plus-4TB-35-Internal-HDD-SATA3---128MB-Cach", 4000, 5400)
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
            image TEXT
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
            image TEXT
        )
    """
    SEED_DATA = """
        INSERT INTO soliddrives (name, powerdraw, cost, url, capacity, speed)
        VALUES
            ("Acer FA100 256gb", 4, 90.85, "https://www.pbtech.co.nz/product/HDDACN1050/Acer-FA100-256GB-M2-PCIe-Gen3-x-4-NVME-SSD-Read-up", 256, 1300)
            ("Crucial E100 2TB", 5, 456.30, "https://www.pbtech.co.nz/product/HDDCRU30130/Crucial-E100-2TB-NVMe-M2-Gen4-Internal-2280-SSD-PC", 2000, 4500)
            ("Kingston Fury Renegade 4TB", 10, 1148.85, "https://www.pbtech.co.nz/product/HDDKIN24300/Kingston-Fury-Renegade-4TB-M2-NVMe-Internal-SSD-wi", 4000, 7000)
    """
class Ram:

    NAME = "ram"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            generation TEXT NOT NULL,
            speed INTEGER NOT NULL,
            image TEXT
        )
    """
    SEED_DATA = """
        INSERT INTO ram (name, cost, url, capacity, generation, speed)
        VALUES
            ("PNY XLR8 8GB DDR4", 125.35, "https://www.pbtech.co.nz/product/MEMPNY11013/PNY-XLR8-8GB-DDR4-3200MTs-Desktop-UDIMM-Gaming-RAM", 8, "DDR4", 3200)
            ("PNY 16GB DDR5", 412.85, "https://www.pbtech.co.nz/product/MEMPNY0003/PNY-16GB-DDR5-Desktop-RAM-5600MTs---11V---CL46", 16, "DDR5", 5600)
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
            image TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO ram (name, cost, url, powerdraw)
        VALUES
            ("NVIDIA GeForce RTX 5080", "2701.35, "https://www.pbtech.co.nz/product/VGAZTC15084/Zotac-GAMING-NVIDIA-GeForce-RTX-5080-SOLID-Core-OC", 360)
            ("AMD Radeon RX 9060 XT", 746.35, "https://www.pbtech.co.nz/product/VGASAP390611/Sapphire-PULSE-AMD-Radeon-RX-9060-XT-Gaming-8GB-GD", 150)
    """

class Cases:

    NAME = "cases"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            hard-drive-trays INTEGER NOT NULL,
            image TEXT
        )
    """
    SEED_DATA = """
        INSERT INTO cases (name, cost, url, hard-drive-trays)
        VALUES
            ("Thermaltake Core P6 TG", 299.00, "https://computerlounge.co.nz/products/thermaltake-core-p6-tempered-glass-mid-tower-case-snow-edition", 4)
            ("Phanteks Enthoo Pro", 214.95, "https://www.pbtech.co.nz/product/CHAPHA6145/Phanteks-Enthoo-Pro-Tempered-Glass-Window-Full-Tow", 6)
            ("Phanteks XT PRO", 84.95, "https://www.pbtech.co.nz/product/CHAPHA0101/Phanteks-XT-PRO-Tempered-Glass-ATX-Case-1x-120mm-F", 2)
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

    SEED_DATA = """
        INSERT INTO cooler (name, cost, url)
        VALUES
            ("NZXT Air Cooler T120", 56.35, "https://www.pbtech.co.nz/product/FANNZX1021/NZXT-Air-Cooler-T120-RGB-CPU-Cooler-White-For-Inte")
            ("DEEPCOOL AG620 G2", 79.35, "https://www.pbtech.co.nz/product/FANDPC3070/DEEPCOOL-AG620-G2-CPU-Cooler-2-x-120mm-Fans-6-heat")
    """
class NetworkCard:

    NAME = "networkcard"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            speed REAL NOT NULL,
            image TEXT
        )
    """

SEED_DATA = """
        INSERT INTO networkcard (name, cost, url, speed)
        VALUES
            ("TP-Link TX401 10Gbps", 139, "https://www.pbtech.co.nz/product/NICTPL1001/TP-Link-TX401-10Gbps-PCI-E-Ethernet-Adapter-1-x-RJ", 10)
            ("ST2GPEX PCIe NIC Card", 68.99, "https://www.pbtech.co.nz/product/ADPSTT4643990/StarTechcom-ST2GPEX-PCIe-NIC-Card---1-Port-25GbE-2", 2.5)
    """

class PowerSupply:

    NAME = "powersupply"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            power INTEGER NOT NULL,
            image TEXT
        )
    """

SEED_DATA = """
        INSERT INTO powersupply (name, cost, url, power)
        VALUES
            ("DEEPCOOL Gamer Storm PF600x 600W", 79.35, "https://www.pbtech.co.nz/product/PSUDPC0006/DEEPCOOL-Gamer-Storm-PF600x-600W-80PLUS-230V-Bronz", 600)
            ("DEEPCOOL PQ1000G Black 1000W", 205.85, "https://www.pbtech.co.nz/product/PSUDPC10130/DEEPCOOL-PQ1000G-Black-1000W-ATX-31-Power-Supply-8", 1000)
    """
class OS:

    NAME = "os"

    SCHEMA = """
        CREATE TABLE note (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            cost    REAL NOT NULL,
            url  TEXT NOT NULL,
            image TEXT
        )
    """

    SEED_DATA = """
        INSERT INTO ram (name, cost, url)
        VALUES
            ("Truenas Scale", 0, "https://www.truenas.com")
            ("Unraid", 83, "https://account.unraid.net/buy")
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
    Cases,
    Cooler,
    NetwordCard,
    PowerSupply,
    OS
]

