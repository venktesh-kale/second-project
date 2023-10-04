class Person:
    def _init_(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0

    def get_user_input(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.age = int(input("Enter your age: "))



    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")

def main():
    user = Person()
    user.get_user_input()
    user.display_info()

main()