if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    li=[]
    #print(student_marks)
    for i in student_marks:
        if i==query_name:
            li=student_marks[i]
    sum=0
    count=0
    for i in li:
        count+=1
        sum=sum+i
    avg=float(sum/count)
    print(f"{avg:.2f}")
