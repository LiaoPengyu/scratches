import os, sys

def idenCan(ms):
    f       = open("cand0.txt")
    fqTrans = open("fqTrans.txt", "w+")
    cand1   = open("cand1.txt", "w+")

    cand = [line.strip("\n") for line in f.readlines()]  # maintain candidates read from file
    firstLine, cand = map(int, cand[0].splite("\t")), cand[1:]
    assert firstLine[0] == firstLine[1] and firstLine[0] == 0
    totleLine, totleMsn = firstLine[2], firstLine[2] * ms
    cands, fqSet = [], set()

    for line in cand:
        lineItem = line.split("\t")
        if int(lineItem[-1]) >= totleMsn:
            if len(lineItem) == 2:
                fqSet.add(int(lineItem[0]))
            fqTrans.write('\t'.join(lineItem[:-1]) + '\n')
        else:
            cands.append(int(i) for i in lineItem[:-1])

    for candList in cands:
        if set(candList) - fqSet:
            continue
        else:
            cand1.write('\t'.join(map(str, candList)) + '\n')


def main():
    hpath ="/home/hadoop/hadoop/"
    n = 88162
    ms = 0.05
    p = 50000
    dpath = "/user/hadoop/tina/inputt/"
    print "dpath: "+dpath
    msn=int(n*ms)
    dpath = "/user/hadoop/lpy"
    mr_cmd0  = "dumbo start cand.py -hadoop "+hpath+" -input "+dpath+" -output /home/hadoop/lpy/fis -overwrite yes -param ms= "+str(ms)+" msn="+str(msn)+" p="+str(p)
    cat_cmd0 = "dumbo cat /home/hadoop/lpy/fis -hadoop "+hpath+" > cand0.txt"
    os.system(mr_cmd0)
    os.system(cat_cmd0)

    idenCan(ms)
    mr_cmd1  = "dumbo start fis.py -hadoop "+hpath+" -input "+dpath+" -output /home/hadoop/lpy/afis -overwrite yes  -param ms="+str(ms)+" msn="+str(msn)+" -file 'cand1.txt' -file 'fqTrans'"
    cat_cmd1 = "dumbo cat /home/hadoop/lpy/afis -hadoop "+hpath+" > fis.txt"
    os.system(mr_cmd1)
    os.system(cat_cmd1)

if __name__ == "__main__":
    main()

