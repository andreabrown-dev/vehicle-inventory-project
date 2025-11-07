# vehicle_inventory.py
class VehicleInventory:
    def __init__(self):
        self.inventory = []
    
    def add_vehicle(self, vehicle_id, model, cost, status="in_production"):
        vehicle = {
            "id": vehicle_id,
            "model": model,
            "cost": cost,
            "status": status
        }
        self.inventory.append(vehicle)
        print("Vehicle added: " + model)
    
    def find_vehicle(self, vehicle_id):
        for vehicle in self.inventory:
            if vehicle["id"] == vehicle_id:
                return vehicle
        return None
    
    def update_status(self, vehicle_id, new_status):
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle:
            vehicle["status"] = new_status
            print("Status updated for vehicle " + vehicle_id)
        else:
            print("Vehicle not found")
    
    def get_total_cost(self):
        total = 0
        for vehicle in self.inventory:
            total += vehicle["cost"]
        return total
    
    def show_inventory(self):
        print("\nCurrent Inventory:")
        for vehicle in self.inventory:
            print("ID: " + vehicle["id"] + ", Model: " + vehicle["model"] + ", Cost: $" + str(vehicle["cost"]) + ", Status: " + vehicle["status"])

# Example usage
if __name__ == "__main__":
    ford_inventory = VehicleInventory()
    
    # Add vehicles
    ford_inventory.add_vehicle("V1001", "F-150", 35000)
    ford_inventory.add_vehicle("V1002", "Mustang", 45000)
    ford_inventory.add_vehicle("V1003", "Explorer", 40000)
    
    # Show inventory
    ford_inventory.show_inventory()
    
    # Update status
    ford_inventory.update_status("V1001", "completed")
    
    # Show total cost
    total = ford_inventory.get_total_cost()
    print("Total inventory value: $" + str(total))