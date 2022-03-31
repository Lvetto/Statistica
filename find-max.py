from math import log

infiles = ["g.out", "m.out", "p.out"]

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

    p0 = sum(pos)/len(pos)

    print("0.1")
    [print(f"{times[i]} {log(pos[i]-p0)}".replace(".", ".")) for i in maxinds]
    #dts = [times[maxinds[n+1]]-times[maxinds[n]] for n, _ in enumerate(maxinds[1:-1])]
    
    #print(sum(dts)/len(dts))
    print("-"*100)
