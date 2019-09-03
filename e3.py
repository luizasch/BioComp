
def smithWatermanCreate(seq1, seq2):
    #inicializa a matriz
    mat = [[0]*(len(seq2)+1) for _ in range(len(seq1)+1)]

    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            match = mat[i-1][j-1] + (1 if seq1[i-1] == seq2[j-1] else -1)
            delete = mat[i-1][j] - 2
            insert = mat[i][j-1] - 2
            mat[i][j] = max(match, insert, delete, 0)

    return mat

def biggerIndex(matrix):
    biggerI = -1
    biggerJ = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] >= matrix[biggerI][biggerJ]:
                biggerI = i
                biggerJ = j
    return biggerI, biggerJ

def smithWatermanBacktrack(matrix, seq1, seq2):
    aseq1 = ''
    aseq2 = ''
    i,j = biggerIndex(matrix)
    score = 0

    while matrix[i][j] != 0:
        match = mat[i-1][j-1] + (1 if seq1[i-1] == seq2[j-1] else -1)
        delete = mat[i-1][j] - 2
        insert = mat[i][j-1] - 2

        cur = mat[i][j]

        if insert == cur:
            aseq1 += '-'
            aseq2 += seq2[j-1]
            j = j-1
            score +=  -2
        elif delete == cur:
            aseq1 += seq1[i-1]
            aseq2 += '-'
            i = i-1
            score += -2
        elif match == cur:
            aseq1 += seq1[i-1]
            aseq2 += seq2[j-1]
            score += (1 if seq1[i-1] == seq2[j-1] else -1)
            i = i-1
            j = j-1
    return aseq1[::-1], aseq2[::-1], score

def identidade(str1, str2):
    cont = 0
    total = len(str1)
    for i in range(total):
        if str1[i] == str2[i]:
            cont += 1

    return (cont/total)*100

urea = "MKLSPREVEKLGLHNAGYLAQKRLARGVRLNYTEAVALIASQIMEYARDGEKTVAQLMCLGQHLLGRRQVLPAVPHLLNAVQVEATFPDGTKLVTVHDPISRENGELQEALFGSLLPVPSLDKFAETKEDNRIPGEILCEDECLTLNIGRKAVILKVTSKGDRPIQVGSHYHFIEVNPYLTFDRRKAYGMRLNIAAGTAVRFEPGDCKSVTLVSIEGNKVIRGGNAIADGPVNETNLEAAMHAVRSKGFGHEEEKDASEGFTKEDPNCPFNTFIHRKEYANKYGPTTGDKIRLGDTNLLAEIEKDYALYGDECVFGGGKVIRDGMGQSCGHPPAISLDTVITNAVIIDYTGIIKADIGIKDGLIASIGKAGNPDIMNGVFSNMIIGANTEVIAGEGLIVTAGAIDCHVHYICPQLVYEAISSGITTLVGGGTGPAAGTRATTCTPSPTQMRLMLQSTDDLPLNFGFTGKGSSSKPDELHEIIKAGAMGLKLHEDWGSTPAAIDNCLTIAEHHDIQINIHTDTLNEAGFVEHSIAAFKGRTIHTYHSEGAGGGHAPDIIKVCGIKNVLPSSTNPTRPLTSNTIDEHLDMLMVCHHLDREIPEDLAFAHSRIRKKTIAAEDVLNDIGAISIISSDSQAMGRVGEVISRTWQTADKMKAQTGPLKCDSSDNDNFRIRRYIAKYTINPAIANGFSQYVGSVEVGKLADLVMWKPSFFGTKPEMVIKGGMVAWADIGDPNASIPTPEPVKMRPMYGTLGKAGGALSIAFVSKAALDQRVNVLYGLNKRVEAVSNVRKLTKLDMKLNDALPEITVDPESYTVKADGKLLCVSEATTVPLSRNYFLF"
ure1 = "MSNISRQAYADMFGPTVGDKVRLADTELWIEVEDDLTTYGEEVKFGGGKVIRDGMGQGQMLAADCVDLVLTNALIVDHWGIVKADIGVKDGRIFAIGKAGNPDIQPNVTIPIGAATEVIAAEGKIVTAGGIDTHIHWICPQQAEEALVSGVTTMVGGGTGPAAGTHATTCTPGPWYISRMLQAADSLPVNIGLLGKGNVSQPDALREQVAAGVIGLKIHEDWGATPAAIDCALTVADEMDIQVALHSDTLNESGFVEDTLAAIGGRTIHTFHTEGAGGGHAPDIITACAHPNILPSSTNPTLPYTLNTIDEHLDMLMVCHHLDPDIAEDVAFAESRIRRETIAAEDVLHDLGAFSLTSSDSQAMGRVGEVILRTWQVAHRMKVQRGALAEETGDNDNFRVKRYIAKYTINPALTHGIAHEVGSIEVGKLADLVVWSPAFFGVKPATVIKGGMIAIAPMGDINASIPTPQPVHYRPMFGALGSARHHCRLTFLSQAAAANGVAERLNLRSAIAVVKGCRTVQKADMVHNSLQPNITVDAQTYEVRVDGELITSEPADVLPMAQRYFLF"
ure2 = "MIPGEYHVKPGQIALNTGRATCRVVVENHGDRPIQVGSHYHFAEVNPALKFDRQQAAGYRLNIPAGTAVRFEPGQKREVELVAFAGHRAVFGFRGEVMGPLEVNDE"
ure3 = "MELTPREKDKLLLFTAALVAERRLARGLKLNYPESVALISAFIMEGARDGKSVASLMEEGRHVLTREQVMEGVPEMIPDIQVEATFPDGSKLVTVHNPII"

ureas = { "urea": urea, "ure1": ure1, "ure2": ure2, "ure3": ure3}

seq2 = ureas[input()]
seq1 = ureas[input()]
mat = smithWatermanCreate(seq1, seq2)
for linha in mat:
	print(linha) #imprime matriz
aseq1, aseq2, score = smithWatermanBacktrack(mat, seq1, seq2)
print(aseq1)
print()
print(aseq2)
print() #imprime sequencias alinhadas
print("score: " + str(score))
print("identidade: " + str(identidade(aseq1, aseq2)) + "%")
