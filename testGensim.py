#!/usr/bin/python
import pickle
import utility


c = utility.wordCount()

(m1,m2)= utility.getNumberTFIDF(4)
#(m1,m2)= utility.getUndisputedTFIDF()
print (str(len(m1))  +" " + str(len(m2)))
#print (str(m1)+ str(m2))
utility.writeTFIDFToFile(m1, "code/svm_light/fedTrain.txt")
utility.writeTFIDFToFile(m2, "code/svm_light/fedTest.txt")

#corpus=[[(0,1), (1,2), (2,1)],
 #       [(1,1), (3,2)]]
#tfidf=models.TfidfModel(corpus)

#print (tfidf[[(2,3),(3,2)]])
#print (tfidf[corpus[1]])

