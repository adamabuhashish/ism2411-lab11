# ISM2411 Lab 11 — Customer Dictionary & Lookup
# Name: Adam Abuhashish


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
