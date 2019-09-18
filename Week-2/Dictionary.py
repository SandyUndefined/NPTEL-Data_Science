# Creating Dictionary
Fuel_type = {"Petrol": 1, "Diesel": 2, "CNG": 3}
print(f'Creating a Dictionary : ', Fuel_type)


# Accessing Dictionary
# 1. To know the value of the key
print(f'To know the value of the key : ', Fuel_type["CNG"])
# 2. To access the keys
print(f'To access the keys : ',Fuel_type.keys())
# 3. To access the values
print(f'To access the values : ', Fuel_type.values())
# 4. To access both keys and values
print(f'To access both keys and values : ', Fuel_type.items())


# Modifying Dictionary
# 1. Adding new key value pair
Fuel_type["Electric"] = 4
print(f'Adding new key value pair : ',Fuel_type )
# 2. Adding new key value pair using update()
Fuel_type.update({"Coal": 5})
print(f'Adding new key value pair using update() : ', Fuel_type)
# 3. Modifying existing key
Fuel_type["Diesel"] = 5
print(f'Modifying existing key : ', Fuel_type)
# 4. Delete key value pair
del Fuel_type["Diesel"]
print(f'Delete key value pair', Fuel_type)
# 5. Clear : removes all the key value pair
Fuel_type.clear()
print(f'Clear : ', Fuel_type)