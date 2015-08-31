#!/usr/bin/python

"""
Adam Kavka and Levi Melnick
December 2014

This calls functions in utility.py to get the function-words feature set for disputed and undisputed papers and writes the results to disk.
"""

import pickle
import utility

import utility as u
"""m1=u.getUndisputedFederalistMatrix()
m2=u.getDisputedFederalistMatrix()
u.writeMatrixToFile(m1, "code/svm_light/fedTrain.txt")
u.writeMatrixToFile(m2, "code/svm_light/fedTest.txt")
"""

m1=u.getTrainingMatrix()
m2=u.getUndisputedFederalistMatrix()
u.writeMatrixToFile(m1, "code/svm_light/fedTrain.txt")
u.writeMatrixToFile(m2, "code/svm_light/fedTest.txt")
