# Flower Shop intro
print(" . . . . . . . . . . . . . . . . . . .\n*. Welcome to the Flawless Flower Shop! .*\n . . . . . . . . . . . . . . . . . . . \nWe create custom bouquets for every occasion!\n")

# In Stock
flowers = ["rose", "sunflower", "daisy", "poppy", "tulip"]

# pluarl
plural_to_singular = {
    "roses": "rose",
    "sunflowers": "sunflower",
    "daisies": "daisy",
    "poppies": "poppy",
    "tulips": "tulip"
}

def check_order(order, flower_list):
    flower_count = {flower: 0 for flower in flower_list}
    words = order.lower().split()
    i = 0

 
    # singular/plural
    i = 0
    while i < len(words):
        flower_found = False
        if words[i] in flower_list:
            if flower_count[words[i]] == 0:
                flower_count[words[i]] += 1
            flower_found = True
        elif words[i] in plural_to_singular:
            singular_form = plural_to_singular[words[i]]
            if flower_count[singular_form] == 0:
                flower_count[singular_form] += 3
            flower_found = True
        if not flower_found:
            i += 1  
        else:
            i += 1  

       # numbers and specific count
    while i < len(words):
        if words[i].isdigit():
            count = int(words[i])
            if i + 1 < len(words) and words[i + 1] in flower_list:
                flower_count[words[i + 1]] += count
                i += 2  
            else:
                i += 1  
        else:
            i += 1  

    return {f: count for f, count in flower_count.items() if count > 0}

while True:
    # order
    order = input("\n\nWhat would you like to order today? (Type 'exit' to leave the shop)\n")
    if order.lower() == 'exit':
        print("\nThank you for visiting the Flawless Flower Shop! Have a great day!")
        break
    
    flower_counts = check_order(order, flowers)
    
    if flower_counts:
        print("\nYou have ordered the following flowers:")
        for flower, count in flower_counts.items():
            print(f"- {count} {flower.capitalize()}(s)")
    else:
        print("\nSorry, we do not have those flowers in stock!")
