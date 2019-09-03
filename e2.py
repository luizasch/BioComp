

def needlemanWunschCreate(seq1, seq2):
    #inicializa a matriz
    mat = []
    mat.append([x*-4 for x in range(len(seq2)+1)])
    mat.extend([[(x+1)*-4] + ([0]*len(seq2)) for x in range(len(seq1))])

    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            match = mat[i-1][j-1] + (5 if seq1[i-1] == seq2[j-1] else -3)
            delete = mat[i-1][j] - 4
            insert = mat[i][j-1] - 4
            mat[i][j] = max(match, insert, delete)
					
    return mat



def needlemanWunschBacktrack(matrix, seq1, seq2):
    aseq1 = ''
    aseq2 = ''
    i = len(seq1)
    j = len(seq2)
    score = 0

    while i != 0 and j != 0:
        match = mat[i-1][j-1] + (5 if seq1[i-1] == seq2[j-1] else -3)
        delete = mat[i-1][j] - 4
        insert = mat[i][j-1] - 4

        cur = mat[i][j]
        
        if insert == cur:
            aseq1 += '-'
            aseq2 += seq2[j-1]
            j = j-1
            score += -4
        elif delete == cur:
            aseq1 += seq1[i-1]
            aseq2 += '-'
            i = i-1
            score += -4
        elif match == cur:
            aseq1 += seq1[i-1]
            aseq2 += seq2[j-1]
            score += (5 if seq1[i-1] == seq2[j-1] else -3)
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
	
	
human = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR"
horse = "MVLSAADKTNVKAAWSKVGGHAGEYGAEALERMFLGFPTTKTYFPHFDLSHGSAQVKAHGKKVGDALTLAVGHLDDLPGALSNLSDLHAHKLRVDPVNFKLLSHCLLSTLAVHLPNDFTPAVHASLDKFLSSVSTVLTSKYR"
deer = "VLSAABKSBVKAAWGKVGGNAAPYGAZALZRMFLSFPTTKTYFPHFBLSHGSAZVKAHGZKVABALTKAVGHLBBLPGTLSBLSBLHAHKLRVBPVBFKLLSHSLLVTLATHLPBBFTPAVHASLBKFLABVSTVLTSKYR"
cow = "MVLSAADKGNVKAAWGKVGGHAAEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGAKVAAALTKAVEHLDDLPGALSELSDLHAHKLRVDPVNFKLLSHSLLVTLASHLPSDFTPAVHASLDKFLANVSTVLTSKYR"	
pig = "VLSAADKANVKAAWGKVGGQAGAHGAEALERMFLGFPTTKTYFPHFNLSHGSDQVKAHGQKVADALTKAVGHLDDLPGALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHHPDDFNPSVHASLDKFLANVSTVLTSKYR"
maned_wolf = "VLSPADKTNIKSTWDKIGGHAGDYGGEALDRTFQSFPTTKTYFPHFDLSPGSAQVKAHGKKVADALTTAVAHLDDLPGALSALSDLHAYKLRVDPVNFKLLSHCLLVTLACHHPTEFTPAVHASLDKFFTAVSTVLTSKYR"
chicken = "MLTAEDKKLIQQAWEKAASHQEEFGAEALTRMFTTYPQTKTYFPHFDLSPGSDQVRGHGKKVLGALGNAVKNVDNLSQAMAELSNLHAYNLRVDPVNFKLLSQCIQVVLAVHMGKDYTPEVHAAFDKFLSAVSAVLAEKYR"
trout = "SLTAKDKSVVKAFWGKISGKADVVGAEALGRDKMLTAYPQTKTYFSHWADLSPGSGPVKKHGGIIMGAIGKAVGLMDDLVGGMSALSDLHAFKLRVDPGNFKILSHNILVTLAIHFPSDFTPEVHIAVDKFLAAVSAALADKYR"	
species = {"human": human, "horse": horse, "deer": deer, "cow": cow, "pig": pig, "maned wolf": maned_wolf, "chicken": chicken, "trout": trout}
 
seq1 = species[input()]
seq2 = species[input()]
mat = needlemanWunschCreate(seq1, seq2)
for linha in mat:  
	print(linha) #imprime matriz
aseq1, aseq2, score = needlemanWunschBacktrack(mat, seq1, seq2)
print(aseq1)
print(aseq2) 
print() #imprime sequencias alinhadas
print("score: " + str(score))
print("identidade: " + str(identidade(aseq1, aseq2)) + "%")
print()
print()