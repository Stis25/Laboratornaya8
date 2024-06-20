import copy

class Prototype:
    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self):
        return f"Name: {self.name}, Data: {self.data}"

def main():
    prototypes = {}

    while True:
        print("\nPrototype Pattern Console Application")
        print("1. Create a new prototype")
        print("2. View prototypes")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the prototype: ")
            data = input("Enter the data for the prototype (as a comma-separated list): ")
            data_list = data.split(',')
            prototypes[name] = ConcretePrototype(name, data_list)
            print(f"Prototype '{name}' created.")

        elif choice == '2':
            for name, prototype in prototypes.items():
                print(f"{name}: \n {prototype}")

        elif choice == '3':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
1