def main():
    num = int(input("enter a number (0 to quit)):\n"))
    while num != 0:
        while num < 0:
            num = int(input("enter a positive number"))
        print(f"recursion attempt: {num}! = {rfact(num)}")
        return
    return 0;

def power(number):
    if number == 1:
        return number
    else:
        return number * rfact(number-1);

main()
