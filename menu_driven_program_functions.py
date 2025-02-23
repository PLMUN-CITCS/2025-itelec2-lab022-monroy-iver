# Iver John Monroy
# ITELEC2
# Laboratory # 22 - Group Activity # 01 - Problem 04: Simple Menu-Driven Program with Function-Based Operations

def main():
    while True:
        print("\nMenu:")
        print("1. Greet User")
        print("2. Check Even/Odd")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                print("Hello! Welcome!")
            elif choice == 2:
                try:
                    num = int(input("Enter an integer: "))
                    if num % 2 == 0:
                        print(f"{num} is an Even number.")
                    else:
                        print(f"{num} is an Odd number.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            elif choice == 3:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()