# Matthew Shen Quiz 1
# mds820

score_list = [
    'Jackie: 88 94 78 96 100',
    'Mike: 75 78 91 80 84',
    'Jen: 81 72 87 93 95',
    'Chris: 94 70 83 86 90'
]


for i in score_list:

    splitList = i.split(':')
    
    name = splitList[0]

    scores = splitList[1].split()

    floatScores = []

    for j in scores:
        floatScores.append(float(j))

    averageScore = sum(floatScores) / len(floatScores)

    print(name,averageScore)


for stu in score_list:
    name, grades = stu.split(':')
    grades = [int(i) for i in grades.split()]
    # grades = map(int(), grades)
    print(name, sum(grades)/len(grades))


#