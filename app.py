import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def open_database():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/')
def index():
    db = open_database()

    total_vehicles = db.execute('SELECT COUNT(*) FROM Vehicles').fetchone()[0]

    active_vehicles = db.execute(
        "SELECT COUNT(*) FROM Vehicles WHERE status = 'Active'"
    ).fetchone()[0]
 
    db.close()

    return render_template('index.html', total=total_vehicles, active=active_vehicles)

@app.route('/vehicles')
def manage_vehicles():
    db = open_database()
 
    all_vehicles = db.execute(
        'SELECT vehicle_id AS id, plate_number AS plate, status FROM Vehicles'
    ).fetchall()
 
    db.close()
    return render_template('vehicles.html', items=all_vehicles)

@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    plate  = request.form.get('plate_number')
    status = request.form.get('status')
 
    db = open_database()
    db.execute(
        'INSERT INTO Vehicles (plate_number, status) VALUES (?, ?)',
        (plate, status)
    )
    db.commit()
    db.close()
 
    return redirect(url_for('manage_vehicles'))

@app.route('/edit_vehicle/<int:id>', methods=['GET', 'POST'])
def edit_vehicle(id):
    db = open_database()
 
    if request.method == 'POST':
        new_plate  = request.form.get('plate_number')
        new_status = request.form.get('status')
 
        db.execute(
            'UPDATE Vehicles SET plate_number = ?, status = ? WHERE vehicle_id = ?',
            (new_plate, new_status, id)
        )
        db.commit()
        db.close()
        return redirect(url_for('manage_vehicles'))

    vehicle = db.execute(
        'SELECT vehicle_id AS id, plate_number AS plate, status FROM Vehicles WHERE vehicle_id = ?',
        (id,)
    ).fetchone()
 
    db.close()
    return render_template('edit_vehicle.html', vehicle=vehicle)

@app.route('/delete_vehicle/<int:id>')
def delete_vehicle(id):
    db = open_database()
    db.execute('DELETE FROM Vehicles WHERE vehicle_id = ?', (id,))
    db.commit()
    db.close()
 
    return redirect(url_for('manage_vehicles'))

@app.route('/routes')
def manage_routes():
    db = open_database()
 
    all_routes = db.execute(
        'SELECT route_id AS id, route_num, origin, destination FROM Routes'
    ).fetchall()
 
    db.close()
    return render_template('routes.html', items=all_routes)

@app.route('/add_route', methods=['POST'])
def add_route():
    route_num   = request.form.get('route_num')
    origin      = request.form.get('origin')
    destination = request.form.get('destination')
 
    db = open_database()
    db.execute(
        'INSERT INTO Routes (route_num, origin, destination) VALUES (?, ?, ?)',
        (route_num, origin, destination)
    )
    db.commit()
    db.close()
 
    return redirect(url_for('manage_routes'))

@app.route('/edit_route/<int:id>', methods=['GET', 'POST'])
def edit_route(id):
    db = open_database()
 
    if request.method == 'POST':
        route_num   = request.form.get('route_num')
        origin      = request.form.get('origin')
        destination = request.form.get('destination')
 
        db.execute(
            'UPDATE Routes SET route_num = ?, origin = ?, destination = ? WHERE route_id = ?',
            (route_num, origin, destination, id)
        )
        db.commit()
        db.close()
        return redirect(url_for('manage_routes'))
 
    route = db.execute(
        'SELECT route_id AS id, route_num, origin, destination FROM Routes WHERE route_id = ?',
        (id,)
    ).fetchone()
 
    db.close()
    return render_template('edit_route.html', route=route)

@app.route('/delete_route/<int:id>')
def delete_route(id):
    db = open_database()
    db.execute('DELETE FROM Routes WHERE route_id = ?', (id,))
    db.commit()
    db.close()
 
    return redirect(url_for('manage_routes'))

@app.route('/drivers')
def manage_drivers():
    db = open_database()
 
    all_drivers = db.execute(
        'SELECT driver_id AS id, name, phone, shift FROM Drivers'
    ).fetchall()
 
    db.close()
    return render_template('drivers.html', items=all_drivers)

@app.route('/add_driver', methods=['POST'])
def add_driver():
    name  = request.form.get('name')
    phone = request.form.get('phone')
    shift = request.form.get('shift')
 
    db = open_database()
    db.execute(
        'INSERT INTO Drivers (name, phone, shift) VALUES (?, ?, ?)',
        (name, phone, shift)
    )
    db.commit()
    db.close()
 
    return redirect(url_for('manage_drivers'))

@app.route('/edit_driver/<int:id>', methods=['GET', 'POST'])
def edit_driver(id):
    db = open_database()
 
    if request.method == 'POST':
        name  = request.form.get('name')
        phone = request.form.get('phone')
        shift = request.form.get('shift')
 
        db.execute(
            'UPDATE Drivers SET name = ?, phone = ?, shift = ? WHERE driver_id = ?',
            (name, phone, shift, id)
        )
        db.commit()
        db.close()
        return redirect(url_for('manage_drivers'))
 
    driver = db.execute(
        'SELECT driver_id AS id, name, phone, shift FROM Drivers WHERE driver_id = ?',
        (id,)
    ).fetchone()
 
    db.close()
    return render_template('edit_driver.html', item=driver)

@app.route('/delete_driver/<int:id>')
def delete_driver(id):
    db = open_database()
    db.execute('DELETE FROM Drivers WHERE driver_id = ?', (id,))
    db.commit()
    db.close()
 
    return redirect(url_for('manage_drivers'))

@app.route('/bus_stops')
def manage_bus_stops():
    db = open_database()
 
    all_stops = db.execute(
        'SELECT stop_id AS id, stop_name, zone FROM Bus_Stops'
    ).fetchall()
 
    db.close()
    return render_template('bus_stops.html', items=all_stops)

@app.route('/add_bus_stop', methods=['POST'])
def add_bus_stop():
    stop_name = request.form.get('stop_name')
    zone      = request.form.get('zone')
 
    db = open_database()
    db.execute(
        'INSERT INTO Bus_Stops (stop_name, zone) VALUES (?, ?)',
        (stop_name, zone)
    )
    db.commit()
    db.close()
 
    return redirect(url_for('manage_bus_stops'))

@app.route('/edit_bus_stop/<int:id>', methods=['GET', 'POST'])
def edit_bus_stop(id):
    db = open_database()
 
    if request.method == 'POST':
        stop_name = request.form.get('stop_name')
        zone      = request.form.get('zone')
 
        db.execute(
            'UPDATE Bus_Stops SET stop_name = ?, zone = ? WHERE stop_id = ?',
            (stop_name, zone, id)
        )
        db.commit()
        db.close()
        return redirect(url_for('manage_bus_stops'))
 
    stop = db.execute(
        'SELECT stop_id AS id, stop_name, zone FROM Bus_Stops WHERE stop_id = ?',
        (id,)
    ).fetchone()
 
    db.close()
    return render_template('edit_bus_stop.html', item=stop)
 
@app.route('/delete_bus_stop/<int:id>')
def delete_bus_stop(id):
    db = open_database()
    db.execute('DELETE FROM Bus_Stops WHERE stop_id = ?', (id,))
    db.commit()
    db.close()
 
    return redirect(url_for('manage_bus_stops'))

@app.route('/trip_logs')
def manage_trip_logs():
    db = open_database()
 
    all_logs = db.execute('''
        SELECT
            t.log_id      AS id,
            t.log_date    AS date,
            v.plate_number AS vehicle,
            d.name         AS driver,
            r.route_num    AS route,
            t.status
        FROM Trip_Logs t
        JOIN Vehicles v ON t.vehicle_id = v.vehicle_id
        JOIN Drivers  d ON t.driver_id  = d.driver_id
        JOIN Routes   r ON t.route_id   = r.route_id
    ''').fetchall()
 
    all_vehicles = db.execute('SELECT vehicle_id, plate_number FROM Vehicles').fetchall()
    all_drivers  = db.execute('SELECT driver_id, name FROM Drivers').fetchall()
    all_routes   = db.execute('SELECT route_id, route_num FROM Routes').fetchall()
 
    db.close()
 
    return render_template(
        'trip_logs.html',
        items    = all_logs,
        vehicles = all_vehicles,
        drivers  = all_drivers,
        routes   = all_routes
    )
 
@app.route('/add_trip_log', methods=['POST'])
def add_trip_log():
    log_date   = request.form.get('log_date')
    vehicle_id = request.form.get('vehicle_id')
    driver_id  = request.form.get('driver_id')
    route_id   = request.form.get('route_id')
    status     = request.form.get('status')
 
    db = open_database()
    db.execute(
        'INSERT INTO Trip_Logs (log_date, vehicle_id, driver_id, route_id, status) VALUES (?, ?, ?, ?, ?)',
        (log_date, vehicle_id, driver_id, route_id, status)
    )
    db.commit()
    db.close()
 
    return redirect(url_for('manage_trip_logs'))
 
@app.route('/delete_trip_log/<int:id>')
def delete_trip_log(id):
    db = open_database()
    db.execute('DELETE FROM Trip_Logs WHERE log_id = ?', (id,))
    db.commit()
    db.close()
 
    return redirect(url_for('manage_trip_logs'))
 
if __name__ == '__main__':
    app.run(debug=True)