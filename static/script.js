// Load inventory when page loads
document.addEventListener('DOMContentLoaded', function() {
    loadInventory();
});

// Load and display inventory
async function loadInventory() {
    try {
        const response = await fetch('/api/vehicles');
        const vehicles = await response.json();
        displayInventory(vehicles);
    } catch (error) {
        console.error('Error loading inventory:', error);
        document.getElementById('inventoryList').innerHTML = '<p>Error loading inventory</p>';
    }
}

// Display inventory in the page
function displayInventory(vehicles) {
    const inventoryList = document.getElementById('inventoryList');
    
    if (vehicles.length === 0) {
        inventoryList.innerHTML = '<p>No vehicles in inventory</p>';
        document.getElementById('totalValue').textContent = '0';
        return;
    }

    let totalValue = 0;
    let inventoryHTML = '';

    vehicles.forEach(vehicle => {
        totalValue += vehicle.cost;
        
        inventoryHTML += `
            <div class="vehicle-card">
                <div class="vehicle-info">
                    <div class="vehicle-id">${vehicle.id}</div>
                    <div class="vehicle-model">${vehicle.model}</div>
                    <div class="vehicle-cost">$${vehicle.cost.toLocaleString()}</div>
                </div>
                <div class="vehicle-status status-${vehicle.status}">
                    ${vehicle.status.replace('_', ' ').toUpperCase()}
                </div>
            </div>
        `;
    });

    inventoryList.innerHTML = inventoryHTML;
    document.getElementById('totalValue').textContent = totalValue.toLocaleString();
}

// Handle form submission
document.getElementById('addVehicleForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = {
        id: document.getElementById('vehicleId').value,
        model: document.getElementById('vehicleModel').value,
        cost: parseInt(document.getElementById('vehicleCost').value),
        status: document.getElementById('vehicleStatus').value
    };

    try {
        const response = await fetch('/api/vehicles', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            // Clear form
            document.getElementById('addVehicleForm').reset();
            // Reload inventory
            loadInventory();
            // Show success message (you can add a proper notification later)
            alert('Vehicle added successfully!');
        }
    } catch (error) {
        console.error('Error adding vehicle:', error);
        alert('Error adding vehicle');
    }
});