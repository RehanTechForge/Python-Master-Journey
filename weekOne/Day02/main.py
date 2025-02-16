# students = {}  # Dictionary to store student records
# student_id = 1  # Auto-incrementing student ID

# def add_student(name, age, student_class):
#     global student_id
#     students[student_id] = {
#         "name": name,
#         "age": age,
#         "class": student_class
#     }
#     print(f"Student added successfully with ID: {student_id}")
#     student_id += 1

# def update_student(student_id, name=None, age=None, student_class=None):
#     if student_id in students:
#         if name:
#             students[student_id]["name"] = name
#         if age:
#             students[student_id]["age"] = age
#         if student_class:
#             students[student_id]["class"] = student_class
#         print("Student record updated successfully.")
#     else:
#         print("Student ID not found.")

# def delete_student(student_id):
#     if student_id in students:
#         del students[student_id]
#         print("Student record deleted successfully.")
#     else:
#         print("Student ID not found.")

# def get_student(student_id):
#     return students.get(student_id, "Student ID not found.")

# def list_students():
#     if not students:
#         print("No students found.")
#         return
#     for student_id, details in students.items():
#         print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Class: {details['class']}")

# def search_students(search_term):
#     results = [
#         {"ID": sid, "Details": details}
#         for sid, details in students.items()
#         if search_term.lower() in details["name"].lower()
#     ]
#     return results if results else "No matching students found."

# # Example CLI Usage
# if __name__ == "__main__":
#     while True:
#         print("\n1. Add Student\n2. Update Student\n3. Delete Student\n4. Get Student\n5. List Students\n6. Search Student\n7. Exit")
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             name = input("Enter name: ")
#             age = input("Enter age: ")
#             student_class = input("Enter class: ")
#             add_student(name, age, student_class)
#         elif choice == "2":
#             student_id = int(input("Enter Student ID: "))
#             name = input("Enter new name (leave blank to skip): ") or None
#             age = input("Enter new age (leave blank to skip): ") or None
#             student_class = input("Enter new class (leave blank to skip): ") or None
#             update_student(student_id, name, age, student_class)
#         elif choice == "3":
#             student_id = int(input("Enter Student ID: "))
#             delete_student(student_id)
#         elif choice == "4":
#             student_id = int(input("Enter Student ID: "))
#             print(get_student(student_id))
#         elif choice == "5":
#             list_students()
#         elif choice == "6":
#             search_term = input("Enter name to search: ")
#             print(search_students(search_term))
#         elif choice == "7":
#             break
#         else:
#             print("Invalid choice. Please try again.")


# num_of_list = [12,45,76,34,34,34,89,123,45,76,34,34,]

# print(num_of_list)

# num_of_list.sort()

# print("Sorted List:", num_of_list)

# print("Length of List:", len(num_of_list))

# print("Maximum Number of", num_of_list[-1])

# print("Minimum Number of", num_of_list[0])


list_one = ["one", "two", "three"]

list_two = ["four", "five", "six"]

combined_list = list_one + list_two

print(type(combined_list))
