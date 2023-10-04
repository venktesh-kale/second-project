class Person:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0

    def user_input(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.age = int(input("Enter your age: "))

    def display(self):
        print(f"firstname = {self.first_name}")
        print(f"lastname = {self.last_name}")
        print(f"age = {self.age}")
def main():
    user = Person
    user.user_input(self=)
    user.display(self=)

main()




