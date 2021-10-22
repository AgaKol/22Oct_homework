# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]


def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]


def add_or_remove_cash(cc_pet_shop, cash):
    cc_pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]


def increase_pets_sold(cc_pet_shop, increase):
    cc_pet_shop["admin"]["pets_sold"] += increase


def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])


def get_pets_by_breed(cc_pet_shop, breed):
    breeds = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed:
            breeds.append(pet["name"])
    return breeds


def find_pet_by_name(cc_pet_shop, name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(cc_pet_shop, name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
            cc_pet_shop["pets"].remove(pet)


def add_pet_to_stock(cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)


def get_customer_cash(customers):
    for customer in customers:
        return customers["cash"]


def remove_customer_cash(customer, cash):
    customer["cash"] -= cash


def get_customer_pet_count(customer):
    return int(len(customer["pets"]))


def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)


def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(cc_pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet) == True:
        customer["pets"].append(pet)
        cc_pet_shop["admin"]["pets_sold"] += 1
        customer["cash"] -= pet["price"]
        cc_pet_shop["admin"]["total_cash"] += pet["price"]
        cc_pet_shop["pets"].remove(pet)
