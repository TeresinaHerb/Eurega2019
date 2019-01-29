import collections

file = open('team.txt', 'r')
temp = file.read().strip()
file.close()

team19 = list()
for x in temp.split():
    team19.append(x)

rotations = 12
count_cox = collections.defaultdict(int)
count_stroke = collections.defaultdict(int)

i = 0
while i < 1:
    boat19 = list()
    cox = team19[i%5]
    boat19.append(team19[(i+1)%5])
    boat19.append(team19[(i+2)%5])
    boat19.append(team19[(i+3)%5])
    boat19.append(team19[(i+4)%5])
    count_cox[cox] += 1
    count_stroke[boat19[0]] += 1
    #generate the n rotations required in ~6:30h
    j = 0
    n = 3
    print("Start setup ")
    print(cox+"\t"+boat19[0]+"\t"+boat19[1]+"\t"+boat19[2]+"\t"+boat19[3])
    while j < rotations:
        temp = cox
        cox = boat19[n%4]
        boat19[n%4] = temp
        count_cox[cox] += 1
        count_stroke[boat19[0]] += 1
        print(cox+"\t"+boat19[0]+"\t"+boat19[1]+"\t"+boat19[2]+"\t"+boat19[3])
        n = n-1
        j += 1

    i += 1

    print(count_cox)
    print(count_stroke)