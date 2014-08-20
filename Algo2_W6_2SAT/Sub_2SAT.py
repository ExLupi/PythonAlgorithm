

def TestandFlip(var, clause, assign, jud):
    nclause=np.size(clause)/2
    jud = 1 # 1 means valid so far
    npass = 0
    # set the var according to the assignment
    for i in range(0,len(var)):
        if assign[i] == 0:
            aa[i] = -aa[i]

    for i in range(0,nclause):
        if (clause[i,0] in var) or (clause[i,1] in var):
            npass = npass+1
        else:
            jud = 0
            which=random.random()
            if which >= 0.5:
                assign[var.index(-clause[i,1])]
            else:
                assign[var.index(-clause[i,0])]
            break
            




# run the preprocessing program multiple times to reduce the size of clauses to the mimimum.
for i in range(0,500):
    out = []
    PreProcessing(init,out)
    init = list(out)
    #print len(init)

# write the data out
fileout = open('2sat1_processed.txt', 'w')
nn = len(init)
s = 'Final number of clauses is     '+ str(nn)+'\n'
fileout.write(s)
for i in xrange(nn):
    s = str(init[i][0])+'      '+str(init[i][1])+'\n'
    fileout.write(s)
fileout.close()

