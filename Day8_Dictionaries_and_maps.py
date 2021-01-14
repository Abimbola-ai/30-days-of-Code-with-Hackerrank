# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {name: numbers for name,numbers in name_numbers}
#print(phone_book.keys())

while True:
    try:
        name = input()

        if name in phone_book.keys():
            print(name + "=" + phone_book[name])
        else:
            print("Not found")
    except: 
        break
