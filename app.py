from flask import Flask, render_template, request, jsonify
from vehicle_inventory_project import VehicleInventory

app = Flask(__name__)
inventory = VehicleInventory()

# Add some sample data
inventory.add_vehicle("V1001", "F-150", 35000)
inventory.add_vehicle("V1002", "Mustang", 45000)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify(inventory.inventory)

@app.route('/api/vehicles', methods=['POST'])
def add_vehicle():
    data = request.json
    inventory.add_vehicle(data['id'], data['model'], data['cost'], data.get('status', 'in_production'))
    return jsonify({"message": "Vehicle added successfully"})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)