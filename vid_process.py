from pickletools import uint8
import cv2
import numpy as np
from time import time

"""
I fotogrammi del video sono salvati come matrici, dove il nero (colore della corda) è rappresentato dal valore 256 e il bianco da 0.
I fotogrammi consecutivi sono quindi confrontati tra loro  la loro differenza in vaore assluto è sommata a una matrice delle stesse dimensioni.
La matrice è poi normalizzata rispetto al valore più alto, in modo da rappresentare la variazione media dei singoli pixel relativa.
Fissando la fotocamera relativamente al sistema e mascherando lo sfondo con un supporto bianco, tutte le variazioni al di fuori dell'oscilazione della corda risultano trascurabili.
Selezionando solo i valori maggiori di una costante scelta in maniera appropriata, risulta possibile ricavare una mappa chiara della forma d'onda, da poter poi sovrapporre a un fotogramma contenente una scala graduata per effettuare le misure
I video utilizzati sono registrati con un framerate elevato, in modo da poterli rallentare senza perdita di qualità prima di processarli.
"""

infiles = [f"vids/vid{n}.mp4" for n in range(8)]
outfiles = [f"ims/im{n}.png" for n,_ in enumerate(infiles)]

for ind,_ in enumerate(infiles):
    print(infiles[ind])
    t0 = time()

    vid = cv2.VideoCapture(infiles[ind])    # apertura file
    n = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))  # contegio fotogrammi
    h= int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))  # dimensioni fotogrammi
    w= int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

    # ritaglio immagine (inutilizzato)
    h0 = int(0)
    h1 = int(h)

    f0 = vid.read()[1]  # estrazione fotogramma su cui verrà sovrimpsta l'immagine finale
    prev = cv2.cvtColor(f0[h0:h1,:], cv2.COLOR_BGR2GRAY)    # inizializzazione fotogramma precedente
    diff_mat = np.zeros(prev.shape) # inizializzazione matrice a cui verranno sommate le differenze tra fotogrammi

    for _ in range(1, n):
        frame = vid.read()[1][h0:h1,:]  # lettura fotogramma e ritaglio
        gframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # conversione in scala di grigi (a_(ij) = media([a_(ij).b, a_(ij).g, a_(ij).r]))
        gframe = np.full(prev.shape, 256) - gframe  # inversione colore fotogramma (256 = bianco, 0 = nero --> 0 = bianco, 256 = nero)
        outframe = np.absolute(gframe-prev) # differenza col fotogramma precedente
        diff_mat += outframe
        prev = gframe   # il fotogramma attuale diventa il precedente per l'iterazione successiva

    m = np.amax(diff_mat)   # valore massimo della matrice
    im2 = (256 * diff_mat) / m  # la matrice viene riscalata rispetto al valore massimo (ora assegnato a 256)
    #cv2.imwrite(outfiles[ind][:-4] + " st1.png", im2)   #save stages

    _, im2 = cv2.threshold(im2, 50, 255, cv2.THRESH_BINARY) # i punti con valore superiori a 50 (parametro arbitrario) sono assegnati a 255, gli altri scartati
    #cv2.imwrite(outfiles[ind][:-4] + " st2.png", im2)   #save stages

    im2 = im2.astype(np.uint8)
    im2 = cv2.Canny(im2, 100, 200)  # estrazione bordi dal'immagine
    #cv2.imwrite(outfiles[ind][:-4] + " st3.png", im2)   #save stages

    b,g,r = cv2.split(f0)   # separazione dei canali dell'immagine
    r[h0:h1,:] = r[h0:h1,:] + (im2 * 0.2)   # sovrimpressione della matice sul canale r del'immagine originale
    #cv2.imwrite(outfiles[ind][:-4] + " st4.png", r) #save stages

    im2 = cv2.merge((b,g,r))    # ricomposizione immagine

    cv2.imwrite(outfiles[ind], im2)
    vid.release()
    print(f"Tempo di esecuzione {time()-t0:.2f} secondi")
