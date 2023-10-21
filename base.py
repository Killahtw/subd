from sqlite3 import connect

conn = connect('move.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Agents (
        AgentID INTEGER PRIMARY KEY AUTOINCREMENT,
        CompanyName TEXT NOT NULL,
        AgentTypeID INTEGER NOT NULL,
        Address TEXT NOT NULL,
        INN TEXT NOT NULL,
        KPP TEXT NOT NULL,
        DirectorName TEXT NOT NULL,
        ContactPhone TEXT NOT NULL,
        ContactEmail TEXT NOT NULL,
        Logo BLOB,
        Priority INTEGER,
        RegistrationDate DATE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS AgentTypes (
        AgentTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        FOREIGN KEY (AgentTypeID) REFERENCES Agents (AgentTypeID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS AgentPriorityHistory (
        APHistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        AgentID INTEGER NOT NULL,
        ChangeDate DATE NOT NULL,
        FOREIGN KEY (AgentID) REFERENCES Agents (AgentID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Shop (
        ShopID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        AgentID INTEGER NOT NULL,
        FOREIGN KEY (AgentID) REFERENCES Agents (AgentID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        ProductTypeID INTEGER NOT NULL,
        Articul INTEGER NOT NULL,
        Description TEXT NOT NULL,
        Image BLOB,
        CountPerson INTEGER NOT NULL,
        NumberFactory INTEGER NOT NULL,
        MinCost INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProductCostHistory (
        PCHistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductID INTEGER NOT NULL,
        ChangeData DATE NOT NULL,
        FOREIGN KEY (ProductID) REFERENCES Product (ProductID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProductSale (
        ProductSaleID INTEGER PRIMARY KEY AUTOINCREMENT,
        AgentID INTEGER NOT NULL,
        ProductID INTEGER NOT NULL,
        SaleDate DATE NOT NULL,
        ProductCount INTEGER NOT NULL,
        FOREIGN KEY (AgentID) REFERENCES Agents (AgentID),
        FOREIGN KEY (ProductID) REFERENCES Product (ProductID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProductType (
        ProductTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        DefectsProduct TEXT NOT NULL,
        FOREIGN KEY (ProductTypeID) REFERENCES Product (ProductTypeID)
    )''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Materials (
        MaterialID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        TypeID TEXT NOT NULL,
        CountoNPack INTEGER NOT NULL,
        CountOnGarage INTEGER NOT NULL,
        MinCount INTEGER NOT NULL,
        Cout REAL NOT NULL,
        Image BLOB
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProductMaterial (
        ProductID INTEGER NOT NULL,
        MaterialID INTEGER NOT NULL,
        FOREIGN KEY (ProductID) REFERENCES Product (ProductID),
        FOREIGN KEY (MaterialID) REFERENCES Materials (MaterialID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS SupplierType (
        SupplierID INTEGER PRIMARY KEY,
        SupplierType TEXT,
        FOREIGN KEY (SupplierID) REFERENCES Supplier (SupplierType)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS MaterialType (
        MaterialTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        FOREIGN KEY (MaterialTypeID) REFERENCES Materials (MaterialID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS MaterialCountHistory (
        MCHistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        MaterialID INTEGER,
        ChangeData DATE NOT NULL,
        FOREIGN KEY (MaterialID) REFERENCES Materials (MaterialID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Supplier (
        SupplierID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        INN TEXT NOT NULL,
        StartPostavok DATE NOT NULL,
        RATE INTEGER NOT NULL,
        SupplierType INTEGER NOT NULL,
        FOREIGN KEY (SupplierType) REFERENCES SupplierType (SupplierID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS MaterialSupplier (
        MaterialID INTEGER,
        SupplierID INTEGER,
        FOREIGN KEY (MaterialID) REFERENCES Materials (MaterialID),
        FOREIGN KEY (SupplierID) REFERENCES Supplier (SupplierID)
    )
''')

conn.commit()
conn.close()