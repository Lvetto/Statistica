"""
    Esportare i file da excel in formato csv, con struttura:

    A  B  vincoli
    x1 y1 sigma1
    x2 y2 sigma2
    ....

"""

infiles = ["t.csv"]    #   Nome dei file

for filename in infiles:
    with open(filename, "r") as file:
        lines = file.readlines()

    lines = [i.split(";") for i in lines]
    lines = [[i.replace(",",".") for i in j if i != '\n'] for j in lines]

    try:
        float(lines[0][0])
    except:
        lines = lines[1:]
    lines = [[float(j) for j in i] for i in lines]

    fs = [i[0] for i in lines]
    As = [i[1] for i in lines]

    mn = 0
    for i, _ in enumerate(As):
        if As[i] > As[mn]:
            mn = i
    
    print(f"Frequenza: {fs[mn]}; Ampiezza: {As[mn]}")
    print("-"*100)

