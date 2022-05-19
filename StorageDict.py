def store(name_to_store, info_to_store):
    storage[name_to_store] = info_to_store


storage = {}
# For testing purposes
while True:
    store(input("Name: "), input("Info: "))
    print(f"\n{storage}")
