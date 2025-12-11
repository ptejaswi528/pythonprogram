def student(*tup):
    tup=[tup1,tup2,tup3,tup4,tup5]
    for i in range(len(tup)):
        print(f"Student {i+1} details: {tup[i]}")
    print("Students with marks greater than 75:")
    for i in range(len(tup)):
        if tup[i][2] > 75:
            print(tup[i][1])
    print("Student with maximum marks:")
    max_marks = max(tup, key=lambda x: x[2])
    print(max_marks[1])
tup1=(67,"Veda",23)
tup2=(75,"Tejaswi",18)
tup3=(85,"deepthi",95)
tup4=(95,"jahnavi",85)
tup5=(90,"khushi",97)
student(tup1,tup2,tup3,tup4,tup5)