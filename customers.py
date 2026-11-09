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
