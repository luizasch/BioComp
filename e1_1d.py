import sys

if __name__ == '__main__':
    f = open(sys.argv[1])

    s = ''
    for line in f.readlines()[1:]:
        s += line  #pula essa linha
                   #>NC_000021.9 Homo sapiens chromosome 21, GRCh38.p7 Primary Assembly

    s = s.replace("\n","") #s contém seq do cromossomo 21

    ATCGX = {}

    for i in range(len(s)):
        ts = s[i]
        if ts in ATCGX: #se o nucleotideo já tiver sido registrado então incrementa
            ATCGX[ts] += 1
        else:
            ATCGX[ts] = 1 #senão o registra

    for key in ATCGX.keys():  #nro ocorrencias cada caractere
            print(key + ": " + str(ATCGX[key]))

    GC = ATCGX['G'] + ATCGX['C']
    print(str(GC))
    pGC = (GC / (len(s))) * 100

    print("percentual de GC: " + str(pGC) + "%")

    c = {'A', 'T', 'C', 'G'}

    print("caracteres diferentes de 'A' 'T' 'C' ou 'G': ")
    for key in ATCGX.keys():
        if key not in c:
            print(key)
