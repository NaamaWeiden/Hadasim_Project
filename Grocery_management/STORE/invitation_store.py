from DTO.invitation import invitation
from connect_SQL import conn

def add_invitation(invitation: invitation):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT price_per_unit, min_quantity
        FROM products
        WHERE product_name = ?
    """, invitation.product_name)

    row = cursor.fetchone()
    if not row:
        raise Exception("המוצר לא נמצא")

    price_per_unit, min_quantity = row

    if invitation.quantity < min_quantity:
        raise Exception("כמות ההזמנה נמוכה מהמינימום המותר")

    total_payment = price_per_unit * invitation.quantity
    cursor.execute("""
        INSERT INTO invitation (invitation_id, product_name, company_name, quantity, total_payment)
        VALUES (?, ?, ?, ?, ?)
    """, (invitation.invitation_id, invitation.product_name, invitation.company_name, invitation.quantity, total_payment))
    conn.commit()



def get_invitations_by_supplier(company_name):
    query = """
    SELECT * FROM invitation
    WHERE company_name = ? AND (status IS NULL OR status = '')
    """
    cursor = conn.cursor()
    cursor.execute(query, company_name)
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

def update_invitation_status(invitation_id, new_status):
    query = """
    UPDATE invitation
    SET status = ?
    WHERE invitation_id = ?
    """
    cursor = conn.cursor()
    cursor.execute(query, (new_status, invitation_id))
    conn.commit()
    return cursor.rowcount > 0  # True if update succeeded


def get_all_invitations():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invitation")
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results


def get_in_process_invitations():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invitation WHERE status = 'בתהליך'")
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

def update_invitation_status_to_completed(invitation_id):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE invitation
        SET status = 'הושלמה'
        WHERE invitation_id = ?
    """, (invitation_id,))
    conn.commit()
    return cursor.rowcount > 0

def get_completed_invitations_for_supplier(company_name):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM invitation
        WHERE company_name = ? AND status = 'הושלמה'
    """, (company_name,))
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

