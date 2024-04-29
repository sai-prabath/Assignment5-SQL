class Customer:
    customer_id_counter = 0
    def __init__(self, customer_name, email, phone_number):
        Customer.customer_id_counter += 1
        self.customer_id = Customer.customer_id_counter
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def display_customer_details(self):
        print("Customer Details:")
        print(f"Name: {self.customer_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
