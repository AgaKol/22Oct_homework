# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]


def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]


def add_or_remove_cash(cc_pet_shop, cash):
    cc_pet_shop["admin"]["total_cash"] = cc_pet_shop["admin"]["total_cash"]+cash
