# ISM2411 Lab 11 — Customer Dictionary & Lookup
# Name: Adam Abuhashish
#
# REFLECTION
#
# 1. .get() vs bracket notation:
#    I'd use .get() when a field might honestly be missing, like a customer
#    who never gave us an email, because it just hands back a default and the
#    program keeps running. I'd use brackets when the field has to be there,
#    like a customer's name, because if it's missing I want it to crash loud
#    so I know the data is broken. My rule of thumb is optional means .get(),
#    required means brackets.
#
# 2. Summary dictionary vs Excel:
#    This is basically a pivot table or SUMIF in Excel, where you group rows by
#    region and add up the amounts. The Python version is better for big
#    datasets because it doesn't slow down or freeze with millions of rows and
#    you can rerun the same script on next month's data in one second. In Excel
#    I'd be rebuilding it by hand every time.


# ----- Exercise 1: One customer -----
print("=== Exercise 1: One customer ===")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# ----- Exercise 2: Update and add -----
print("\n=== Exercise 2: Update and add ===")
customer["phone"] = "813-555-0142"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# ----- Exercise 3: Safe lookup -----
print("\n=== Exercise 3: Safe lookup ===")
email = customer.get("email", "no email on file")
print(".get() returned:", email)

try:
    print(customer["email"])
except KeyError as error:
    print("Bracket notation raised KeyError:", error)


# ----- Exercise 4: Iterate -----
print("\n=== Exercise 4: Iterate ===")
for key, value in customer.items():
    print(f"{key}: {value}")

print("--- without .items() ---")
for key in customer:
    print(key)
# Looping over a dict without .items() only gives you the keys.
# .items() gives you each key AND its value together as a pair,
# so you don't have to look the value up again with customer[key].


# ----- Exercise 5: Lookup table -----
print("\n=== Exercise 5: Lookup table ===")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

purchase = 200
rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - rate)
print(f"Tier: {customer['tier']}")
print(f"Discount rate: {rate:.0%}")
print(f"Final price on ${purchase}: ${final_price:.2f}")


# ----- Exercise 6: List of dicts -----
print("\n=== Exercise 6: List of dicts ===")
customers = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 1250.00},
    {"name": "Ben", "tier": "silver", "ytd_spend": 430.00},
    {"name": "Carla", "tier": "bronze", "ytd_spend": 95.00},
    {"name": "Dev", "tier": "gold", "ytd_spend": 780.00},
]

purchase = 300
for c in customers:
    discount = purchase * tier_discounts.get(c["tier"], 0)
    print(f"{c['name']:<6} | tier: {c['tier']:<8} | discount on ${purchase}: ${discount:.2f}")


# ----- Exercise 7: Nested catalog -----
print("\n=== Exercise 7: Nested catalog ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} only has {info['stock']} left")


# ----- Exercise 8: Sales by region -----
print("\n=== Exercise 8: Sales by region ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")
