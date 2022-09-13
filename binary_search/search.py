def create_array(arr_size):
    arr = []
    for i in range(arr_size+1):
        arr.append(i)
    return arr


def process_info(cycle, value):
    print(f'cycle-{cycle}, value-{value}')


def binary_search(arr, number, cycle=1):
    mid = len(arr)//2
    if len(arr) == 1:
        process_info(cycle, arr[mid])
        return arr[0]
    if arr[mid] == number:
        process_info(cycle, arr[mid])
        return arr[mid]
    else:
        process_info(cycle, arr[mid])
        cycle += 1        
        return binary_search(arr[0: mid], number, cycle) if arr[mid] > number else binary_search(arr[mid:], number, cycle)        


if __name__ == '__main__':
    arr_size = 1000000
    number = 0
    
    array = create_array(arr_size)    
    print(f'answer: {binary_search(array, number)}')