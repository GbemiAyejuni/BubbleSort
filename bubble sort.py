sort_list = []  # empty list to store numbers to be sorted
list_size = int(input("Enter the size of list: "))  # variable to store size of list indicated by the user

for i in range(0, list_size):
    number = int(input("Enter digit: "))
    sort_list.append(number)  # adds each number the user gives to sort_list

print("Unsorted List: ", sort_list)

for i in range(0, len(sort_list) - 1):
    swapped = False  # swapped initialized as false
    for j in range(0, len(sort_list) - 1):
        if sort_list[j] > sort_list[j + 1]:
            sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
            swapped = True  # sets swapped to true if swapping of numbers occurs in the iteration
    if not swapped:
        break

print("Sorted List: ", sort_list)

input('Press Enter to Exit...')
