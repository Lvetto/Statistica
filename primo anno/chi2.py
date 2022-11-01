from math import sqrt
xs = [0.0847, 0.1045, 0.1241, 0.1437, 0.1637, 0.1737, 0.1934, 0.2134, 0.233] #Inserire lista dei dati da ricavare
ys = [0.0110667, 0.0135651, 0.0157323, 0.0184636, 0.0210075, 0.0219732, 0.0241158, 0.0265877, 0.0294600] #Inserire lista dei dati reali
dy = [0.000018, 0.000028, 0.000038, 0.000052, 0.000068, 0.000074, 0.000089, 0.00011, 0.00013]                 #Errore

def f(x):
    A = -0.000703691          #Intercetta
    B = 0.122475456              #Coeficiente angolare
    return A + B*x

chi2 = sum([((ys[i]-f(xs[i]))/dy[i])**2 for i, _ in enumerate(xs)])
gdl = len(xs) - 1           #cambiare il numero col numero edi vincoli!
print(f"Chi2 ridotto: {chi2/gdl}, gradi di libertà: {gdl}")
