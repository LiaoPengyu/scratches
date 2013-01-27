import os, sys

def idenCan(ms):
    from itertools import combinations
    f       = open("cand0.txt")
    fqTrans = open("fqTrans.txt", "w+")
    cand1   = open("cand1.txt", "w+")

    cand = [line.strip("\n") for line in f.readlines()]  # maintain candidates read from file
    candDict = {}
    for line in cand:
        lineItem = map(int, line.split("\t"))
        if lineItem[0] == lineItem[1]:
            assert lineItem[0] == 0
            totleLine, totleBlock = lineItem[-1], lineItem[-3]
            totleMsn = totleLine * ms
        else:
            candDict.get(len(lineItem)-3, []).append(lineItem)
    candSetDict = {}
    for item in candDict[1]:
        if item[-1] < totleMsn:
            candDict[1].remove(item)
        else:
            _tmp = item[0]
            candDict[1].remove(item)
            candSetDict.get(1, set()).add((_tmp, ))
            fqTrans.write(item[0] + '\n')

    for i in candDict.keys().sort()[1:]:  #do not count candDict[1]
        for item in candDict[i]:
            if item[-2] >= totleMsn:
                fqTrans.write('\t'.join(map(str, item[:-3])) + '\n')
            elif item[-2] + (totleLine - item[-1]) * ms * 0.9 - (totleBlock - item[-3]) >= totleMsn:
                for j in range(1,i):
                    _item = item[:-3].sort()
                    if set(combinations(_item, j)) - candSetDict.get(j, set()):
                        break
                else:
                    candDict[i].append(_item)
                    candSetDict.get(i, set()).add(_item)
            candDict[i].remove(item)
    for _value in candDict.values():
        map(lambda x: cand1.write('\t'.join(x) + '\n'), _value)

    f.close()
    fqTrans.close()
    cand1.close()


def main():
    hpath ="/home/hadoop/hadoop/"
    n = 88162
    ms = 0.05
    p = 50000
    dpath = "/user/hadoop/tina/inputt/"
    print "dpath: "+dpath
    msn=int(n*ms)
    dpath = "/user/hadoop/lpy"
    mr_cmd0  = "dumbo start cand.py -hadoop "+hpath+" -input "+dpath+" -output /home/hadoop/lpy/fis -overwrite yes -param ms="+str(ms)+" msn="+str(msn)+" p="+str(p)
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
