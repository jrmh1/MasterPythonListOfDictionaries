
products = [
    {"name": "Laptop", "category": "Electronics", "price": 30000.00, "stock": 50, "supplier_email": "supplier1@gmail.com"},
    {"name": "Desk Chair", "category": "Furniture", "price": 3000.00, "stock": 200, "supplier_email": "supplier2@gmail.com"},
    {"name": "Smartwatch", "category": "Electronics", "price": 2500.00, "stock": 150, "supplier_email": "supplier3@gmail.com"},
    {"name": "Notebook", "category": "Stationery", "price": 100.00, "stock": 0, "supplier_email": "supplier4@gmail.com"},
    {"name": "Running Shoes", "category": "Apparel", "price": 4500.00, "stock": 100, "supplier_email": "supplier5@gmail.com"},
]

# Print product data
print("Product Data:")
for product in products:
    print(f"Product: {product['name']}, Category: {product['category']}, Price: ₱{product['price']}, Stock: {product['stock']}, Supplier Email: {product['supplier_email']}")
