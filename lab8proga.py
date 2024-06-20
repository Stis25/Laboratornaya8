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
        print("3. Shallow clone a prototype")
        print("4. Deep clone a prototype")
        print("7. Modify a prototype's data")
        print("6. Exit")
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
            name = input("Enter the name of the prototype to clone: ")
            if name in prototypes:
                new_name = input("Enter the name for the new shallow clone: ")
                prototypes[new_name] = prototypes[name].clone()
                print(f"Prototype '{name}' shallow cloned as '{new_name}'.")
            else:
                print(f"No prototype found with the name '{name}'.")

        elif choice == '4':
            name = input("Enter the name of the prototype to clone: ")
            if name in prototypes:
                new_name = input("Enter the name for the new deep clone: ")
                prototypes[new_name] = prototypes[name].deep_clone()
                print(f"Prototype '{name}' deep cloned as '{new_name}'.")
            else:
                print(f"No prototype found with the name '{name}'.")

        elif choice == '7':
            name = input("Enter the name of the prototype to modify: ")
            if name in prototypes:
                new_data = input("Enter the new data for the prototype (as a comma-separated list): ")
                new_data_list = new_data.split(',')
                prototypes[name].data = new_data_list
                print(f"Prototype '{name}' modified.")
            else:
                print(f"No prototype found with the name '{name}'.")

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
1