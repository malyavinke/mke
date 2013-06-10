def ParseAttributes(infname):
    f = open(infname,'r')
    attr,attrnames,tests = {},[],[]
    attrnum = int(f.readline())
    for i in xrange(attrnum):
        fWords = f.readline().split()
        attrnames.append(fWords[0]) 
        attr[fWords[0]] = [i,fWords[1],fWords[2]]
        attr[fWords[1]] = 1
        attr[fWords[2]] = 0
    num = attr[f.readline().strip()][0]
    testnum = int(f.readline())
    for i in xrange(testnum):
        fWords = f.readline().split()
        test = []
        for j in xrange(attrnum): test.append(0)
        for j in xrange(attrnum):
            attrib = fWords[j][:fWords[j].find('=')]
            value = fWords[j][fWords[j].find('=')+1:len(fWords[j])]
            test[ attr[attrib][0] ] = attr[value]
        tests.append(test)
    f.close()
    return [attrnum,attrnames,attr,tests,num]

def entropy(tests,num):
    import math
    def log2(x): return math.log(x)/math.log(2)
    neg = float(len(filter(lambda x:(x[num]==0),tests)))
    tot = float(len(tests))
    if ((neg==tot) or (neg==0)): return 0
    return -(neg/tot)*log2(neg/tot)-((tot-neg)/tot)*log2(tot-neg)

def gain(tests,attrnum,num):
    res = 0
    for i in xrange(2):
        arr = filter(lambda x:(x[attrnum]==i),tests)
        res += entropy(arr,num)*len(arr)/float(len(tests))
    return entropy(tests,num)-res

def ID3(tests,num,f,tabnum,usedattr,attrnames,attr):
    def findgains(x):
        if usedattr[x]: return 0
        return gain(tests,x,num)
    if (len(tests)==0):
        f.write('\t'*tabnum+'1')
        return
    if len(filter(lambda x:(x[num]==0),tests))>len(filter(lambda x:(x[num]==1),tests)):
        majority = '0'
    else: majority = '1'
    gains = map(findgains,xrange(len(tests[0])))
    maxgain = gains.index(max(gains))
    if (gains[maxgain]==0):
        f.write('\t'*tabnum+majority+'\n')
        return
    arrpos=filter(lambda x:(x[maxgain]==1),tests)
    arrneg=filter(lambda x:(x[maxgain]==0),tests)
    newusedattr=usedattr
    newusedattr[maxgain]=True
    f.write('\t'*tabnum+attrnames[maxgain]+'='+attr[attrnames[maxgain]][1]+'\n')
    if (len(arrpos)==0):
        f.write('\t'*(tabnum+1)+majority+'\n')
    else:
        ID3(arrpos,num,f,tabnum+1,newusedattr,attrnames,attr)
    f.write('\t'*tabnum+attrnames[maxgain]+'='+attr[attrnames[maxgain]][2]+'\n')
    if (len(arrneg)==0):
        f.write('\t'*(tabnum+1)+majority+'\n')
    else:
        ID3(arrneg,num,f,tabnum+1,newusedattr,attrnames,attr)

def applyID3(infname,outfname):
    bigarr = ParseAttributes(infname)
    attrnum,attrnames,attr,tests,num = bigarr[0],bigarr[1],bigarr[2],bigarr[3],bigarr[4]
    f = open(outfname,'w')
    usedattr=[]
    for i in xrange(attrnum): usedattr.append(i==num)
    ID3(tests,attrnum-1,f,0,usedattr,attrnames,attr)

if __name__ == '__main__':
    applyID3("infile.txt","outfname")

