stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

 
def displayInventory(inventory):
    count = 0
    for k, v in stuff.items(): 
        print(v, k)
    for value in stuff.values():
        count += value
    print(f'Total number of items: {count}')


if __name__ == "__main__":
    displayInventory(stuff)
