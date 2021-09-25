def load_csv (nome_arq:str):
    alunos = []
    with open (nome_arq, "r") as arq:
        while True:
            line = arq.readline()

            if not line:
                break

            line = line.replace (",",".")
            vet = line.split(";")
            d = {"Nome":vet[0], "Av1":float(vet[1]), "Av2":float(vet[2])}
            alunos.append(d)

    return alunos