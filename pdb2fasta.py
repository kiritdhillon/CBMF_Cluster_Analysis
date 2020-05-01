import sys
import os
import re

def convert(pdb_file, pdb_file_path, target_path):
    aa3to1={
    'ALA':'A', 'VAL':'V', 'PHE':'F', 'PRO':'P', 'MET':'M',
    'ILE':'I', 'LEU':'L', 'ASP':'D', 'GLU':'E', 'LYS':'K',
    'ARG':'R', 'SER':'S', 'THR':'T', 'TYR':'Y', 'HIS':'H',
    'CYS':'C', 'ASN':'N', 'GLN':'Q', 'TRP':'W', 'GLY':'G',
    'MSE':'M',
    }

    ca_pattern=re.compile("^ATOM\s{2,6}\d{1,5}\s{2}CA\s[\sA]([A-Z]{3})\s([\s\w])|^HETATM\s{0,4}\d{1,5}\s{2}CA\s[\sA](MSE)\s([\s\w])")

    chain_dict=dict()
    chain_list=[]

    fp=open(pdb_file_path,'rU')
    for line in fp.read().splitlines():
        if line.startswith("ENDMDL"):
            break
        match_list=ca_pattern.findall(line)
        if match_list:
            resn=match_list[0][0]+match_list[0][2]
            chain=match_list[0][1]+match_list[0][3]
            if chain in chain_dict:
                chain_dict[chain]+=aa3to1[resn]
            else:
                chain_dict[chain]=aa3to1[resn]
                chain_list.append(chain)
    fp.close()


    for chain in chain_list:
        name = os.path.join(target_path, chain+'.txt')
        with open(name, 'w') as f:
            f.write(chain_dict[chain])
        f.close()
        del f

        # sys.stdout.write('> %s\n%s\n'%(chain,chain_dict[chain]))


solutionPath='./solutions/'
inputPaths='./input/'
inputFolders = os.listdir(inputPaths)
# print(inputFolders) 

for folder in inputFolders:
    basepath = inputPaths+folder+'/'
    family_file = folder+'.ali'
    # print(basepath+family_file)
    family_file_reader = open(basepath+family_file).readline().strip('\n')
    family_name = family_file_reader[11:]
    # print(family_name)
    # print(solutionPath+family_name)
    c_dir = os.path.join (solutionPath,family_name)
    print(c_dir)
    print(os.path.isdir(c_dir))

    if os.path.isdir(c_dir):
        print("IF")
        pdb_file = folder + '-sup.pdb'
        pdb_file_path = os.path.join(basepath,pdb_file)
        target_path = c_dir
        convert(pdb_file,pdb_file_path,target_path)

    else:
        os.mkdir(c_dir) 
        pdb_file = folder + '-sup.pdb'
        pdb_file_path = os.path.join(basepath,pdb_file)
        target_path = c_dir
        convert(pdb_file,pdb_file_path,target_path)

