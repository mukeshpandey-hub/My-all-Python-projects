import csv 

print("::::Welcome to the Student Record Management System::::")
print("""1. Add Student Record
        2. search Student Records
        3. Update Student Records
        4. calculate Average Grade
        5. Exit""")

choice = int(input("Enter your choice from the above options 1,2,3,4,5: "))

def add_student_record():
    with open('student_records.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        header = ['Student ID', 'Name', 'Age', 'Grade']
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        grade = input("Enter Student Grade: ")
        writer.writerow(header)
        writer.writerow([student_id, name, age, grade])
        
def search_student_record():
    student_id = int(input("Enter Student ID to search: "))
    with open('student_records.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(student_id):
                print(f"Student ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
                return
        print("Student record not found.")        

def update_student_record():
    student_id = int(input("Enter Student ID to update: "))
    with open('student_records.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(student_id):
                name = input("Enter new Student Name: ")
                age = int(input("Enter new Student Age: "))
                grade = input("Enter new Student Grade: ")
                row[1] = name
                row[2] = age
                row[3] = grade
                print("Student record updated successfully.")
            else:
                print("Student record not found.")
                
def calculate_average_grade():
    with open ('student_records.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            grades = []
            for row in reader:
                grades.append(float(row[3]))
            average_grade = sum(grades) / len(grades)
            print(f"The average grade of all students is: {average_grade}")

if choice == 1:
    add_student_record()
elif choice == 2:
    search_student_record()     
elif choice == 3:
    update_student_record() 
elif choice == 4:
    calculate_average_grade()
else:
    print("Exiting the Student Record Management System. Goodbye!")                            