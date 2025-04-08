import pyodbc
from connect_SQL import conn
from DTO.Products import Products

def add_supplier(supplier):
    cursor = conn.cursor()

    try:
        # Insert the supplier first
        cursor.execute("""
            INSERT INTO supplier (company_name, phone_num, worker_name)
            VALUES (?, ?, ?)
        """, supplier.company_name, supplier.phone_num, supplier.worker_name)

        # Insert the products
        for product in supplier.products:
            cursor.execute("""
                IF NOT EXISTS (SELECT 1 FROM Products WHERE product_name = ?)
                BEGIN
                    INSERT INTO Products (product_name, price_per_item, minimum_for_sale)
                    VALUES (?, ?, ?)
                END
            """, product.product_name, product.price_per_item, product.minimum_for_sale)

            cursor.execute("""
                INSERT INTO supplier_product (company_name, product_name)
                VALUES (?, ?)
            """, supplier.company_name, product.product_name)

        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print("Error inserting supplier:", e)
        return False
    finally:
        cursor.close()


def get_all_suppliers_names():
    cursor = conn.cursor()
    cursor.execute("SELECT company_name FROM supplier")
    rows = cursor.fetchall()
    return [row[0] for row in rows]
