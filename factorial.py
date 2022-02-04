while True:
    number = (input("Enter The Number For Factorial OR q To Quit : \n"))
    
    no = number

    factorial = 1
    

    if number != "q":
        number = int(number)
        for num in range(number):
            if number > 0:
                factorial *= number
                number += -1

    else:
        print("THANK YOU !")
        break

    print(f"""
The Factorial Of {no} = {factorial}
""")


    list = []
    factorial = str(factorial)

    for num in factorial:
        list.append(num)


    trail = []

    for num in list:
        if "0" in list[-1]:
            trail.append("yes")
            list.pop(-1)

    yes = trail.count("yes")
    print(f"""No Of Trailling 0 = {yes}
    """)
            