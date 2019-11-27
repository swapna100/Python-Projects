#Write a function called ‘translate’ that,
# when given a DNA sequence of arbitrary length,the program identifies and returns the amino acid sequence of the DNA using the
# amino acid SLC code found in that table. E.g  DNA Input: ATTATTATT Output: ​III​ (representing: Isoleucine, Isoleucine, Isoleucine ​)
# There are many different amino acids, so this may get a bit repetitive. Just do the first five Amino Acids (i.e I, L, V, F M) and
# make any other codon be printed as the amino acid 'X' .
# So basically, you would use an if - elif - elif .... else structure to translate each  codon of DNA into the correct Amino Acid. 
# Note that the program must be able to handle DNA sequences that are not of a length divisible by 3

seq = ""
with open("DNA.txt","r") as f:
        seq = f.read()
        seq = seq.replace("\n","")
        seq = seq.replace("\r","")
       
def translate(seq):
    
    dict_aminoacid = {
	    'ATT' : 'I' , 'ATC' : 'I' , 'ATA' : 'I',
	    'CTT' : 'L' , 'CTC' : 'L' , 'CTA' : 'L',
	    'CTG' : 'L' , 'TTA' : 'L' , 'TTG' : 'L',
	    'GTT' : 'V' , 'GTC' : 'V' , 'GTA' : 'V', 'GTG' : 'V',
	    'TTT' : 'F' , 'TTC' : 'F' , 'GCT' : 'A' , 'GCC' : 'A' ,
	    'GCA' : 'A' , 'GCG' : 'A' , 'GGT' : 'G' , 'GGC' : 'G' , 'GGA' : 'G' , 'GGG' : 'G', 
	    'ATG' : 'M' , 'TGT' : 'C' , 'TGC' : 'C' ,
	    'ACT' : 'T' , 'ACC' : 'T' , 'ACA' : 'T'  , 'ACG': 'T'
    }

    protein = ""

    if len(seq) % 3 != 0:
        for i in range(0, len(seq),3):
          codon = seq[i:i+3]

          if codon in dict_aminoacid:
              protein  += dict_aminoacid[codon]
          else:
              continue
              
    return protein 

def txttranslate():
    return translate(seq)

txttranslate();
          
def mutate():

    aminoAcid1 = ""
    aminoAcid2 = ""
    
    with open("DNA.txt","r") as f:
        seq = f.read()
       
        pos = seq.index("a")
        print("The first occurance of a in the dna sequence is in index " + str(pos))
        
        seqA = seq.replace("a","A")
        seqT = seq.replace("a","T")
        
        amino_acid1  = translate(seqA)
        aminoAcid1 += amino_acid1
        
        amino_acid2 = translate(seqT)
        aminoAcid2 += amino_acid2
        
        f1 = open("normalDNA.txt","w+")
        f2 = open("mutatedDNA.txt","w+")
        
        f1.write(seqA + "\n\n amino acid : " + aminoAcid1)
        
        f2.write(seqT + "\n\n amino acid : " + aminoAcid2)
        
        f1.close()
        f2.close()

mutate()








 

    
    


    
