from operator import itemgetter

def sort_score():
    f = open("filename.log.txt", 'r')
    line = f.readlines()
    #line = ['game1, number, name, 5', 'game2, number, name, 3','game2, number, name, 2','game1, number, name, 100','game1, number, name, 30','game2, number, name, 20','game1, number, name, 1000','game1, number, name, 1200','game2, number, name, 203','game2, number, name, -30','game2, number, name, -35']

    line2 = []
    line3 = []
    game1 = []
    top_game1 = []
    game2 = []
    top_game2 = []
    final = []
    for i in range(0, len(line)):
        line2.append(line[i].split(", "))
        line3.append(list(map(lambda x: int(x) if line2[i][3] == x else x, line2[i])))
    print(line3)


    for j in range(0, len(line2)):
        if line3[j][0] == "game1":
            game1.append(line3[j])
        else:
            game2.append(line3[j])


    #game1 sort
    game1 = sorted(game1, key=itemgetter(3))
    game1.reverse()
    for k in range(0, 5):
        top_game1.append(game1[k])

    #game2 sort
    game2 = sorted(game2, key=itemgetter(3))
    game2.reverse()
    for k in range(0, 5):
        top_game2.append(game2[k])

    #return list
    final = top_game1 + top_game2

    return final

value = sort_score()
print("return")
print(value)