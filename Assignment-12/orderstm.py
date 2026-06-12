from abc import ABC, abstractmethod


# =====================================
# ORDER CLASSES
# =====================================

class Order(ABC):

    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    @abstractmethod
    def get_total(self):
        pass


class RegularOrder(Order):

    def get_total(self):
        return self.amount


class DiscountedOrder(Order):

    def __init__(self, order_id, customer_name, amount, discount):
        super().__init__(order_id, customer_name, amount)
        self.discount = discount

    def get_total(self):
        return self.amount - self.discount


class PriorityOrder(Order):

    def __init__(self, order_id, customer_name, amount, priority_fee):
        super().__init__(order_id, customer_name, amount)
        self.priority_fee = priority_fee

    def get_total(self):
        return self.amount + self.priority_fee


# =====================================
# PAYMENT METHODS
# =====================================

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Payment of Rs.{amount} done using Credit Card")


class UPIPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Payment of Rs.{amount} done using UPI")


class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Payment of Rs.{amount} done using Wallet")


# =====================================
# NOTIFICATION METHODS
# =====================================

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(f"Email Notification: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS Notification: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Push Notification: {message}")


# =====================================
# STORAGE METHODS
# =====================================

class Storage(ABC):

    @abstractmethod
    def save(self, order):
        pass


class DatabaseStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved in Database")


class FileStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved in File")


# =====================================
# ORDER SERVICE
# =====================================

class OrderService:

    def __init__(self, payment_method, notification_method, storage_method):
        self.payment_method = payment_method
        self.notification_method = notification_method
        self.storage_method = storage_method

    def process_order(self, order):

        total_amount = order.get_total()

        print("\n===== ORDER DETAILS =====")
        print("Order ID :", order.order_id)
        print("Customer :", order.customer_name)
        print("Total Amount : Rs.", total_amount)

        # Payment Processing
        self.payment_method.pay(total_amount)

        # Notification
        self.notification_method.send(
            f"Order {order.order_id} processed successfully"
        )

        # Save Order
        self.storage_method.save(order)

        print("=========================")


# =====================================
# MAIN PROGRAM
# =====================================

if __name__ == "__main__":

    # Creating Orders
    order1 = RegularOrder(101, "Rahul", 5000)

    order2 = DiscountedOrder(102, "Anjali", 4000, 500)

    order3 = PriorityOrder(103, "Rohit", 6000, 300)

    # Creating Services
    service1 = OrderService(
        CreditCardPayment(),
        EmailNotification(),
        DatabaseStorage()
    )

    service2 = OrderService(
        UPIPayment(),
        SMSNotification(),
        FileStorage()
    )

    service3 = OrderService(
        WalletPayment(),
        PushNotification(),
        DatabaseStorage()
    )

    # Processing Orders
    service1.process_order(order1)

    service2.process_order(order2)

    service3.process_order(order3)