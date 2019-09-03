import sys

if __name__ == '__main__':
    f = open(sys.argv[1])
    s = f.read().replace("\n","") #s contém seq do cromossomo 21

    sequencia37 = {}

    for i in range(len(s)-37):
        ts = s[i:i+37]
        if ts in sequencia37:
            sequencia37[ts] += 1
        else:
            sequencia37[ts] = 1
    for key in sequencia37.keys():
        print(key + ": " + str(sequencia37[key]))

    print("número de sequências diferentes: " + str(len(sequencia37)))
