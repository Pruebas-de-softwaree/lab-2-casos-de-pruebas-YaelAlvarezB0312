class OnlinePurchase:
    def __init__(self):
        self.valid_coupons = {"DISCOUNT10": 0.15, "DISCOUNT30": 0.30}
        
        self.items = {
            "Laptop": 1000,
            "Headphones": 100,
            "Mouse": 50,
            "Keyboard": 80,
            "Monitor": 300,
            "Printer": 200,
            "Webcam": 70,
            "USB Drive": 30,
            "Smartphone": 800,
            "Tablet": 400
        }

    def validate_quantity(self, quantity):
        if not isinstance(quantity, int):
            return False
        if quantity <= 0:
            return False
        return True

    def validate_coupon(self, code):
        return code in self.valid_coupons or code == ""

    def validate_address(self, address):
        return isinstance(address, str) and len(address.strip()) > 5

    def process_purchase(self, cart, coupon, address):
        print("Processing purchase...")

        for item, quantity in cart.items():
            if item not in self.items:
                return f" Error: '{item}' is not a valid item."
            if not self.validate_quantity(quantity):
                return f" Error: Quantity for '{item}' must be an integer greater than 0."

        if not self.validate_coupon(coupon):
            return " Error: The entered coupon code is not valid."

        total = sum(self.items[item] * quantity for item, quantity in cart.items())
        discount = self.valid_coupons.get(coupon, 0)
        total_with_discount = total * (1 - discount)

        cart_summary = "\n".join([f"{item}: {quantity} x ${self.items[item]}" for item, quantity in cart.items()])

        return (f"Purchase completed.\n"
                f"Items:\n{cart_summary}\n"
                f"Coupon: {coupon or 'None'}\n"
                f"Shipping Address: {address}\n"
                f"Total to pay: ${total_with_discount:.2f}")


if __name__ == "__main__":
    purchase = OnlinePurchase()

    cart = {
        "Mouse": 0,          
        "Keyboard": -2, 
        "Webcam": 1.5        
    }
    coupon = ""
    address = "Calle Falsa 123"
    purchase_1 = purchase.process_purchase(cart, coupon, address)
    print(purchase_1)
    print("END")
