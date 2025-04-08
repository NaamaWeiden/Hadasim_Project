from DTO.Products import Products
from connect_SQL import conn

def add_product(product: Products):
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO Products (product_name, price_per_item, minimum_for_sale)
        VALUES (?, ?, ?)
        """
        cursor.execute(query, product.product_name, product.price_per_item, product.minimum_for_sale)
        conn.commit()
        return True
    except Exception as e:
        print("Error adding product:", e)
        return False


def get_products_by_supplier(company_name):
    cursor = conn.cursor()
    print("Received company_name:", company_name)
    query = """
        SELECT p.product_name
        FROM Products p
        JOIN supplier_product sp ON p.product_name = sp.product_name
        WHERE sp.company_name = ?
    """
    cursor.execute(query, (company_name,))
    rows = cursor.fetchall()
    print("Products found:", rows)  # 🔍 חשוב!
    return [row[0] for row in rows]

def get_minimum_for_sale(product_name):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT minimum_for_sale
        FROM Products
        WHERE product_name = ?
    """, (product_name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        raise Exception("המוצר לא נמצא")


def calculate_total_payment(product_name, quantity):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT price_per_item
        FROM Products
        WHERE product_name = ?
    """, (product_name,))
    row = cursor.fetchone()
    if not row:
        raise Exception("המוצר לא נמצא")

    price_per_item = row[0]
    total_payment = price_per_item * quantity
    return total_payment
