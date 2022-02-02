def main():
    num = float(input("enter a number (0 to quit)):\n"))
    exp = float(input("enter the exponent:\n"))
    while num != 0:
        print(f"recursion attempt: {num}^{exp} = {power(num,exp)}\n")
        return
    return 0;

def power(number,exponent):
    if exponent ==1:
        return number
    elif exponent == 0:
        return number
    elif number == 0:
        return 0;
    elif exponent <= 0:
        return float(1/(number * power(number, -1 * (exponent + 1))))
    else:
        return number  * power(number,exponent - 1)
    pass




main()
