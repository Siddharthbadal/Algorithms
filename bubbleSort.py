def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print(f"The bubble sort: {str(arr)}")
        swap_happened = False
        for num in range(len(arr) -1):
            if arr[num] > arr[num + 1]:
                swap_happened = True
                arr[num], arr[num + 1] = arr[num +1], arr[num]

            

lst = [6,8,1,4,10,7,8,9,2,3,5]
bubble_sort(lst)
