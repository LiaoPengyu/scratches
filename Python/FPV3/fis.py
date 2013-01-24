import os
import dumbo
SEP=" "
class Mapper():
    cand=[]
    trans=[]
    supNum=[]
    def __init__(self):
        self.min_sup = self.params["ms"]

    def processTr(self,data):
        f=open("cand1.txt")
        fc1=open("fc1.txt")
        #print >> sys.stderr,f

        contents = f.readlines()
        #print >> sys.stderr, contents
        candi=[line.split("\t")[0] for line in contents]# maintain candidates read from file 
        fp1=[]
        for i in xrange(len(candi)):
            self.supNum.append(0)
            itemset=[]
            itemset0 = candi[i].split(",")
            for itm in itemset0:
                itemset.append(int(itm))
            itemset.sort()
            self.cand.append(itemset)
		    #if len(itemset)==1:
			    #fp1.append(itemset[0])
        fcontents = fc1.readlines()
        fcandi=[line.strip('\n') for line in fcontents]
        for i in xrange(len(fcandi)):
            fp1.append(int(fcandi[i]))
        fp1.sort()

        f.close()
        fc1.close()
        for docID,doc in data:
            newtr=[]
            tr=[]
            tr1 = doc.strip("\r").strip(" ").split(SEP)
            for itm in tr1:
                tr.append(int(itm))
            tr.sort()
            k=0
            lf=len(fp1)	
            for item in tr:
                i=0
                for i in xrange(k,lf):
                    item1= fp1[i]
                    if (item==item1):
                        newtr.append(item)
                        break
                    elif item<item1:
                        i=i-1
                        break
                k=i+1
                if k>lf:
                    break
            if newtr != None and  len(newtr) > 0:
                lr=len(newtr)
                for i in xrange(len(self.cand)):
                    itemset = self.cand[i]
                    li = len(itemset)
                    if li>lr:
                        continue
                    count=0
                    k=0
                    for item in itemset:
                        j=0
                        for j in xrange(k,lr):
                            item1=newtr[j]
                            if (item==item1):
                                count=count+1
                                break
                            elif item<item1:
                                j=j-1
                                break
                        k=j + 1
                        if k == lr:
                            break
                    if count==li:
                        self.supNum[i]=self.supNum[i]+1
                        #self.trans.append(newtr)

    def __call__(self,data):
        self.processTr(data)
        for i in xrange(len(self.cand)):
            yield self.cand[i], self.supNum[i]

    
#def reducer(key, values):
    #yield key, sum(values)

class Reducer():
    def __init__(self):
        self.msn =int(self.params["msn"])

    def __call__(self, key, values):
        sumv=0
        for v in values:
            sumv=sumv+v
        if sumv>=self.msn:
            yield key, sumv

if __name__ == "__main__":
    dumbo.run(Mapper, Reducer)
