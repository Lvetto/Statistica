from math import sqrt


"""
    Esportare i file da excel in formato csv, con struttura:

    A  B  vincoli
    x1 y1 sigma1
    x2 y2 sigma2
    ....

"""

infiles = ["a.csv", "a.csv"]    #   Nome dei file

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

    A,B,v = lines[0]
    lines = lines[1:]
    xs = [i[0] for i in lines]
    ys = [i[0] for i in lines]
    dy = [i[0] for i in lines]

    def f(x):
        return A + B*x

    chi2 = sum([((ys[i]-f(xs[i]))/dy[i])**2 for i, _ in enumerate(xs)])
    gdl = len(xs) - v
    print(f"Chi2 ridotto: {chi2/gdl}, gradi di libertà: {gdl}")
    print("-"*100)
