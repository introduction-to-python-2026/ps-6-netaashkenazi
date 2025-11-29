def create_codon_dict(file_path):
    file = open( file_path )
    rows = file.readlines()
    file.close()
    codon_dict = {}
    for r in rows :
       cell = r.strip().split('\t')
       key = cell[0]
       value = cell[2]
       codon_dict[key]=value
    return codon_dict



