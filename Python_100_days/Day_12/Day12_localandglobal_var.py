enemies = 1


def increase_enemies():
    enemies = 2
    print(f"eneimes inside function: {enemies}")
    
    
increase_enemies()
print(f"enemies outside function: {enemies}")



# Local Scope
def drink_potion():
    potion_strength = 2
    