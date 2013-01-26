import os
import sys
def fisCount():
    f=open("fis1.txt",'+')
    cons=f.readlines()
    f.write("\nCount: "+len(cons)+"\n\n")
    f.close()
def idenCan(ms,msn,n):
    f=open("cand0.txt")
    fw=open('cand1.txt','w')
    fis0=open('fis0.txt','w') #store frequent itemsets without identifying by once scan
    fc1=open('fc1.txt','w')
    #print >> sys.stderr,f
    contents = f.readlines()
    #print >> sys.stderr, contents
    cand=[line.strip("\n") for line in contents]# maintain candidates read from file
    fp1 = []
    cands = []
    mapcount = 0
    fisC = 0
    for line in cand:
        linei = line.split("\t")
        if len(linei)==2: # frequent 1-itemsets
            fp1.append(linei[0])
            fis0.write(linei[0]+" : "+linei[1]+"\n")
            fc1.write(linei[0]+"\n")
            fisC += 1
        elif len(linei)==3 and linei[0]==0 and line[1] == 1:
            mapcount = int(linei[2].split(",")[0])
        else:
            cands.append(linei)
            #if len(linei) == 3 and linei[0]=="8420" and linei[1]=="9479":
                #print "ok"
    #fp1.sort()

    cand=[]#clear cand
    for candi in cands:
        lc = len(candi)#the last element is "support numbers, the number of Tr, maps"
        st = ""
        for i in xrange(0, lc - 1):
            st = st + candi[i] + ","
        st = st.strip(",")
        lastE = candi[lc - 1].split(",")
        count = 0
        if int(lastE[0]) < msn:
            flag=1
            count = int(lastE[0]) + (n - int(lastE[1])) * ms * 0.9 - (mapcount - int(lastE[2]))
            if count >= msn:
                for i in xrange(0, lc - 1):
                    item = candi[i]
                    if item not in fp1:
                        flag = 0
                        break
                if flag == 1:
                    fw.write(st + "\n")
        else:
            fis0.write(st +":"+str(lastE[0])+" : msn:"+str(msn)+"\n")
            fisC += 1
    
    fis0.write("\nCount: "+str(fisC)+"\n")
    #for i in xrange(len(itemsets2)):
    #count = itemcount2[i]
    #print itemsets2[i]+"\t"+str(itemcount2[i])
    f.close()
    fw.close()
    fis0.close()
    fc1.close()

def main():
    hpath ="/home/hadoop/hadoop/"
    for i in range(1,2):
        if i==0:
            ms1 = 0.01
            n1 = 2000000
            pathc = 100
            dpath1 = "/user/hadoop/tina/inputD/t20i10d20-"
            p1=20000
        else:
            n1 = 1000000
            n1 = 88162
            ms1 = 0.05
            pathc = 50
            dpath1 = "/user/hadoop/tina/inputD/t40i20d20-"
            p1=50000
        for j in range(0,1):
            pathp = pathc * (j+1)
            dpath = dpath1 + str(pathp)+"k/"
            dpath = "/user/hadoop/tina/inputt/"
            print "dpath: "+dpath
            p = p1
            if p<5000:
                p=5000
            ms = ms1
            n = n1 * (j+1)
            msn=int(n*ms)
            dpath = "/user/hadoop/lpy"
            args="dumbo start cand.py -hadoop "+hpath+" -input "+dpath+" -output /home/hadoop/lpy/fis -param ms="+str(ms)+" msn="+str(msn)+" p="+str(p)+" -overwrite yes"
            args1 ="dumbo cat /home/hadoop/lpy/fis -hadoop "+hpath+" > cand0.txt"
            os.system(args)
            os.system(args1)
            #idenCan(ms,msn,n)
            #args3="dumbo start fis.py -hadoop "+hpath+" -input "+dpath+" -output /home/hadoop/lpy/afis -overwrite yes  -param ms="+str(ms)+" msn="+str(msn)+" -file 'cand1.txt' -file 'fc1.txt'"
            #args4 ="dumbo cat /home/hadoop/lpy/afis -hadoop "+hpath+" > fis.txt"
            #os.system(args3)
            #os.system(args4)

main()

