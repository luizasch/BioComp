import sys

def compara(s, subs):
    carac = ''
    eq = 0
    for i in range(len(subs)): #0-13
        if s[i] == subs[i]: #compara caracteres
            eq += 1
        else:
            carac = i
    return (True, carac) if eq == 13 else (False, '')
'''se a subseq for quase idêntica ou idêntica retorna true
   e o caracter original
'''


if __name__ == '__main__':
    f = open(sys.argv[1])

    s = f.read().replace("\n","") #s contém seq do cromossomo 21

    subs = 'ACCTGGTGTTCCCA' # sequência que contém uma mutação

    for i in range(len(s)-14):
        ts = s[i:i+14]
        torf, carac = compara(ts, subs)
        if torf:
            print(ts + ' posição inicial: ' + str(i)) #imprime todos os candidatos à seq original
            print(ts[carac] + ' posição caracter original: ' + str(i + carac))
