from operator import itemgetter

def sort_score():
    f = open("scoreboard.txt", 'r')
    line = f.readlines()
    f.close()


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
    for l in range(0, 5):
        top_game2.append(game2[l])

    #return list
    final = top_game1 + top_game2

    return final

value = sort_score()
print(value)
f = open("top5_list.txt", "w")
for m in range(0, len(value)):
    f.write(str(value[m])+"\n")
f.close()
