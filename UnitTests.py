# Bradley Begnoche
# 3/26/24
# This program uses a list and a for loop to print out customer id, invoice code, and the cost of their order

class Invoice:
   
    def __init__(self, invoice_id, customer_id):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.ditems = {}

    def add_item(self, item, price):
        
        self.ditems[item] = price

    def print_invoice(self):
       
        print(f"CUSTOMER: {self.customer_id}\nINVOICE: {self.invoice_id}")
        for idx, (item, price) in enumerate(sorted(self.ditems.items(), key=lambda x: x[1])):
            print(f"{item}: {price:.2f}")

    def __str__(self):
        
        return f"Invoice ID: {self.invoice_id}, Customer ID: {self.customer_id}"


def main():
    invoices_list = [
        {"invoice_id": "A554GFT-117", "customer_id": "98676867", "items": [("ipad", 499.99), ("mouse", 29.97), ("monitor", 229.08)]},
        {"invoice_id": "J244GFT-283", "customer_id": "77594872", "items": [("router", 267.78), ("hdmi-cable", 24.77)]},
        {"invoice_id": "R943RXC-476", "customer_id": "54092341", "items": [("laptop", 1399.54), ("warranty", 199.94), ("snickers", 2.49)]},
        {"invoice_id": "J712WQR-888", "customer_id": "43908134", "items": [("amplifier", 749.00), ("speaker-cable", 42.75)]}
    ]

   
    for invoice_data in invoices_list:
        invoice = Invoice(invoice_data["invoice_id"], invoice_data["customer_id"])
        
       
        for item, price in invoice_data["items"]:
            invoice.add_item(item, price)
        
        invoice.print_invoice()
        print()


if __name__ == "__main__":
    main()