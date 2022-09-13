from search import create_array, binary_search
from typing import Optional


def value_request(value: str) -> Optional[int]:
    input_object = input(f'Enter {value}: ')
    valid_input = input_validation(input_object)
    if valid_input < 0:
        return value_request(value)
    return valid_input


def input_validation(input_object: str) -> bool:
    if not input_object:
        print('Try to input anything...')
        return -1
                
    try:    
        integer = int(input_object)        
    except:
        print('Input should be an integer')
        return -1

    if integer < 0:
        print('Input can not be negative')
        return integer
    
    return integer


def check_within(number, array):
    if number not in array:
        print('The number is out of the array. Try again!')
        return False
    return True


def main():
    array_size = value_request(value='an array size')    
    number = value_request(value='a number')
    
    array = create_array(array_size)    
    if not check_within(number, array):
        return main()
    
    print(f'answer: {binary_search(array, number)}')    


if __name__ == '__main__':
    main()
