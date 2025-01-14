import sqlite3

# Функция для подключения к базе данных
def connect_db():
    return sqlite3.connect('warehouse.db')

# Функция для создания таблиц
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Room (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Rack (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_id INTEGER,
        name TEXT NOT NULL,
        capacity INTEGER,
        x INTEGER,
        y INTEGER,
        FOREIGN KEY (room_id) REFERENCES Room(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Shelf (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rack_id INTEGER,
        number INTEGER NOT NULL,
        FOREIGN KEY (rack_id) REFERENCES Rack(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Container (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shelf_id INTEGER,
        x INTEGER,
        y INTEGER,
        volume REAL,
        type TEXT,
        FOREIGN KEY (shelf_id) REFERENCES Shelf(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Item (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        container_id INTEGER,
        name TEXT NOT NULL,
        volume REAL,
        type TEXT,
        FOREIGN KEY (container_id) REFERENCES Container(id)
    )
    ''')

    conn.commit()
    conn.close()

# Функции для работы с помещениями
def add_room(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Room (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
def get_rooms():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Room')
    rooms = cursor.fetchall()
    conn.close()
    return rooms
def update_room(room_id, new_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Room SET name = ? WHERE id = ?', (new_name, room_id))
    conn.commit()
    conn.close()
def delete_room(room_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Room WHERE id = ?', (room_id,))
    conn.commit()
    conn.close()

# Функции для работы со стеллажами/шкафчиками
def add_rack(room_id, name, capacity, x, y):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Rack (room_id, name, capacity, x, y) VALUES (?, ?, ?, ?, ?)',
                   (room_id, name, capacity, x, y))
    conn.commit()
    conn.close()
def get_racks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Rack')
    racks = cursor.fetchall()
    conn.close()
    return racks
def update_rack(rack_id, new_name, new_capacity, new_x, new_y):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Rack SET name = ?, capacity = ?, x = ?, y = ? WHERE id = ?',
                   (new_name, new_capacity, new_x, new_y, rack_id))
    conn.commit()
    conn.close()
def delete_rack(rack_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Rack WHERE id = ?', (rack_id,))
    conn.commit()
    conn.close()

# Функции для работы с полками
def add_shelf(rack_id, number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Shelf (rack_id, number) VALUES (?, ?)', (rack_id, number))
    conn.commit()
    conn.close()
def get_shelves():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Shelf')
    shelves = cursor.fetchall()
    conn.close()
    return shelves
def update_shelf(shelf_id, new_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Shelf SET number = ? WHERE id = ?', (new_number, shelf_id))
    conn.commit()
    conn.close()
def delete_shelf(shelf_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Shelf WHERE id = ?', (shelf_id,))
    conn.commit()
    conn.close()


# Функции для работы с контейнерами
def add_container(shelf_id, x, y, volume, type_):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Container (shelf_id, x, y, volume, type) VALUES (?, ?, ?, ?, ?)',
                   (shelf_id, x, y, volume, type_))
    conn.commit()
    conn.close()
def get_containers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Container')
    containers = cursor.fetchall()
    conn.close()
    return containers
def update_container(container_id, new_x, new_y, new_volume, new_type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Container SET x = ?, y = ?, volume = ?, type = ? WHERE id = ?',
                   (new_x, new_y, new_volume, new_type, container_id))
    conn.commit()
    conn.close()
def delete_container(container_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Container WHERE id = ?', (container_id,))
    conn.commit()
    conn.close()


# Функции для работы с предметами
def add_item(container_id, name, volume, type_):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Item (container_id, name, volume, type) VALUES (?, ?, ?, ?)',
                   (container_id, name, volume, type_))
    conn.commit()
    conn.close()
def get_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Item')
    items = cursor.fetchall()
    conn.close()
    return items
def update_item(item_id, new_name, new_volume, new_type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Item SET name = ?, volume = ?, type = ? WHERE id = ?',
                   (new_name, new_volume, new_type, item_id))
    conn.commit()
    conn.close()
def delete_item(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Item WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

create_tables()
