import numpy as np
from math import sin, cos
from numpy import log

#Trasformata di fourier con interpolazione parabolica e gaussiana [fonte:http://cds.cern.ch/record/738182/files/ab-2004-023]

infiles = ["chiuso/modo 1c.csv", "chiuso/modo 2c.csv", "chiuso/modo 3c.csv", "chiuso/modo 4c.csv", "chiuso/modo 5c.csv"]    #   Nome dei file

for filename in infiles:
    with open(filename, "r") as file:
        lines = file.readlines()

    lines = [i.split(";") for i in lines]
    lines = [[i.replace(",",".") for i in j if i != '\n'] for j in lines]

    try:
        float(lines[0][0])
    except:
        lines = lines[1:]
    lines = [[float(j) for j in i] for i in lines if i!=[""]]

    ys = [i[0] for i in lines]
    xs = [i[1] for i in lines]

    d = sum([xs[i+1]-xs[i] for i, _ in enumerate(xs[1:])])/len(xs)

    A = np.fft.fft(ys, norm="forward")
    freqs = np.fft.fftfreq(len(ys), d)

    print(f"{filename}")
    print("Frequenza; Ampiezza; Fase")
    [print(f"{freqs[i]}; {2*np.abs(A[i])}; {2*np.angle(A[i])}".replace(".",",")) for i, _ in enumerate(A[:len(A)//2])]

    M = [np.abs(i) for i in A]
    km = M.index(np.amax(M[:len(A)//2]))
    dm2 = (log(M[km+1]/M[km-1]))/(2*log((M[km]**2)/(M[km-1]*M[km+1])))
    f2 = (km+dm2)/(d*len(ys))
    dm = (M[km+1]-M[km-1])/(2*(2*M[km]-M[km-1]-M[km+1]))
    f = (km+dm)/(d*len(ys))

    print(f"F int:; {f2:.2f}; {f:.2f}".replace(".",","))
