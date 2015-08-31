#!/usr/bin/python

"""
Adam Kavka and Levi Melnick
December 2014

This runs the SVM program (a third party C program) on the features sets that script.py and testGensim.py wrote to disk.
"""


import utility as u
import os
from permute import permute




m=u.getUndisputedFederalistMatrix()
d=u.getDisputedFederalistMatrix()


trainfile = "code/svm_light/fedTrain.txt"
testfile = "code/svm_light/fedTest.txt"
modelfile = "code/svm_light/fedModel.txt"
predictionfile = "code/svm_light/fedPredictions"
u.writeMatrixToFile(m, trainfile)
u.writeMatrixToFile(d, testfile)
os.system("./code/svm_light/svm_learn -x 1 -c 1000000.0 " + trainfile + " " + modelfile)
os.system("./code/svm_light/svm_classify " + testfile + " " + modelfile + " " + predictionfile)
    

