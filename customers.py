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
