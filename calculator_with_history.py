history_file = "history.txt"

def show_history():
    try:
        with open(history_file, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No history found!")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history found!")

def clear_history():
    with open(history_file, 'w') as file:
        pass
    print("History cleared")

def save_to_history(equation, result):
    with open(history_file, 'a') as file:
        file.write(f"{equation}={result}\n")

def calculate(user_input):
    try:
        num1, operator, num2 = user_input.split()
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input")
        return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    if int(result) == result:
        result = int(result)
    print("Result: ", result)

    save_to_history(user_input, result)

def main():
    print("--SIMPLE CALCULATOR(type history, clear, quit)")
    while True:
        user_input = input("Enter a calculation (+, -, *, /) or command [History | Clear | Quit]: ").strip()
        user_input = user_input.lower()
        if user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        elif user_input == "quit":
            break
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()