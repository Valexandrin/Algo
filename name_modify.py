import re

def modify_name(origin_name: str):
    res = re.split('\W+', origin_name)   
    print(res) 
    return '_'.join(res)+'.py'

def main():
    original_name = input('Enter original name: ')

    print('Python file name: ', modify_name(original_name))

if __name__ == '__main__':
    main()
