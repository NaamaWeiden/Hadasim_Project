class supplier:
    def __init__(self, company_name, phone_num, worker_name, products=None):
        self.company_name = company_name
        self.phone_num = phone_num
        self.worker_name = worker_name
        self.products = products if products else []
