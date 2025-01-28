def get_grade(subject):
    while True:
        try:
            grade_input = input(f"Enter the grade for {subject}: ")
            grade = float(grade_input)
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error! Grade must be between 0 and 100.")
        except ValueError:
            print("Error! Please enter a valid grade.")

def get_student_info():
    student_name = input("Enter student name: ")
    english_grade = get_grade("English")
    math_grade = get_grade("Math")
    return {
        "name": student_name,
        "english_grade": english_grade,
        "math_grade": math_grade
    }

def print_student_info(students):
    print("\nStudent Information:")
    for student in students:
        best_grade = max(student["english_grade"], student["math_grade"])
        average_grade = (student["english_grade"] + student["math_grade"]) / 2
        print(f"Name: {student["name"]}")
        print(f"Best Grade: {best_grade:.2f}")
        print(f"Average Grade: {average_grade:.2f}\n")

def calculate_average_grades(students):
    total_english = 0
    total_math = 0
    total_grades = 0
    total_subjects = 0

    for student in students:
        total_english += student["english_grade"]
        total_math += student["math_grade"]
        total_grades += student["english_grade"] + student["math_grade"]
        total_subjects += 2

    average_english = total_english / len(students)
    average_math = total_math / len(students)
    overall_average = total_grades / total_subjects

    average_grades_per_subject = {
        "English": average_english,
        "Math": average_math
    }

    return average_grades_per_subject, overall_average

def calculate_failing_grades(students):
    failing_count_per_student = []
    total_failing_grades = 0

    for student in students:
        failing_grades = 0

        if student["english_grade"] <= 55:
            failing_grades += 1
            total_failing_grades += 1

        if student["math_grade"] <= 55:
            failing_grades += 1
            total_failing_grades += 1

        failing_count_per_student.append((student["name"], failing_grades))

    return failing_count_per_student, total_failing_grades

def main():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students <= 0:
                print("Please enter a positive number of students.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    students_list = []

    for x in range(num_students):
        print(f"\nEntering information for student {x + 1}")
        student_info = get_student_info()
        students_list.append(student_info)

    print_student_info(students_list)

    average_grades_per_subject, overall_average_grade = calculate_average_grades(students_list)

    print("\nAverage grades per subject:")
    for subject, average_grade in average_grades_per_subject.items():
        print(f"{subject}: {average_grade:.2f}")

    print(f"\nOverall average grade across all subjects: {overall_average_grade:.2f}")

    failing_count_per_student, total_failing_grades = calculate_failing_grades(students_list)

    print("\nFailing grades per student:")
    for student_name, failing_grades in failing_count_per_student:
        print(f"{student_name}: {failing_grades} failing grade(s)")

    print(f"\nTotal failing grades across all students and subjects: {total_failing_grades}")

main()
