import flowerdraw

flowerdraw.start()

# Flower Shop intro
print("\n. . . . . . . . . . . . . . . . . . .\n*. Welcome to the Flawless Flower Shop! .*\n . . . . . . . . . . . . . . . . . . . \n\nWe create custom bouquets for every occasion!")

# In Stock
flowers = ["marigold", "sunflower", "daisy", "lotus", "tulip"]

# plural to singular mapping
plural_to_singular = {
    "marigolds": "marigold",
    "sunflowers": "sunflower",
    "daisies": "daisy",
    "lotuses": "lotus",
    "tulips": "tulip"
}

def check_order(order, flower_list):
    flower_count = {flower: 0 for flower in flower_list}
    words = order.lower().split()
    i = 0

    # Process numbers and specific counts
    while i < len(words):
        if words[i].isdigit():
            count = int(words[i])
            if i + 1 < len(words):
                flower = words[i + 1]
                # Check if the next word is a plural form
                if flower in plural_to_singular:
                    flower = plural_to_singular[flower]
                # Check if the flower is in stock and update the count
                if flower in flower_list:
                    flower_count[flower] += count
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1

    # Process singular/plural terms if no number
    i = 0
    while i < len(words):
        flower_found = False
        if words[i] in flower_list:
            # If the flower has been counted already with a number, skip
            if flower_count[words[i]] == 0:
                flower_count[words[i]] += 1
            flower_found = True
        elif words[i] in plural_to_singular:
            singular_form = plural_to_singular[words[i]]
            # Only add if no count was assigned earlier
            if flower_count[singular_form] == 0:
                flower_count[singular_form] += 3
            flower_found = True
        if not flower_found:
            i += 1
        else:
            i += 1

    return {f: count for f, count in flower_count.items() if count > 0}

while True:
    # order
    order = input(". . . . . . . . . . . . . . . . .  . . .. . . . . . .\n\nWhat would you like to order today? (Type 'exit' to leave the shop)\n")
    if order.lower() == 'exit':
        print("\nThank you for visiting the Flawless Flower Shop! Have a great day!")
        break
    
    # Check if the order contains "rose" or "roses"
    if "rose" in order.lower() or "roses" in order.lower():
        print("Our roses are not in stock due to high demand.")
    
    flower_count = check_order(order, flowers)
    
    if flower_count:
        print("\nYou have ordered the following flowers:")
        for flower, count in flower_count.items():
            print(f"- {count} {flower.capitalize()}(s)")
        
        # Call the draw function
        flowerdraw.draw_flowers(flower_count)
    
    else:
        print("\nSorry, we do not have those flowers in stock!")
