import sqlite3

connection = sqlite3.connect('database.db')

# 1. คำสั่งศักดิ์สิทธิ์: เปิดการใช้งาน Foreign Key บังคับของ SQLite
connection.execute("PRAGMA foreign_keys = ON;")

with open('schema.sql', 'w', encoding='utf-8') as f:
    f.write("""
DROP TABLE IF EXISTS Trip_Logs;
DROP TABLE IF EXISTS Vehicles;
DROP TABLE IF EXISTS Drivers;
DROP TABLE IF EXISTS Routes;
DROP TABLE IF EXISTS Bus_Stops;

CREATE TABLE Routes (
    route_id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_num TEXT NOT NULL UNIQUE,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL
);

CREATE TABLE Bus_Stops (
    stop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stop_name TEXT NOT NULL,
    zone TEXT NOT NULL
);

CREATE TABLE Vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate_number TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL DEFAULT 'Active'
);

CREATE TABLE Drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    shift TEXT NOT NULL
);

-- ตาราง Trip_Logs ที่มีการตั้ง Foreign Key แบบสมบูรณ์ พร้อมกฎ ON DELETE CASCADE
CREATE TABLE Trip_Logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_date DATE NOT NULL,
    status TEXT NOT NULL,
    vehicle_id INTEGER,
    driver_id INTEGER,
    route_id INTEGER,
    
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles (vehicle_id) ON DELETE CASCADE,
    FOREIGN KEY (driver_id) REFERENCES Drivers (driver_id) ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES Routes (route_id) ON DELETE CASCADE
);

-- (ใส่ข้อมูล Mock Data 50 Records)
INSERT INTO Routes (route_num, origin, destination) VALUES ('39', 'ม.ธรรมศาสตร์ รังสิต', 'อนุสาวรีย์ฯ'), ('510', 'ม.ธรรมศาสตร์ รังสิต', 'อนุสาวรีย์ฯ'), ('29', 'ม.ธรรมศาสตร์ รังสิต', 'หัวลำโพง'), ('34', 'รังสิต', 'หัวลำโพง'), ('504', 'รังสิต', 'สะพานกรุงเทพ'), ('520', 'ตลาดไท', 'มีนบุรี'), ('185', 'รังสิต', 'คลองเตย'), ('522', 'รังสิต', 'อนุสาวรีย์ฯ'), ('1138', 'รังสิต', 'ปทุมธานี'), ('90', 'ปทุมธานี', 'หมอชิต 2');
INSERT INTO Bus_Stops (stop_name, zone) VALUES ('ตรงข้าม ม.กรุงเทพ', 'ปทุมธานี'), ('ฟิวเจอร์พาร์ค', 'ปทุมธานี'), ('เซียร์ รังสิต', 'ปทุมธานี'), ('ดอนเมือง', 'กทม.เหนือ'), ('หลักสี่', 'กทม.เหนือ'), ('ม.เกษตร', 'กทม.เหนือ'), ('เซ็นทรัล ลาดพร้าว', 'กทม.เหนือ'), ('สวนจตุจักร', 'กทม.ชั้นใน'), ('สะพานควาย', 'กทม.ชั้นใน'), ('อนุสาวรีย์ฯ', 'กทม.ชั้นใน');
INSERT INTO Vehicles (plate_number, status) VALUES ('11-1234', 'Active'), ('11-5678', 'Active'), ('12-0001', 'Maintenance'), ('12-9999', 'Active'), ('13-4455', 'Active'), ('14-2233', 'Maintenance'), ('15-6789', 'Active'), ('16-1111', 'Active'), ('16-2222', 'Active'), ('17-8888', 'Active');
INSERT INTO Drivers (name, phone, shift) VALUES ('สมชาย', '081', 'Morning'), ('สมศักดิ์', '082', 'Afternoon'), ('สมบูรณ์', '083', 'Night'), ('วิชัย', '084', 'Morning'), ('ประเสริฐ', '085', 'Afternoon'), ('อำนาจ', '086', 'Morning'), ('บุญส่ง', '087', 'Afternoon'), ('มานพ', '088', 'Night'), ('ชูชาติ', '089', 'Morning'), ('กิตติ', '090', 'Afternoon');
INSERT INTO Trip_Logs (log_date, status, vehicle_id, driver_id, route_id) VALUES ('2026-05-11', 'In Progress', 1, 1, 1), ('2026-05-11', 'Completed', 2, 2, 2), ('2026-05-11', 'In Progress', 4, 4, 3), ('2026-05-11', 'Completed', 5, 5, 4), ('2026-05-11', 'Delayed', 7, 6, 5), ('2026-05-12', 'Scheduled', 8, 7, 1), ('2026-05-12', 'Scheduled', 9, 9, 2), ('2026-05-12', 'Scheduled', 10, 10, 8), ('2026-05-10', 'Completed', 1, 1, 1), ('2026-05-10', 'Completed', 2, 2, 2);
    """)

with open('schema.sql', 'r', encoding='utf-8') as f:
    connection.executescript(f.read())

print("สร้างฐานข้อมูลพร้อมเปิดใช้งาน Foreign Key สมบูรณ์แบบ!")
connection.commit()
connection.close()