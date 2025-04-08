import connect_SQL

def add_supplier_product(supplier_product):
    conn = connect_SQL.connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO supplier_products (company_name, product_name)
            VALUES (?, ?)
        """, (supplier_product.company_name, supplier_product.product_name))
        conn.commit()
        return True
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        cursor.close()
