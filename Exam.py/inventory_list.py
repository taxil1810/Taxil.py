print("Welcome to Inventory List Analyzer! ")

items = []
categories = []

while True:

    item = input("Enter item name : ")
    category = input("Enter category : ")
    quantity = int(input("Enter quantity : "))

    items.append({
        "item": item,
        "category": category,
        "quantity": quantity,
    })
    
    choice = input("\nDo you want to add more items? (y/n) : ")
    if choice.lower() == 'y': 
        continue

    elif choice == 'n':
        break

    else:
        print("Invalid choice")    
    

print("\n========== INVENTORY SUMMARY ==========\n")  
Total_items = len(items)
Total_quantity = sum(item['quantity'] for item in items)
Average = Total_quantity/Total_items
Stocked = max(items , key= lambda x: x['quantity'])
stocked = min(items , key= lambda x: x['quantity'])

print("\nTotal Different Items :" , Total_items)
print("Total Quantity in stock :" , Total_quantity)
print("Average Quantity per Itrm :" , Average)
print(f"Most Stocked Item : , {Stocked['item']} ({Stocked['quantity']}units)")
print(f"Least Stocked Item : , {stocked['item']} ({stocked['quantity']}units)")

print("\n=======================================")
categories = sorted((set(item['category'] for item in items)))
print(f"unique categories are in inventory:  {set(categories)}")


print("\n========================================\n")

print("Items Sorted by Quantity (High to Low):")
sorted_items = sorted(items, key=lambda x: x['quantity'], reverse=True)
for i, item in enumerate(items, start=1):
    print(f"{i}. {item['item']} - {item['quantity']} units")

print("\n========================================\n")

print("Categories in Alphabetical Order:")
for i, cat in enumerate(categories, start=1):
    print(f"{i}. {cat}")


print("\n ========== END OF REPORT =========== \n")