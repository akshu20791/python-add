import sys

# yes, just adding two numbers

def add_two_numbers(a=0, b=0):

    result = a + b

    print(f"a is {a}")

    print(f"b is {b}")

    print(f"solution is {result}")





if __name__ == "__main__":

    if len(sys.argv) > 2:

        add_two_numbers(int(sys.argv[1]), int(sys.argv[2]))

    else:

        add_two_numbers()


