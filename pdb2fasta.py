import sys
import os

solutionPath='./solutions/'
inputPaths='./input/'
inputFolders = os.listdir(inputPaths)
print(inputFolders) 

def convert(file_name, path):
    input_file = open(path)
    letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
           'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
           'TYR':'Y','VAL':'V'}
    prev = '-1'
    
    with open(solutionPath+file_name+'.txt', 'w') as f:
        for line in input_file:
            toks = line.split()
            if len(toks)<1: continue
            if toks[0] != 'ATOM': continue
            if toks[5] != prev:
                # print(letters[toks[3]])
                f.write('%s' % letters[toks[3]])
            prev = toks[5]

        f.write('\n')
        f.close()

for folder in inputFolders:
    x = folder+'-sup.pdb'
    path=inputPaths+folder+'/'+x
    print(path)
    # input_file = open(path)
    convert(folder,path)


# if len(sys.argv) <= 1:
#     print('usage: python pdb2fasta.py file.pdb > file.fasta')
#     exit()
    
# input_file = open(sys.argv[1])

# letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
#            'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
#            'TYR':'Y','VAL':'V'}
# print('>',sys.argv[1])
# prev = '-1'
# for line in input_file:
#     toks = line.split()
#     if len(toks)<1: continue
#     if toks[0] != 'ATOM': continue
#     if toks[5] != prev:
#         sys.stdout.write('%c' % letters[toks[3]])
#     prev = toks[5]

# sys.stdout.write('\n')
# input_file.close()