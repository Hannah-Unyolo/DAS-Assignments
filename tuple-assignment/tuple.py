inventory = {}

def add_product(category, product_id, name, price, quantity):
    key = (category, product_id)
    inventory[key] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

def display_product(category, product_id):
    key = (category, product_id)
    product = inventory.get(key)
    if product:
        print(f"Product Details for {key}:")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
    else:
        print(f"No product found for {key}.")

def update_quantity(category, product_id, new_quantity):
    key = (category, product_id)
    if key in inventory:
        inventory[key]['quantity'] = new_quantity
        print(f"Updated quantity for {key} to {new_quantity}.")
    else:
        print(f"No product found for {key} to update.")

if __name__ == "__main__":
    add_product("Electronics", 101, "Smartphone", 699.99, 50)
    add_product("Electronics", 102, "Laptop", 999.99, 30)
    add_product("Home Appliances", 201, "Vacuum Cleaner", 199.99, 20)
    display_product("Electronics", 101)
    display_product("Home Appliances", 201)
    update_quantity("Electronics", 101, 45)
    display_product("Electronics", 101)