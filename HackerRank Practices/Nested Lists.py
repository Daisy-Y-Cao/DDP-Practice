if __name__ == '__main__':
    
    students_scores = []
    student_num = int(input())

# Input names and scores for each student
    for _ in range(student_num):
        name = input()
        score = float(input())
        students_scores.append([name, score])

# Sort the students based on scores
    students_scores.sort(key=lambda x: x[1])

# Find the second lowest score
    second_lowest_score = sorted(set(student[1] for student in students_scores))[1]

# Collect names of students with the second lowest score
    second_lowest_students = [student[0] for student in students_scores if student[1] ==    second_lowest_score]

# Sort the names alphabetically
    second_lowest_students.sort()

# Print the names of students with the second lowest score
    for student in second_lowest_students:
        print(student)




    
    
