def search_number(arr, number):
    low = 0 
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == number:
            print("Item found at the index:", mid)
            return mid  # 2. RETURN immediately to stop the infinite loop!
        elif guess > number:
            high = mid - 1
        else:
            low = mid + 1
            
    print("Number not found in the array.")
    return -1


def create_array():
    l1 = []
    choice = int(input("Enter the size of array: "))
    for i in range(choice):
        element = int(input("Enter the element: "))
        l1.append(element)
    l1.sort()
    print("Sorted array:", l1)
    
    num = int(input("Enter the number which you want to search: "))
    search_number(l1, num)

create_array()