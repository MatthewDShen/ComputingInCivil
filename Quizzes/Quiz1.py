# Matthew Shen Quiz 1
# mds820

scoreList = [
    'Jackie: 88 94 78 96 100',
    'Mike: 75 78 91 80 84',
    'Jen: 81 72 87 93 95',
    'Chris: 94 70 83 86 90'
]

numScores = 5

for i in scoreList:

    splitList = i.split(':')
    
    name = splitList[0]

    scores = [splitList[1].split(' ')]

    floatScores = []

    # for i scores:
    #     floatScores[i] = float(j)

    averageScore = sum(scores) / len(score)

    print(name,averageScore)


