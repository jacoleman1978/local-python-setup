def hello():
    print("Hello user!")

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(lunch_list):
    if lunch_list == []:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_list[0]}")

        for index in range(1, len(lunch_list)):
            print(f"Next I eat {lunch_list[index]}")

hello()

print(pack('socks', 'underwear', 'shirts'))

print("***Empty list:")
eat_lunch([])
print("***One item in list")
eat_lunch(['carrots'])
print("***More than one item in list")
eat_lunch(['carrots', 'apple slices', 'string cheese', 'deli turkey'])