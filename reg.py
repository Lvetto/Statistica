infiles = ["1.out"]

for filename in infiles:
    with open(filename, "r") as file:
        lines = file.readlines()

    lines = [i.split(" ") for i in lines]
    lines = [[float(j) for j in i] for i in lines]

    sigma = lines[0][0]
    lines = lines[1:]
    xs = [i[0] for i in lines]
    ys = [i[1] for i in lines]

    Sw = len(xs)*(1/sigma**2)
    Sx = sum([i/sigma**2 for i in xs])
    Sxx = sum([i**2/sigma**2 for i in xs])
    Sy = sum([i/sigma**2 for i in ys])
    Sxy = sum([xs[n]*ys[n]/sigma**2 for n,_ in enumerate(xs)])
    Delta = Sxx*Sw-Sx**2

    A = (Sxx*Sy-Sxy*Sx)/Delta
    B = (Sxy*Sw-Sx*Sy)/Delta
    sigma_a = (Sxx/Delta)**(1/2)
    sigma_b = (Sw/Delta)**(1/2)

    print(f"{A};{B};{sigma_a};{sigma_b}")
    print("-"*100)
