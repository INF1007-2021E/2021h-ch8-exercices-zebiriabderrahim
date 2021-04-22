#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def  compare_le_contenu(path1,path2):
    with open(path1, 'r') as f1,open(path2, 'r') as f2:
            line2 = f1.readline()
            for line1 in f2:
                if line1!=line2:
                        print(line2)
                        print(line1)
                        break
def exo2(path1,rpath):
    with open(path1, 'r') as f1,open(rpath, 'w') as f2:
        for line in f1.readlines():
            line=line.replace(' ','  ')
            f2.write(line)

def exo3(path2,rpath):
    with open(path2, 'r') as f1, open(rpath, 'w') as f2:
     for line in f1.readlines():
        for k,v in PERCENTAGE_TO_LETTER.items():
                if v[1] >= int(line.strip()) >= v[0]:
                    f2.write(f"{int(line.strip())} {k} \n")
                    break

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    path1 = "./notes_letter.txt"
    path2 = "./notes.txt"
    rpath = "./exemplec.txt"
    compare_le_contenu(path1,rpath)
    exo3(path2,rpath)
