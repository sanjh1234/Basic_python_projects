def factorial(x):
    if x == 0 or x == 1:
        return 1

    else:
        return x * factorial(x-1)


def trailing(x):
    a=5
    count = 0
    while x // a > 0:
        count += (x//a)
        a = a*5
    return count    



if __name__ == '__main__':
    number = int(input("""
Enter The Number For Factorial : 
 """))
    fac = factorial(number)
    print(f"""The Factorial Of {number} = {fac}
    """)
    
    trail = trailing(number)
    print(f"""The Factorial Trailing Zeros Of {number} = {trail}
    """)