from math import sqrt

"""
    Esportare i file da excel in formato csv, con struttura:

    x1 y1 sigma1
    x2 y2 sigma2
    ....

"""

infiles = ["a.csv"]    #   Nome dei file

for filename in infiles:
    with open(filename, "r") as file:
        lines = file.readlines()

    lines = [i.split(";") for i in lines]
    lines = [[i.replace(",",".") for i in j] for j in lines]

    try:
        float(lines[0][0])
    except:
        lines = lines[1:]
    lines = [[float(j) for j in i] for i in lines]

    xs = [i[0] for i in lines]
    ys = [i[1] for i in lines]
    sigmas = [i[2] for i in lines]

    Sw = sum([1/(s**2) for s in sigmas])
    Sx = sum([x/(s**2) for x,s in zip(xs,sigmas)])
    Sxx = sum([x**2/s**2 for x,s in zip(xs,sigmas)])
    Sy = sum([y/s**2 for y,s in zip(ys,sigmas)])
    Sxy = sum([(x*y)/s**2 for x,y,s in zip(xs,ys,sigmas)])
    Delta = Sxx*Sw-Sx**2

    A = (Sxx*Sy-Sxy*Sx)/Delta
    B = (Sxy*Sw-Sx*Sy)/Delta
    sigma_a = sqrt(Sxx/Delta)
    sigma_b = sqrt(Sw/Delta)

    print(f"A= {A} +- {sigma_a}; B= {B} +- {sigma_b}".replace(".", ","))
    print("-"*100)
