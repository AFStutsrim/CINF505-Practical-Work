import json


#Use this function to add a student to the gradebook
def add_student(gradebook, student_id, student_name):
    if student_id in gradebook.keys():
        print('This Student ID already exists')
    else:
        gradebook[student_id] = {}
        gradebook[student_id]["student_name"] = student_name
        #print(gradebook)
    print("Student added successfully!")


#Use this function to add a grade for a specific student and subject in the gradebook
def add_grade(gradebook, student_id, subject, grade):
    if "grades" not in gradebook[student_id]:
        gradebook[student_id]["grades"] = {}
        #print("first if statement triggered")
    
    if subject not in gradebook[student_id]["grades"].keys():
        #print("second if statement triggered")
        gradebook[student_id]["grades"][subject] = []
    gradebook[student_id]["grades"][subject].append(grade)
    #print(gradebook)
    print("Grade added successfully!")


#Use this function to calculate the average grade for a student in a specific subject
def calculate_average(gradebook, student_id, subject):
    grade_sum = 0
    grade_count = len(gradebook[student_id]["grades"][subject])
    for grade in gradebook[student_id]["grades"][subject]:
        #print(grade)
        grade_sum += grade
    grade_average = grade_sum / grade_count
    student_name = gradebook[student_id]["student_name"]
    #print(gradebook[student_id]["student_name"])
    print("Average grade for " + student_name + " in " + subject + ": " + str(grade_average))
    

#Use this function to list all the students and their ID numbers
def list_all_students(gradebook):
    print("List of students:")
    for id in gradebook:
        print ("Student ID: " + str(id) + ", Name: " + gradebook[id]["student_name"])


#Use this function to list all the grades for a specific student
def list_all_grades(gradebook, student_id):
    #print("hi")
    #print(gradebook[student_id]["grades"])
    print(gradebook[student_id]["student_name"] + "'s Grades:")
    for subject in gradebook[student_id]["grades"]:
        if len(gradebook[student_id]["grades"][subject]) == 1:
            #print(subject + ": " + str(gradebook[student_id]["grades"][subject][0]))
            print(f'{subject} : {gradebook[student_id]["grades"][subject][0]}')
        else:
            grade_list = subject + ": "
            list_length = len(gradebook[student_id]["grades"][subject]) - 1
            #print(list_length)
            for grade in range(list_length):
                #print(gradebook[student_id]["grades"][subject][grade])
                grade_list += str(gradebook[student_id]["grades"][subject][grade])
                grade_list += ", "
            grade_list += str(gradebook[student_id]["grades"][subject][list_length])
            print(grade_list)
                

#Use this function to save the entire gradebook to a text file
def export_gradebook(gradebook, file_name):
    with open(file_name, "w") as text_file:
        json.dump(gradebook, text_file, indent = 4)
    print("Gradebook exported successfully!")


#Use this function to turn load a gradebook text file and return it as a dictionary
def load_gradebook(file_name):
    #print("hi")
    #gradebook.clear()
    with open(file_name, "r") as text_file:
        new_gradebook = text_file.read()
    gradebook = json.loads(new_gradebook)
    #gradebook = new_gradebook
    #print(gradebook)
    print("Gradebook loaded successfully!")
    return(gradebook)


#Use this funtion to display the menu and prompt the user
def menu():
    welcome_message = "Welcome to Student Grade Tracker!"
    option_1 = "1. Add a Student"
    option_2 = "2. Add a Grade"
    option_3 = "3. Calculate Average Grade"
    option_4 = "4. List All Students"
    option_5 = "5. List All Grades"
    option_6 = "6. Export Gradebook"
    option_7 = "7. Load Gradebook"
    option_8 = "8. Exit"
    user_prompt = "Please enter your choice: "
    print(welcome_message)
    print()
    print(option_1 + "\n" + option_2 + "\n" + option_3 + "\n" + option_4 + "\n" + option_5 + "\n" + option_6 + "\n" + option_7 + "\n" + option_8)
    print()
    print(user_prompt)
    menu_input = input()
    return(menu_input)
    

#Use this function as the main entry point for the program
def main():
    gradebook = {}
    user_input = ""
    #add_student(gradebook, 123, "Alison")
    #add_student(gradebook, 124, "Brennan")
    #add_grade(gradebook, 123, "Math", 90.0)
    #add_grade(gradebook, 123, "Math", 60.0)
    #add_grade(gradebook, 123, "Art", 75.0)
    #add_grade(gradebook, 124, "Math", 85.0)
    #add_grade(gradebook, 124, "Science", 92.0)
    #calculate_average(gradebook, 123, "Math")
    #list_all_students(gradebook)
    #list_all_grades(gradebook, 123)
    #list_all_grades(gradebook, 124)
    #export_gradebook(gradebook, "C:\\Users\\aliso\\OneDrive\\Graduate School\\2026 Fall\\CINF505\\Programming Assignment 1\\gradebook.json")
    #print(gradebook)
    #load_gradebook("C:\\Users\\aliso\\OneDrive\\Graduate School\\2026 Fall\\CINF505\\Programming Assignment 1\\gradebook.json")
    while user_input != "8":
        user_input = menu()
        if user_input == "1":
            id1 = input("Enter student ID: ")
            user_id1 = int(id1)
            user_name1 = input("Enter student name: ")
            add_student(gradebook, user_id1, user_name1)
            print()
            #menu()
        elif user_input == "2":
            id2 = input("Enter student ID: ")
            user_id2 = int(id2)
            user_subject2 = input("Enter subject: ")
            grade2 = input("Enter grade: ")
            user_grade2 = float(grade2)
            add_grade(gradebook, user_id2, user_subject2, user_grade2)
            print()
        elif user_input == "3":
            id3 = input("Enter student ID: ")
            user_id3 = int(id3)
            user_subject3 = input("Enter subject: ")
            calculate_average(gradebook, user_id3, user_subject3)
            print()
        elif user_input == "4":
            list_all_students(gradebook)
            print()
        elif user_input == "5":
            id5 = input("Enter student ID: ")
            user_id5 = int(id5)
            list_all_grades(gradebook, user_id5)
            print()
        elif user_input == "6":
            user_file6 = input("Enter file name: ")
            export_gradebook(gradebook, user_file6)
            print()
        elif user_input == "7":
            user_file7 = input("Enter file name: ")
            load_gradebook(user_file7)
            print()
        elif user_input == "8":
            print("Goodbye!")
        else:
            print("Error: Input invalid!")
            print()
            #menu()
    #print("Goodbye!")


main()