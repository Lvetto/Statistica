#infiles = [f"_molla media/misura{n}.csv" for n in range(1,11)]
#outfiles = [f"out-media2{n}.dat" for n in range(1,11)]

infiles = ["in.csv"]
outfiles = ["1.out"]

for n,f in enumerate(infiles):
    file = open(f, "r")
    out = open(outfiles[n], "w")

    lines = file.readlines()
    for m, line in enumerate(lines):
        if m==0:
            continue
        t = list(line)
        for i, c in enumerate(t):
            if c==',':
                t[i]='.'
            if c==';':
                t[i]=' '
        t = "".join(t)
        out.write(t)
