# OOP Cash Register Lab

The CashRegister class models a simple point-of-sale system.
It supports adding items, applying percentage-based discounts, tracking individual transactions, and voiding the most recent purchase.
This class is designed to provide clear, easy-to-use methods for managing totals and item lists in a retail-style checkout environment.

### Features
✔ Initialize With Optional Discount
- You can create a register with or without a discount:

register = CashRegister()              # No discount
discount_register = CashRegister(20)   # 20% discount

✔ Track Items
- Items are stored by name in a simple list.
- Multiple quantities appear multiple times:

register.add_item("apple", 0.99, 3)
print(register.items)
# ['apple', 'apple', 'apple']

✔ Maintain a Running Total
- Every time an item is added, the price is added to the total:

register.total  # Updates automatically

✔ Apply Percentage Discounts
- If a discount percentage is set, the total can be reduced:

discount_register.apply_discount()
# After the discount, the total comes to $800.
- If the discount is 0%, the method prints: "There is no discount to apply."

✔ Void the Last Transaction
- The register stores the value of each transaction.
- Voiding removes the most recent transaction and updates the total accordingly:

register.void_last_transaction()

- If the last transaction was the only one, items reset as well.

### Methods Overview
#### __init__(discount=0)

-Initializes the register with:
-- discount (0–100)
-- total set to 0
-- items as an empty list
-- previous_transactions to track transaction values

#### add_item(item, price, quantity=1)
- Adds the item name to the list once per quantity and increases the total.

apply_discount()
- Applies the percentage discount to the total.
- Prints the updated total.
- Prints a message if no discount is available.

void_last_transaction()
- Removes the most recently added transaction and updates the total.

### Example Usage
from cash_register import CashRegister

register = CashRegister(10)

register.add_item("bread", 3.50)
register.add_item("milk", 4.00, 2)

print(register.total)
# 11.50

register.apply_discount()
# After the discount, the total comes to $10.

register.void_last_transaction()
print(register.total)
# 6.0