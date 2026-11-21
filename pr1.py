def calculate(a, b, op):
    if op =="+":
        print(a + b)
    elif op =="-":
        print(a - b)
    elif op =="*":
        print(a * b)
    elif op =="/":
        print(a / b)
    else:
        print("no such operation is available")

def count(filename):
    with open(filename, "r") as f:
        count = 0
        for line in f: 
            count = count + 1
    return count

def remove(filename):
    with open(filename, "w") as f:
        pass

def read(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

def write(filename, text):
    with open(filename, "a") as f:
        f.write(text + "\n")

def main():
    while True:
        print("")
        print("-------------")
        print("menu")
        print("1. Calculate")
        print("2. Count lines in file")
        print("3. Remove content from file")
        print("4. Read file")
        print("5. Write to file")
        print("6. Exit")
        print("--------------")
        print("")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                op = input("Enter operation (+, -, *, /): ")
                calculate(a, b, op)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                pass
            except ZeroDivisionError:
                print("Can not divide by zero")
                pass
        elif choice == "2":
            filename = input("Enter filename: ")
            print(f"Number of lines: {count(filename)}")
        elif choice == "3":
            filename = input("Enter filename: ")
            remove(filename)
            print(f"Content removed from {filename}")
        elif choice == "4":
            filename = input("Enter filename: ")
            read(filename)
        elif choice == "5":
            filename = input("Enter filename: ")
            text = input("Enter text to write: ")
            write(filename, text)
            print(f"Text written to {filename}")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

main()