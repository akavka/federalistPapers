"""
Adam Kavka and Levi Melnick
December 2014

I'm sorry this file is so long. If I had to do it over again I would break this into smaller files.

This file contains the bulk of our Federalist paper project. It does many things.

It contains the list of function words.
It divides the monolithic Federalist Paper text file into individual files (one for each Paper)
It converts documents to bags of words
Divides the "other writings" of Madison and Hamilton into individual documents.
It puts bag-of-words dictionaries into the text-matrix format our SVM needs
It can look at a training set of documents and get the tf-idf features for them, outputting in the format needed for SVM
It can write the feature-matrix to disk files
with all these functions, it can iterate over the undisputed (training) documents, or the disputed (test) documents.


"""


#!/usr/bin/python
import pickle
import os.path
import string
from gensim import corpora, models, similarities
#enumerations to keep the classes consistent
hamiltonClass=-1
madisonClass=1

#this is a list of what that one paper called the 'function words'

"""
def getFunctionList():
    l=["upon", "would"]
    return l

"""
def getFunctionList():
    l = ["a","all","also", "an","and","any","are","as","at","be","been","but","by","can","do","down","even","every","for","from","had","has","have","her","his","if","in","into","is","it","its","may","more","must","my","no","not","now","of","on","one","only","or","our","shall","should","so","some","such","than","that","the","their","then","there", "things","this","to","up","upon","was","were","what","when","which","who","will","with","would","your"]
    return l

#takes list of words, turns into dictionary of (word,0) tuples for counting
#if we use the function list of the above function, they happen to be sorted by word
def makeCounter(l):
    counter={}
    for word in l:
        counter[word]=0
    return counter

#this takes a list and removes the words 'the' 'of' and 'to' (because they're at the top of many pages as they're published, but not in the body of text)
def removeWords(l,words=["the","of","to"]):
    for word in words:
        if (word in l):
            l.remove(word)
    return l
    
#this paper parsed the federalist paper document we had and divided it into many documents
def divideFederalistPapers():

    #the pickling is kinda deprecated
    import pickle

    #where we write the files
    dirname="fedPapersDir"
    filename="fedPapers"

#the input file
    f=open("FederalistPapersFullText.txt")
    paperCount=0;

    #there's junk at beginning of the file; read it and store it here
    outFile=open(dirname+"/" + filename + "junk", "w")

    lines= f.readlines()

    for i in range(0, len(lines)):
  
        line=lines[i]
        words=line.split();

        #Check for our delimiter
        if len(words)>=2 and words[0]=="FEDERALIST" and words[1]=="No.":
        
        #we're starting a new paper if we see the delimter
            paperCount+=1 
            outFile.close()
            outFile=open(dirname+"/"+filename+ str(paperCount), "w")
           
            #end if

        outFile.write(line)


#This function takes a text file as input and outputs a list of (value,wordCount) pairs, sorted by value.
#no dictionary here...it outputs every word
#It can write results to text or pickle file...but that's kinda deprecated.
#There are bugs galore as of 10/28; I'll be working on them.
def wordCount(inputFile="FederalistPapersFullText.txt", outputText="FederalistPapersWordCountText.txt", outputPickle="FederalistPapersWordCountPickle.pk", functionWordList=0):


    f=open(inputFile, "r")
    lines= f.readlines()
    i=0
    if functionWordList==0:
        functionWordList=getFunctionList()
    counter={}#dictionary type
    for line in lines:
        line=line.rstrip();
        words=line.split();
        i+=1
        for word in words:
            word=word.rstrip(string.punctuation)
            word=word.lstrip(string.punctuation)
            word = word.lower()

            if word in counter:
                counter[word]+=1
            else:
                counter[word]=1

            
    l=[]

    wordCountText=open(outputText, "w")
    

    #conver
     #From this site:
     #http://stackoverflow.com/questions/9001509/python-dictionary-sort-by-key
    for k in sorted(counter.keys()):
        l.append((k,counter[k]))
    l=sorted(l)
    returnD={}
    for i in range(len(l)):
        returnD[l[i][0]]=i

    return returnD

    for tup in l:
        print tup
        wordCountText.write(str(tup)+'\n')

    

    wordCountPickle=open(outputPickle, "w")
    pickle.dump(l, wordCountPickle)
    wordCountPickle.close()
    wordCountText.close()
    f.close()
    return l


#This function takes several hard-coded text files as  input and outputs a list of (value,wordCount) pairs, sorted by value.

#It can write results to text or pickle file...but that's kinda deprecated.

def wordCountFull(inputFile="FederalistPapersFullText.txt", outputText="FederalistPapersWordCountText.txt", outputPickle="FederalistPapersWordCountPickle.pk", functionWordList=0):


    f=open(inputFile, "r")
    lines= f.readlines()
    f.close()
    f=open("JamesMadisonFullTextTwo.txt")
    lines = lines + f.readlines()
    f.close()

    f=open("AlexanderHamiltonFullText.txt")
    lines = lines + f.readlines()
    f.close()
    i=0
    if functionWordList==0:
        functionWordList=getFunctionList()
    counter={}#dictionary type
    for line in lines:
        line=line.rstrip();
        words=line.split();
        i+=1
        for word in words:
            word=word.rstrip(string.punctuation)
            word=word.lstrip(string.punctuation)
            word = word.lower()

            if word in counter:
                counter[word]+=1
            else:
                counter[word]=1

            
    l=[]

    wordCountText=open(outputText, "w")
    

    #conver
     #From this site:
     #http://stackoverflow.com/questions/9001509/python-dictionary-sort-by-key
    for k in sorted(counter.keys()):
        l.append((k,counter[k]))
    l=sorted(l)
    returnD={}
    for i in range(len(l)):
        returnD[l[i][0]]=i

    return returnD

    for tup in l:
        print tup
        wordCountText.write(str(tup)+'\n')

    

    wordCountPickle=open(outputPickle, "w")
    pickle.dump(l, wordCountPickle)
    wordCountPickle.close()
    wordCountText.close()
    f.close()
    return l


def wordCountHalf(inputFile="FederalistPapersFullText.txt", outputText="FederalistPapersWordCountText.txt", outputPickle="FederalistPapersWordCountPickle.pk", functionWordList=0):


    f=open("JamesMadisonFullTextTwo.txt")
    lines = f.readlines()
    f.close()

    f=open("AlexanderHamiltonFullText.txt")
    lines = lines + f.readlines()
    f.close()
    i=0
    if functionWordList==0:
        functionWordList=getFunctionList()
    counter={}#dictionary type
    for line in lines:
        line=line.rstrip();
        words=line.split();
        i+=1
        for word in words:
            word=word.rstrip(string.punctuation)
            word=word.lstrip(string.punctuation)
            word = word.lower()

            if word in counter:
                counter[word]+=1
            else:
                counter[word]=1

            
    l=[]

    wordCountText=open(outputText, "w")
    

    #conver
     #From this site:
     #http://stackoverflow.com/questions/9001509/python-dictionary-sort-by-key
    for k in sorted(counter.keys()):
        l.append((k,counter[k]))
    l=sorted(l)
    returnD={}
    for i in range(len(l)):
        returnD[l[i][0]]=i

    return returnD

    for tup in l:
        print tup
        wordCountText.write(str(tup)+'\n')

    

    wordCountPickle=open(outputPickle, "w")
    pickle.dump(l, wordCountPickle)
    wordCountPickle.close()
    wordCountText.close()
    f.close()
    return l



def getBagForDocument(inputFile, inCounter):
    f=open(inputFile, "r")
    lines= f.readlines()
    i=0

    counter={}#dictionary type
    stopWords=getFunctionList()
    
    for line in lines:
        if (lineIsOkay(line)):
            line=line.rstrip();
            words=line.split();
            i+=1
            for word in words:
                
                word=word.rstrip(string.punctuation)
                word=word.lstrip(string.punctuation)
                word = word.lower()
            
                if word in inCounter:
        
                    #               if (word in counter):              
                    if (word in counter):
                        counter[word]+=1
                #else:
                    elif (wordIsOkay(word)):
                        counter[word]=1
                
    l=[]
    for k in counter.keys():
        l.append((inCounter[k], counter[k]))
        
    l=sorted(l)
    #print l
    return l


#This function takes a text file and dictionary as input and outputs a list of (value,wordCount) pairs, sorted by value.
#It can write results to text or pickle file...but that's kinda deprecated.
#There are bugs galore as of 10/28; I'll be working on them.
def wordCountDictionary(inputFile="FederalistPapersFullText.txt",  functionWordList=0):


    f=open(inputFile, "r")
    lines= f.readlines()
    i=0
    totalWords=0

    if functionWordList==0:
        functionWordList=getFunctionList()
    counter=makeCounter(functionWordList)#dictionary type
    
    #Look through each line, split line into words, chop punctuation from end of words
    for line in lines:
        line=line.rstrip();
        words=line.split();
        i+=1
        for word in words:
            word=word.rstrip(string.punctuation)
            word=word.lstrip(string.punctuation)
            word=word.lower() 

            totalWords+=1
            if word in counter:
                counter[word]+=1
       

    l=[]


    #convert from dictionary to sorted list
     #From this site:
     #http://stackoverflow.com/questions/9001509/python-dictionary-sort-by-key
    for k in sorted(counter.keys()):

        #not only do we add to list, we also normalize the counts by dividing by the total number of words
        l.append((k, float(counter[k])/float(totalWords)))
    l=sorted(l)
    f.close()
    return l


#This function splits up James Madison's papers into separate files.
#Takes a text input file and outputs many text files in a single directory
#it uses "TO " as a delimiter, since that starts letters (but not every document is a letter)
def splitMadisonPapers(fullFilesNames=["JamesMadisonFullTextTwo.txt"], outputDir="madisonPapersDir", outputFileName="madisonPaper"):
 
#indexing starts at 1 to match federalist papeers
    paperCount=1
    for fileName in fullFilesNames:
        
#main file for reading
        f=open(fileName, "r")
        
        #junk at beginning of file will always be output to junk file
        outputFile=open(outputDir + "/" + outputFileName +  "junk", "w")
        lines=f.readlines()
        i=0

        #scan past the introductory text
        while(lines[i][0:4]!="MY D"):
            i+=1

        #iterate through the lines now that we're in the actual writings
        while i<len(lines):
            if (lines[i][0:3]=="TO "):
                
             #start new output file
                outputFile.close()
                
                outputFile=open(outputDir + "/" + outputFileName +  str(paperCount), "w")
                paperCount+=1
            outputFile.write(lines[i])
            i+=1



#Takes all of Hamilton's work as a single text document as input and divides them into several texts in a single directory.
#The first document is a fraction of a long essay; that's hardcoded.
#Afterward automatically delimits on "TO "
def splitHamiltonPapers(fullFilesNames=["AlexanderHamiltonFullText.txt"], outputDir="hamiltonPapersDir", outputFileName="hamiltonPaper"):
 
    paperCount=1
    for fileName in fullFilesNames:
        
#main file for reading
        f=open(fileName, "r")
        
        #junk at beginning of file will always be output to file 0
        outputFile=open(outputDir + "/" + outputFileName +  "junk", "w")
        lines=f.readlines()
        i=0


        #scan past the introductory text
        while(lines[i][0:7]!="DEFENCE"):
            i+=1

        outputFile.close()
        outputFile=open(outputDir + "/" + outputFileName +  str(paperCount), "w")
        #read the miscellaneous paper at the beginning of the file.
        while(lines[i][0:5]!="TO ED"):
            outputFile.write(lines[i])
            i+=1

        #iterate through the lines of the private correspondence
        while i<len(lines):

            #Assume "TO " is the start of a new letter
            if (lines[i][0:3]=="TO "):
                
             #start new output file
                outputFile.close()
                paperCount+=1
                outputFile=open(outputDir + "/" + outputFileName +  str(paperCount), "w")
            outputFile.write(lines[i])
            i+=1

#This method returns a list of lists: The first list is a document. The second list is the vector of numbers wordCountDictionary() produced for that document.
def getTrainingMatrix(trainingSet=["hamiltonPapersDir/hamiltonPaper","madisonPapersDir/madisonPaper"]):

    matrix=[]
    
    #assumes Hamilton is -1; Madison is 1
    #loop through Hamilton first, then loop through Madison
    dataClass=hamiltonClass
    for classPath in trainingSet:
        
        #iterate until we've done all of the files
        i=1
        while(os.path.isfile(classPath+str(i))):
            
            #get that file's feature list, then add it to matrix
            l=wordCountDictionary(classPath+str(i),getFunctionList())
            featureList=[dataClass]
            for pair in l:
                featureList.append(pair[1])
            if i>1:
                matrix.append(featureList)
            i+=1
        
            
        #change the class label
        dataClass+=madisonClass - hamiltonClass
    return matrix



### LM ADDED: 11/30/2014 ###
#This method returns a list of lists: The first list is a document. The second list is the vector of numbers wordCountDictionary() produced for that document.
def getStretchMatrix(trainingSet=["trainNonFedDir/hamilton/","trainNonFedDir/madison/"]):

    #print(os.listdir(trainingSet[0]))
    hamiltonfiles = [trainingSet[0] + hf for hf in os.listdir(trainingSet[0])]
    madisonfiles = [trainingSet[1] + mf for mf in os.listdir(trainingSet[1])]
    matrix=[]

    dataClass=hamiltonClass
    for hf in hamiltonfiles:
        
        l=wordCountDictionary(hf, getFunctionList())
        featureList=[dataClass]
        
        for pair in l:
            featureList.append(pair[1])
        matrix.append(featureList)
            
    dataClass=madisonClass
    for mf in madisonfiles:
        l=wordCountDictionary(mf, getFunctionList())
        featureList=[dataClass]
        
        for pair in l:
            featureList.append(pair[1])
        matrix.append(featureList)

    return matrix



#This function reads all of the papers undisputedly attributed to hamilton and Madison and turns them into a list of feature-lists
# The output can easily be written to a training file with writeMatrixToFile
def getUndisputedFederalistMatrix(testSet=["fedPapersDir/fedPapers"]):

    matrix=[]
    
    #assumes Hamilton is -1; Madison is 1, only grabs those two's unambiguous papers.
   
    for classPath in testSet:
        
        #iterate until we've done all of the files
        i=1
        while(os.path.isfile(classPath+str(i))):


#            l=wordCountDictionary(classPath+str(i), "don'tCare.txt", "don'tCare2.txt", removeWords(getFunctionList()))

            #get features (just the numbers) of the document, then add them to our matrix. use a different class for the different authors
            l=wordCountDictionary(classPath+str(i), getFunctionList())
            if (hamiltonNumbers.count(i)==1):
                featureList=[hamiltonClass]
                for pair in l:
                    featureList.append(pair[1])
                matrix.append(featureList)

            elif (madisonNumbers.count(i)==1):
                featureList=[madisonClass]
                for pair in l:
                    featureList.append(pair[1])
                matrix.append(featureList)


            i+=1
            

    return matrix



#This function reads all of the papers that are disputed and turns them into a list of feature-lists
# The output can easily be written to a training file with writeMatrixToFile
def getDisputedFederalistMatrix(testSet=["fedPapersDir/fedPapers"]):

    matrix=[]
    
    #assumes Hamilton is -1; Madison is 1, only grabs those two's unambiguous papers.
   
    for classPath in testSet:
        
        #iterate until we've done all of the files
        i=1
        while(os.path.isfile(classPath+str(i))):


#            l=wordCountDictionary(classPath+str(i), "don'tCare.txt", "don'tCare2.txt", removeWords(getFunctionList()))

            #get feature list
            l=wordCountDictionary(classPath+str(i), getFunctionList())
        
            #only read the disputed ones.
            if (disputedNumbers.count(i)==1):
                


                #Mark Madison as correct class, consistent with historical analysis
                featureList=[1]
                
                #make list and append it to our matrix.
                for pair in l:
                    featureList.append(pair[1])
                matrix.append(featureList)


            i+=1
            

    return matrix





#This function reads all of the papers undisputedly attributed to hamilton and Madison and returns the TFIDF features of each.
def getUndisputedTFIDF(testSet=["fedPapersDir/fedPapers"]):

    matrix=[]
    matrix2=[]
    
    #assumes Hamilton is -1; Madison is 1, only grabs those two's unambiguous papers.
    corpus=[]
    trainCorpus=[]
    for classPath in testSet:
        
        #iterate until we've done all of the files
        i=1
        d= wordCount()
        print len(d)
        while(os.path.isfile(classPath+str(i))):
            


            l=getBagForDocument(classPath+str(i), d)
            corpus.append(l)

            if (i in hamiltonNumbers) or (i in madisonNumbers):
                
                trainCorpus.append(l)
            


            i+=1
        tfidf=models.TfidfModel(trainCorpus)
        i=1
        while(os.path.isfile(classPath+str(i))):
            l=tfidf[corpus[i-1]]
            if (hamiltonNumbers.count(i)==1):
                featureList=[hamiltonClass]
                for pair in l:
                    featureList.append(pair)
                matrix.append(featureList)

            elif (madisonNumbers.count(i)==1):
                featureList=[madisonClass]
                for pair in l:
                    featureList.append(pair)
                matrix.append(featureList)

            
            elif (disputedNumbers.count(i)==1):
                featureList=[madisonClass]
                for pair in l:
                    featureList.append(pair)
                matrix2.append(featureList)

            i+=1
    
    return (matrix, matrix2)







#This function reads all of the other writings of hamilton and Madison and returns the TFIDF features of each.
def getMixedTFIDF(trainingSet=["trainNonFedDir/hamilton/","trainNonFedDir/madison/"]):


    corpus=[]
    trainCorpus=[]
    tags=[]
    d=wordCountFull()
#print(os.listdir(trainingSet[0]))
    hamiltonfiles = [trainingSet[0] + hf for hf in os.listdir(trainingSet[0])]
    madisonfiles = [trainingSet[1] + mf for mf in os.listdir(trainingSet[1])]
    matrix=[]

    dataClass=hamiltonClass
    i=2
    while(os.path.isfile("hamiltonPapersDir/hamiltonPaper"+str(i))):
        hf="hamiltonPapersDir/hamiltonPaper"+str(i)
        l=getBagForDocument(hf, d)
        trainCorpus.append(l)
        corpus.append(l)
        tags.append("ho")
        i+=1
    i=1
    while(os.path.isfile("madisonPapersDir/madisonPaper"+str(i))):
        mf="madisonPapersDir/madisonPaper"+str(i)
        l=getBagForDocument(mf, d)
        trainCorpus.append(l)
        corpus.append(l)
        tags.append("mo")
        i+=1
    i=1
    while(os.path.isfile("fedPapersDir/fedPapers"+str(i))):
        l=getBagForDocument("fedPapersDir/fedPapers"+str(i),d)
        
        if (i in hamiltonNumbers):
            corpus.append(l)
            tags.append("hp")
        elif (i in madisonNumbers):
            corpus.append(l)
            tags.append("mp")
        else:
            corpus.append(l)
            tags.append("x")
        i+=1 
    tfidf=models.TfidfModel(trainCorpus)

    matrix=[]
    matrix2=[]
    print("Len corpus is "+ str(len(corpus)))
    print("Len tags is " + str(len(tags)))
    for i in range(len(corpus)):
      l=tfidf[corpus[i]]
      if (tags[i]==("hp")):
          featureList=[hamiltonClass]
          for pair in l:
              featureList.append(pair)
          matrix2.append(featureList)

      elif (tags[i]==("mp")):
          featureList=[madisonClass]
          for pair in l:
              featureList.append(pair)
          matrix2.append(featureList)

      elif (tags[i]==("ho")):
     
          featureList=[hamiltonClass]
          for pair in l:
              featureList.append(pair)
          matrix.append(featureList)
      elif (tags[i]==("mo")):
     
          featureList=[madisonClass]
          for pair in l:
              featureList.append(pair)
          matrix.append(featureList)
            
          

          

    return (matrix, matrix2)




def getOtherTFIDF(trainingSet=["trainNonFedDir/hamilton/","trainNonFedDir/madison/","testNonFedDir/hamilton/","testNonFedDir/madison/" ]):

    #print(os.listdir(trainingSet[0]))
    hamiltonfiles = [trainingSet[0] + hf for hf in os.listdir(trainingSet[0])]
    madisonfiles = [trainingSet[1] + mf for mf in os.listdir(trainingSet[1])]
    hamiltonTest = [trainingSet[2] + ht for ht in os.listdir(trainingSet[2])]
    madisonTest = [trainingSet[3] + mt for mt in os.listdir(trainingSet[3])]
    matrix1=[]
    matrix2=[]
    trainingCorpus=[]
    corpus=[]
    d=wordCountHalf()
    tags=[]
    dataClass=hamiltonClass
    for hf in hamiltonfiles:
        
        l=getBagForDocument(hf, d)
        corpus.append(l)
        trainingCorpus.append(l)
        tags.append("hr")


    for mf in madisonfiles:
        
        l=getBagForDocument(mf, d)
        corpus.append(l)
        trainingCorpus.append(l)
        tags.append("mr")

    for ht in hamiltonTest:
        
        l=getBagForDocument(ht, d)
        corpus.append(l)

        tags.append("ht")
    for mt in madisonTest:
        
        l=getBagForDocument(mt, d)
        corpus.append(l)

        tags.append("mt")

    tfidf=models.TfidfModel(trainingCorpus)
    
    for i in range(len(corpus)):
        l=tfidf[corpus[i]]
        
        if tags[i]=="hr":
            featureList=[hamiltonClass]
            for pair in l:
                featureList.append(pair)
            matrix1.append(featureList)
        
        if tags[i]=="mr":
            featureList=[madisonClass]
            for pair in l:
                featureList.append(pair)
            matrix1.append(featureList)
        
        if tags[i]=="ht":
            featureList=[hamiltonClass]
            for pair in l:
                featureList.append(pair)
            matrix2.append(featureList)
        
        if tags[i]=="mt":
            featureList=[madisonClass]
            for pair in l:
                featureList.append(pair)
            matrix2.append(featureList)
                
    return (matrix1, matrix2)


def getNumberTFIDF(n):

    trainingSet=["trainNonFedDir"+str(n)+"/hamilton/","trainNonFedDir"+str(n)+"/madison/","testNonFedDir"+str(n)+"/hamilton/","testNonFedDir"+str(n)+"/madison/"]
    

    hamiltonfiles=[]
    for i in range(300):
        fileToAdd =trainingSet[0]+ "hamiltonPaper" + str(i)
        if os.path.isfile(fileToAdd):
            hamiltonfiles.append(fileToAdd)
    madisonfiles=[]
    for i in range(300):
        fileToAdd =trainingSet[1]+ "madisonPaper" + str(i)
        if os.path.isfile(fileToAdd):
            madisonfiles.append(fileToAdd)

        
    hamiltonTest=[]
    for i in range(300):
        fileToAdd =trainingSet[2]+ "hamiltonPaper" + str(i)
        if os.path.isfile(fileToAdd):
            hamiltonTest.append(fileToAdd)
    
    madisonTest=[]
    for i in range(300):
        fileToAdd =trainingSet[3]+ "madisonPaper" + str(i)
        if os.path.isfile(fileToAdd):
            madisonTest.append(fileToAdd)
        
        
    """
    #print(os.listdir(trainingSet[0]))
    hamiltonfiles = [trainingSet[0] + hf for hf in os.listdir(trainingSet[0])]
    madisonfiles = [trainingSet[1] + mf for mf in os.listdir(trainingSet[1])]
    hamiltonTest = [trainingSet[2] + ht for ht in os.listdir(trainingSet[2])]
    madisonTest = [trainingSet[3] + mt for mt in os.listdir(trainingSet[3])]
    """   
    matrix1=[]
    matrix2=[]
    trainingCorpus=[]
    corpus=[]
    d=wordCountHalf()
    
    #this is only for debugging
    if (n==6):
        d={}
        d["alpha"]=0
        d["beta"]=1
        d["gamma"]=2
        d["delta"]=3
        d["epsilon"]=4
        d["correspondence"]=5
        d["hamilton"]=6
        
    tags=[]
    dataClass=hamiltonClass
    checker=0
    for hf in hamiltonfiles:
        print (str(checker) + " " + hf)
        checker+=1
        l=getBagForDocument(hf, d)
        corpus.append(l)
        trainingCorpus.append(l)
        tags.append("hr")


    for mf in madisonfiles:
        print (str(checker) + " " + mf)
        checker+=1
        l=getBagForDocument(mf, d)
    
        corpus.append(l)
        trainingCorpus.append(l)
        tags.append("mr")

    for ht in hamiltonTest:
        print (str(checker) + " " + ht)
        
        checker+=1
        l=getBagForDocument(ht, d)
    
        corpus.append(l)

        tags.append("ht")
    for mt in madisonTest:
        print (str(checker) + " " + mt)
    
        checker+=1
        l=getBagForDocument(mt, d)
        corpus.append(l)

        tags.append("mt")

    tfidf=models.TfidfModel(trainingCorpus)
    
    print(len(corpus))
    for i in range(len(corpus)):
        l=tfidf[corpus[i]]
        
        if tags[i]=="hr":
            featureList=[hamiltonClass]
            for pair in l:
                featureList.append(pair)
            matrix1.append(featureList)
        
        if tags[i]=="mr":
            featureList=[madisonClass]
            for pair in l:
                featureList.append(pair)
            matrix1.append(featureList)
        
        if tags[i]=="ht":
            featureList=[hamiltonClass]
            for pair in l:
                featureList.append(pair)
            matrix2.append(featureList)
        
        if tags[i]=="mt":
            featureList=[madisonClass]
            for pair in l:
                featureList.append(pair)
            matrix2.append(featureList)
                
    return (matrix1, matrix2)



"""
#This function reads all of the federalist papers and turns them into a list of feature-lists
# The output can easily be written to a training file with writeMatrixToFile
def getDisputedFederalistMatrix(testSet=["fedPapersDir/fedPapers"]):

    matrix=[]
    
    #assumes Hamilton is -1; Madison is 1, only grabs those two's unambiguous papers.
   
    for classPath in testSet:
        
        #iterate until we've done all of the files
        i=1
        while(os.path.isfile(classPath+str(i))):


#            l=wordCountDictionary(classPath+str(i), "don'tCare.txt", "don'tCare2.txt", removeWords(getFunctionList()))

            #get feature list
            l=wordCountDictionary(classPath+str(i), getFunctionList())
        
            #only read the disputed ones.
            if (disputedNumbers.count(i)==1):
                


                #Mark Madison as correct class, consistent with historical analysis
                featureList=[1]
                
                #make list and append it to our matrix.
                for pair in l:
                    featureList.append(pair[1])
                matrix.append(featureList)


            i+=1
            

    return matrix
"""

#writes a list of lists to a file so we can use it for linear svm program.
def writeMatrixToFile(m, fileName):
    outFile=open(fileName, "w")
    
    
    #iterate through the different feature vectors
    for vect in m:
        
        #write class
        outFile.write(str(vect[0]))
        
        for i in range(1,len(vect)):
            outFile.write(" " + str(i)+":"+str(vect[i]))
        
        #put newline at end
        outFile.write('\n')
    outFile.close()



#writes a list of lists to a file so we can use it for linear svm program.
def writeTFIDFToFile(m, fileName):
    outFile=open(fileName, "w")
    
    
    #iterate through the different feature vectors
    for vect in m:
        
        #write class
        outFile.write(str(vect[0]))
        
        for i in range(1,len(vect)):
            outFile.write(" " + str(vect[i][0]+1)+":"+str(vect[i][1]))
        
        #put newline at end
        outFile.write('\n')
    outFile.close()

#Enumerations of whose papers are whose
madisonNumbers=[10,14] + range(37,49)

hamiltonNumbers=[1,6,7,8,9,11,12,13,15,16,17] + range(21,37) + range (59,62) + range(65,86)

jayNumbers=[2,3,4,5,64]

collabNumbers=[18,19,20]

disputedNumbers=range(49,59) + [62,63]

headerWords=["james", "madison", "the", "complete", "works", "of", "digitized","vj00q", "by", "ic", "private", "correspondence", "alexander", "hamilton"]

def wordIsOkay(word):
    returnBool=True
    if not (word.isalpha()):
        return False
    if word in headerWords:
        returnBool=False
    if word[0:1]=="17":
        returnBool=False
    if word in getFunctionList():
        returnBool=False
    return returnBool

def lineIsOkay(line):
    returnBool=True
    if not (line[0].isalpha()):
        return False
    if line[0]=="T":
        return False
    if line[0]=="D":
        return False
    if line[0]=="P":
        return False
    return True

"""
check line
no D,P, T, *, number
"""
