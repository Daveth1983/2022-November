

def ask_for_a_number(force_valid_input):
    while True:
        inp = input("Please provide a number! ")
        if is_number(inp):
            return float(inp)
        else:
            if not force_valid_input:
                return None
            print("This didn't look like a number, try again.")

#komentarz
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def simple_calculator():
    while True:
        a = ask_for_a_number(force_valid_input=False)
        if a is None:
            break
        op = ask_for_an_operation(force_valid_input=True)
        b = ask_for_a_number(force_valid_input=True)
        result = calc(op, a, b)
        if result is not None:
            print(f"The result is {result}")





def calc(operation, a, b):
    if not is_valid_operation(operation) or not is_number(a) or not is_number(b):
        return None
    result = None
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b != 0:
            result = a / b
        else:
            print("Error: Division by zero")
            return None
    return result


def ask_for_an_operation(force_valid_input):
    while True:
        operation = input("Please provide an operation (one of +, -, *, /)! ")
        if is_valid_operation(operation):
            return operation
        else:
            if not force_valid_input:
                return None
            print("Unknown operation.")


def is_valid_operation(operation):
    operations = ('+', '-', '*', '/')
    return operation in operations


if __name__ == "__main__":
    simple_calculator()