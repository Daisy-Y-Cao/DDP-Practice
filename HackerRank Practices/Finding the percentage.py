if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_list = student_marks[query_name]
    sum_of_scores = sum(query_list)
    outcome = "{:.2f}".format(sum_of_scores / 3)
    
    print(outcome)
