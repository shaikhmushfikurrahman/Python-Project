import json

class Student:
    def __init__(self, name, age, roll_id):
        """Initialize student details."""
        self.name = name
        self.age = age
        self.roll_id = roll_id

    def display_info(self):
        """Display student information."""
        print(f"\nStudent Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll ID: {self.roll_id}")

    def to_dict(self):
        """Convert the student object to a dictionary for saving."""
        return {"name": self.name, "age": self.age, "roll_id": self.roll_id}

    @classmethod
    def from_dict(cls, data):
        """Create a student object from a dictionary."""
        return cls(data["name"], data["age"], data["roll_id"])


class StudentManager:
    def __init__(self):
        """Initialize student list."""
        self.students = []
        self.load_students()

    def add_student(self):
        """Add a new student."""
        name = input("\nEnter Name: ")
        age = input("Enter Age: ")
        while not age.isdigit():  # Validate that the age is a number
            print("Invalid age. Please enter a valid number for age.")
            age = input("Enter Age: ")
        roll_id = input("Enter Roll ID: ")
        student = Student(name, int(age), roll_id)
        self.students.append(student)
        print("Student added successfully!")
        self.save_students()

    def view_students(self):
        """Display all students."""
        if not self.students:
            print("\nNo student records available.")
            return
        print("\nStudent Records:")
        for student in self.students:
            student.display_info()

    def delete_student(self):
        """Delete a student by Roll ID."""
        if not self.students:
            print("\nNo student records available to delete.")
            return
        roll_id = input("\nEnter Roll ID to delete: ")
        for student in self.students:
            if student.roll_id == roll_id:
                self.students.remove(student)
                print(f"Student with Roll ID {roll_id} deleted successfully!")
                self.save_students()
                return
        print("Student not found!")

    def search_student(self):
        """Search for a student by name or roll ID."""
        search_term = input("\nEnter name or roll ID to search: ")
        found_students = [student for student in self.students if
                          search_term.lower() in student.name.lower() or search_term in student.roll_id]
        if found_students:
            print("\nSearch Results:")
            for student in found_students:
                student.display_info()
        else:
            print("No student found with that name or Roll ID.")

    def update_student(self):
        """Update student details by Roll ID."""
        roll_id = input("\nEnter Roll ID to update: ")
        for student in self.students:
            if student.roll_id == roll_id:
                new_name = input(f"Enter new name (Current: {student.name}): ") or student.name
                new_age = input(f"Enter new age (Current: {student.age}): ") or str(student.age)
                while not new_age.isdigit():
                    print("Invalid age. Please enter a valid number for age.")
                    new_age = input(f"Enter new age (Current: {student.age}): ") or str(student.age)
                student.name = new_name
                student.age = int(new_age)
                print(f"Student with Roll ID {roll_id} updated successfully!")
                self.save_students()
                return
        print("Student not found!")

    def save_students(self):
        """Save the student list to a file."""
        with open("students.json", "w") as f:
            json.dump([student.to_dict() for student in self.students], f)

    def load_students(self):
        """Load the student list from a file."""
        try:
            with open("students.json", "r") as f:
                students_data = json.load(f)
                self.students = [Student.from_dict(data) for data in students_data]
        except FileNotFoundError:
            self.students = []

    def run(self):
        """Main loop with options."""
        while True:
            print("\n========================")
            print(" Student Manager")
            print("========================")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Search Student")
            print("5. Update Student")
            print("6. Exit")
            print("========================")
            choice = input("Select an option: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.search_student()
            elif choice == "5":
                self.update_student()
            elif choice == "6":
                print("Exiting program... Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    manager = StudentManager()
    manager.run()

