import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql', 'w', encoding='utf-8') as f:
    f.write("""
CREATE TABLE IF NOT EXISTS Routes (
    route_id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_num TEXT NOT NULL UNIQUE,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL
);

INSERT INTO Routes (route_num, origin, destination) VALUES
('39', 'มหาวิทยาลัยธรรมศาสตร์ ศูนย์รังสิต', 'อนุสาวรีย์ชัยสมรภูมิ'),
('510', 'มหาวิทยาลัยธรรมศาสตร์ ศูนย์รังสิต', 'อนุสาวรีย์ชัยสมรภูมิ'),
('29', 'มหาวิทยาลัยธรรมศาสตร์ ศูนย์รังสิต', 'หัวลำโพง'),
('34', 'รังสิต', 'หัวลำโพง'),
('504', 'รังสิต', 'สะพานกรุงเทพ'),
('520', 'ตลาดไท', 'มีนบุรี'),
('185', 'รังสิต', 'คลองเตย'),
('522', 'รังสิต', 'อนุสาวรีย์ชัยสมรภูมิ'),
('1138', 'รังสิต', 'ปทุมธานี'),
('90', 'ปทุมธานี', 'หมอชิต 2');

CREATE TABLE IF NOT EXISTS Bus_Stops (
    stop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stop_name TEXT NOT NULL,
    zone TEXT NOT NULL
);

INSERT INTO Bus_Stops (stop_name, zone) VALUES
('ตรงข้าม ม.กรุงเทพ (รังสิต)', 'ปทุมธานี'),
('ฟิวเจอร์พาร์ค รังสิต', 'ปทุมธานี'),
('เซียร์ รังสิต', 'ปทุมธานี'),
('สนามบินดอนเมือง', 'กรุงเทพฯ เหนือ'),
('หลักสี่', 'กรุงเทพฯ เหนือ'),
('มหาวิทยาลัยเกษตรศาสตร์', 'กรุงเทพฯ เหนือ'),
('เซ็นทรัล ลาดพร้าว', 'กรุงเทพฯ เหนือ'),
('สวนจตุจักร', 'กรุงเทพฯ ชั้นใน'),
('สะพานควาย', 'กรุงเทพฯ ชั้นใน'),
('อนุสาวรีย์ชัยสมรภูมิ', 'กรุงเทพฯ ชั้นใน');

CREATE TABLE IF NOT EXISTS Vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate_number TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL DEFAULT 'Active'
);

INSERT INTO Vehicles (plate_number, status) VALUES
('11-1234', 'Active'),
('11-5678', 'Active'),
('12-0001', 'Maintenance'),
('12-9999', 'Active'),
('13-4455', 'Active'),
('14-2233', 'Maintenance'),
('15-6789', 'Active'),
('16-1111', 'Active'),
('16-2222', 'Active'),
('17-8888', 'Active');

CREATE TABLE IF NOT EXISTS Drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    shift TEXT NOT NULL
);

INSERT INTO Drivers (name, phone, shift) VALUES
('สมชาย ใจดี', '081-111-1111', 'Morning'),
('สมศักดิ์ รักงาน', '082-222-2222', 'Afternoon'),
('สมบูรณ์ พูนสุข', '083-333-3333', 'Night'),
('วิชัย ขับไว', '084-444-4444', 'Morning'),
('ประเสริฐ เลิศล้ำ', '085-555-5555', 'Afternoon'),
('อำนาจ บาตรใหญ่', '086-666-6666', 'Morning'),
('บุญส่ง ตรงเวลา', '087-777-7777', 'Afternoon'),
('มานพ พบสุข', '088-888-8888', 'Night'),
('ชูชาติ มาดมั่น', '089-999-9999', 'Morning'),
('กิตติ ดีเลิศ', '090-000-0000', 'Afternoon');

CREATE TABLE IF NOT EXISTS Trip_Logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_date DATE NOT NULL,
    status TEXT NOT NULL,
    vehicle_id INTEGER,
    driver_id INTEGER,
    route_id INTEGER,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id),
    FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id),
    FOREIGN KEY (route_id) REFERENCES Routes(route_id)
);

INSERT INTO Trip_Logs (log_date, status, vehicle_id, driver_id, route_id) VALUES
('2026-05-11', 'In Progress', 1, 1, 1),
('2026-05-11', 'Completed', 2, 2, 2),
('2026-05-11', 'In Progress', 4, 4, 3),
('2026-05-11', 'Completed', 5, 5, 4),
('2026-05-11', 'Delayed', 7, 6, 5),
('2026-05-12', 'Scheduled', 8, 7, 1),
('2026-05-12', 'Scheduled', 9, 9, 2),
('2026-05-12', 'Scheduled', 10, 10, 8),
('2026-05-10', 'Completed', 1, 1, 1),
('2026-05-10', 'Completed', 2, 2, 2);
    """)

with open('schema.sql', 'r', encoding='utf-8') as f:
    connection.executescript(f.read())

print("สร้างฐานข้อมูล database.db และใส่ข้อมูล 50 Records เรียบร้อยแล้ว!")

connection.commit()
connection.close()