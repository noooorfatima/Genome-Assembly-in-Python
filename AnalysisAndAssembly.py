"""

The functions used to implement Lab 8 should be written here.
As usual, you'll need to include a test suite as well as your well-commented
functions.  In addition, you'll need to find any necessary code for doctest to
work (see past assignments) and import any needed libraries yourself.  After all,
other than this comment and a few tests below, this is a blank file!

A sample test for part 1 of the lab:
>>> dotMatrix("hello", "jello")
array([[0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 1, 0],
       [0, 0, 1, 1, 0],
       [0, 0, 0, 0, 1]])
       
A sample test for part 2 of the lab.  The dictionary output order is not
guaranteed, so we test equality instead of directly testing the dictionary.
>>> aminoAcids("tttttttggaga") == {'R': 1, 'W': 1, 'F': 2}
True
       
A sample test for part 3 of the lab, run on a small set of test fragments.
The final function should be able to run on the full set of fragments available
in GenomeLib.getFragments().
>>> putFragmentsTogether(GenomeLib.getTestFragments())
'ttttttggagacgcggg'

#sample tests for part 1
>>> dotMatrix("ttttt", "ttgg") #few overlaps example
array([[1, 1, 0, 0],
       [1, 1, 0, 0],
       [1, 1, 0, 0],
       [1, 1, 0, 0],
       [1, 1, 0, 0]])
>>> dotMatrix("ttttt", "gggg") #no overlap example
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]])
>>> dotMatrix("tgg", "tgg") #full overlap
array([[1, 0, 0],
       [0, 1, 1],
       [0, 1, 1]])
>>> dotMatrix("   ", "  ") #strings with spaces
array([[1, 1],
       [1, 1],
       [1, 1]])
>>> dotMatrix("ttggcc", "tgg")
array([[1, 0, 0],
       [1, 0, 0],
       [0, 1, 1],
       [0, 1, 1],
       [0, 0, 0],
       [0, 0, 0]])
       
#sample tests for part 2
>>> aminoAcids("ttaattatgatg") == {'L': 1, 'I': 1, 'M': 2}
True
>>> aminoAcids("ccgacg")=={'L': 1}
False
>>> aminoAcids("ctcctc")=={'L':2}
True
>>> aminoAcids("aacttcttt")=={'N':1, 'F':2}
True
>>> aminoAcids("ggagggggcggt")=={'G':4}
True
>>> aminoAcids("ttgggt")=={'L':1, 'G':2}
False

#sample tests for part 3

>>> putFragmentsTogether(['tttttt', 'ttttgg',  'agacgc','tggaga', 'bgcggg'])
'ttttttggagacgcbgcggg'
>>> putFragmentsTogether(['tttttt', 'ttttgg', 'tggaga', 'agacgc', 'cgcggg'])
'ttttttggagacgcggg'
>>> putFragmentsTogether(['tttggg','tgggac','acggca','caggga'])
'tttgggacggcaggga'
>>> putFragmentsTogether(['tttggg','','aaaggg'])
'tttgggaaaggg'
>>> putFragmentsTogether(['tttttt', 'ttttgg', 'agacgc', 'tggaga', 'cgcggg'])
'ttttttggagacgcggg'
>>> putFragmentsTogether(['tttttt', 'tggg', 'ttgaga',''])
'ttttttgagatggg'
>>> putFragmentsTogether(['hellow', 'world', 'whats','sup'])
'hellowhatsupworld'

# >>> len(putFragmentsTogether(GenomeLib.getFragments())) #ran this to see if it works and how much time it takes(almost 2 mins)
# 2#just a random integer


"""
import numpy as np #importing libraries

import GenomeLib 


    

def dotMatrix(seq1,seq2):
    #precond: both inputs are strings
    a =np.zeros([len(seq1),len(seq2)], dtype=int) #initiating a 0 matrix and its dimensions
    for s1 in range(len(seq1)): #for loop to or through first sequence 
        for s2 in range(len(seq2)): #for loop to go through second sequence
            if seq1[s1]==seq2[s2]: #checking the same elements
                a[s1][s2]=1 #if similar, puts 1 in the matrix
            else:
                a[s1][s2]=0 #else 0 if no similarity
            #postcond:returns a matrix made from arrays
    return a #returns the dormatrix, that shows similarities


def aminoAcids(seq): #translates amino acids to the abbreviations
    #precond:input has to be a string
    value ="" #initializing the value 
    if len(seq)%3 == 0: #the amino acid string must be divisible by three because bio but even if we comment it out wouldn't matter for this code
        for i in range(0, len(seq), 3): #goes through the sequence and the three letter acids in it
            codon = seq[i:i + 3] #defiing what codon is 
            value=value+ GenomeLib.getAminoAcidsDict()[codon] #this value will be  all the abbreviaitions
            dict = {} #forming a dictionary for the values
            for letter in value: #for loop for filling the dictionary with the value and the amounts of values
                dict[letter] = dict.get(letter, 0) + 1 
                #postcond:returns a dictionary with letters corresponding to sequence acids and their frequency
        return dict


def putFragmentsTogether(list): #puts frags together, with max overlap starting from he first in the list
    #precod:takes a list of sequences or any string would work
    head=list[0] #defining head
    newlist=list #defining newlist,not necessary but better for my understanding
     
    while len(newlist)>1: #while loop that checks if a final fragment has been created
        maxoverlap=0 #keeps a check on the overlap length
        string=newlist[1] #initializng a string that keeps track of elements that need to be joined 
        for j in range(len(newlist)-1): #going through all other elements except the head  
            for i in range(len(head)): #goes through head to see where overlap starts 
                if head[i:]==newlist[j+1][:len(head)-i]: #if there is an overlap 
                    if maxoverlap <=len(head[i:]): #starts checking max overlap
                        maxoverlap=len(head[i:]) #changes max overlap value, loop is making progress
                        string=newlist[j+1] #string is also changing
        head=head+string[maxoverlap:] #redifines haead
        newlist[0]=head #the list has first element as the new long string made from overlaps
        newlist.remove(string) #it removes what aever overlapped and is the part of new string
         #precond;returns the max overlap string
    return newlist[0] #returns the long fragment






def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()



