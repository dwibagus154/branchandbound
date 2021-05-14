def isiTable(table):
    jumlah = len(table)
    for i in range(jumlah):
        print("OLAHRAGA", i + 1)
        table[i][0] = input("masukkan nama olahraga = ")
        table[i][1] = int(input("masukkan waktu olahraga = "))
        table[i][2] = int(input("masukkan nilai kalori yang dihasilkan = "))
        table[i][3] = table[i][2]/table[i][1]
    return table


def urutTable(table):
    jumlah = len(table)
    for i in range(jumlah):
        for j in range(i + 1, jumlah):
            if table[j][3] > table[i][3]:
                temp = table[i]
                table[i] = table[j]
                table[j] = temp
    return table


def cost(nilaiF, nilaiK, nilaiW, nilaipw):
    return nilaiF + (nilaiK - nilaiW)*nilaipw


def branchAndBound(table):
    queue = []
    K = 60
    F = 0
    W = 0
    i = 0
    Ci = cost(F, K, W, table[i][3])
    jalur = []
    queue.append([W, F, i, Ci, jalur])

    while len(queue) != 0 and W != K:
        cut = True
        stop = False
        simpul = queue.pop(0)

        # apakah harus di block atau tidak
        while cut:
            if simpul[0] > K:
                if len(queue) != 0:
                    simpul = queue.pop(0)
                else:
                    stop = True
                    cut = False
            else:
                cut = False

        # append simpul anak
        if not cut and not stop and i < len(table) - 1:
            W = simpul[0]
            F = simpul[1]
            i = simpul[2]
            jalur = simpul[4]
            # untuk kegiatan yang di ambil
            Fambil = F + table[i][2]
            Wambil = W + table[i][1]

            i = i + 1
            Ci = cost(Fambil, K, Wambil, table[i][3])

            jalur.append(1)
            newJalur = []
            for z in range(len(jalur)):
                newJalur.append(jalur[z])
            queue.append([Wambil, Fambil, i, Ci, newJalur])

            jalur.pop()

            # untuk kegiatan yang tidak di ambil
            Ci = cost(F, K, W, table[i][3])
            jalur.append(0)
            queue.append([W, F, i, Ci, jalur])

            # urutkan queue
            queue = urutTable(queue)
    return simpul


def printHasil(simpul, table):
    print("Olahraga yang diambil adalah : ")
    for i in range(len(simpul[4])):
        if simpul[4][i] == 1:
            print(table[i][0])


def mainProgram():
    jumlah = int(input("Masukka berapa Jumlah Olahraga = "))
    table = [[0 for j in range(4)] for i in range(jumlah)]
    table = isiTable(table)
    table = urutTable(table)
    simpul = branchAndBound(table)
    printHasil(simpul, table)


mainProgram()
