import os
SEP=" "

class Mapper():
    def __init__(self):
        self.cand1   = open("cand1.txt", 'r')
        self.fqTrans = open("fqTrans.txt", 'r')

        self.transSet = (set(map(int, line.split('\t'))) for line in self.cand1.readlines())

        self.fqSet = set()
        for line in self.fqTrans.readlines():
            map(lambda x: self.fqSet.add(int(x)), line.split('\t'))

        self.cand1.close()
        self.fqTrans.close()

    def __call__(self, key, value):
        valueSet = set(map(int, value.split(SEP))) & self.fqSet

        for item in self.transSet:
            if not item - valueSet:
                yield item, 1


class Reducer():
    def __init__(self):
        pass

    def __call__(self, key, values):
        sumv = sum(values)
        yield key, sumv

class Fliter():
    def __init__(self):
        self.msn = int(self.params["msn"])

    def __call__(self, key, value):
        if int(value) >= self.msn:
            key, value

if __name__ == "__main__":
    import dumbo
    job = dumbo.Job()
    job.additer(Mapper, Reducer)
    job.additer(Fliter)
    job.run()
