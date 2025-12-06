#!/usr/bin/env python3

# Author
# Date: 12/6/25
# Version 1.1

class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize the cash register with an optional discount.
        Sets total to 0, items to an empty list, and prepares a list
        to track the value of each transaction.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Return the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Set the discount percentage.
        Ensures the value is an integer between 0 and 100.
        """
        if not isinstance(value, int):
            raise ValueError("Discount must be an integer")
        if value < 0 or value > 100:
            raise ValueError("Discount must be between 0 and 100")

        self._discount = value

    def add_item(self, item, price, quantity=1):
        """
        Add an item to the register.
        Each item's name is stored once per quantity.
        The transaction's total value is added to the running total.
        """
        for _ in range(quantity):
            self.items.append(item)

        transaction_total = price * quantity
        self.total += transaction_total
        self.previous_transactions.append(transaction_total)

    def apply_discount(self):
        """
        Apply the set discount to the total price.
        If no discount is set, an informational message is printed.
        Otherwise, the total is reduced and a success message is shown.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discounted_total = self.total * (100 - self.discount) / 100
        self.total = int(discounted_total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        """
        Remove the last recorded transaction from the total.
        If the transaction represented all current items,
        the items list is cleared.
        """
        if not self.previous_transactions:
            return

        last_total = self.previous_transactions.pop()
        self.total -= last_total

        # If removing the last transaction returns total to zero,
        # all items are removed for consistency.
        if abs(self.total) < 0.0001:
            self.items = []
