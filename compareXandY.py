print('##############################################')
print('\n'*2)
print("This program will compare numbers you provide type integers and return a value")
print('\n'*2)
print('##############################################')
num2run = int(input("Enter how many times should we loop this program: "))


def compare(num2run):
    for any in range(num2run):
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        # nested function

        def logic(x, y):
            if x > y:
                return 1
            elif x < y:
                return -1
            elif x == y:
                return 0

        result = logic(x, y)
        print(result)
        print("this is attempt number ", any+1)


compare(num2run)
