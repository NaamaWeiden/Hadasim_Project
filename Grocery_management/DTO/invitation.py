class invitation:
    def __init__(self, invitation_id, product_name, company_name, quantity, total_payment, status=""):
        self.invitation_id = invitation_id
        self.product_name = product_name
        self.company_name = company_name
        self.quantity = quantity
        self.total_payment = total_payment
        self.status = status
