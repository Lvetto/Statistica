infiles = ["piccola.out", "media.out", "grande.out"]

for filename in infiles:
    with open(filename, "r") as file:
        lines = file.readlines()

    lines = [i.split(" ") for i in lines]
    lines = [[float(j) for j in i] for i in lines]
    #print([i for i in lines])

    pos = [i[1] for i in lines]
    times = [i[0] for i in lines]
    pos2 = [sum(pos[n-5:n+5])/10 for n,_ in enumerate(pos[5:-5])][5:]
    maxinds = [n+6 for n, _ in enumerate(pos2[1:-1]) if pos2[n]<pos2[n+1] and pos2[n+1]>pos2[n+2]]

    [print(f"{pos[i]};{times[i]}".replace(".", ",")) for i in maxinds]
    print("-"*100)

