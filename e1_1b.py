import sys

def palindromo(s):
    return s == s[::-1]


if __name__ == '__main__':
    f = open(sys.argv[1])
    s = f.read().replace("\n","") #s contém seq do cromossomo 21

    palindromos = {}

    for i in range(len(s)-9):
        ts = s[i:i+9]
        if palindromo(ts):
            if ts in palindromos:
                palindromos[ts] += 1
            else:
                palindromos[ts] = 1
    for key in palindromos.keys():
        print(key + ": " + str(palindromos[key]))

    print("número de palíndromos diferentes: " + str(len(palindromos))) 
