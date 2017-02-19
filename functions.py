def call_numbers():
    for number in range(0,10):
        print(number)

def call_numbers_with_limit(limit):
    for number in range(0,limit):
        print(number)

def calculator(x=10, y=15):
    return x+y

call_numbers()
print("-------------------------")
call_numbers_with_limit(50)
print("-------------------------")
print("Result is: ", calculator(10,5))
print("Result is: ", calculator())
