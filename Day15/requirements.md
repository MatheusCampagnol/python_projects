# Coffee Machine Program Requirements

## 1. Prompt User

Prompt the user by asking:

```text
What would you like? (espresso/latte/cappuccino):
```

### Requirements

* Check the user's input to decide what to do next.
* The prompt should appear every time an action has completed.
* After dispensing a drink, the prompt should appear again to serve the next customer.

---

## 2. Turn Off the Coffee Machine

If the user enters:

```text
off
```

### Requirements

* This is a secret command intended for maintainers.
* The program should terminate immediately.

---

## 3. Print Report

If the user enters:

```text
report
```

Generate a report showing the current resources.

### Example

```text
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

---

## 4. Check Resources

When the user selects a drink:

1. Check whether sufficient resources are available.
2. If a resource is insufficient, stop the process.

### Example

If a Latte requires:

```text
Water: 200ml
```

But only:

```text
Water: 100ml
```

Remain in the machine, print:

```text
Sorry there is not enough water.
```

The same logic applies to milk and coffee.

---

## 5. Process Coins

If enough resources exist:

1. Prompt the user to insert coins.
2. Use the following values:

| Coin    | Value |
| ------- | ----- |
| Quarter | $0.25 |
| Dime    | $0.10 |
| Nickel  | $0.05 |
| Penny   | $0.01 |

### Example Calculation

```text
1 quarter
2 dimes
1 nickel
2 pennies
```

Calculation:

```text
0.25 + (0.10 × 2) + 0.05 + (0.01 × 2)
```

Result:

```text
$0.52
```

---

## 6. Check Transaction

### Not Enough Money

If the inserted amount is less than the drink cost:

Example:

```text
Latte cost = $2.50
Inserted = $0.52
```

Print:

```text
Sorry that's not enough money. Money refunded.
```

### Successful Payment

If enough money was inserted:

* Add the drink price to the machine's profit.
* The next report should reflect the updated amount.

Example:

```text
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

### Give Change

If the customer inserts more money than necessary:

Example:

```text
Here is $2.45 dollars in change.
```

Change should be rounded to **2 decimal places**.

---

## 7. Make Coffee

If:

* Resources are sufficient, and
* Payment is successful,

Then:

1. Deduct the required ingredients from the machine resources.

### Example

Before purchasing a Latte:

```text
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
```

After purchasing a Latte:

```text
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

### Final Message

After the ingredients are deducted, print:

```text
Here is your latte. Enjoy!
```

Replace `latte` with the drink selected by the user.
