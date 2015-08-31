# federalistPapers
This is a machine learning project where we sought to classify the authorship of the Federalist Papers.The full analysis is available here:
https://onedrive.live.com/redir?resid=32E6A245B0AB92ED!5401&authkey=!AHJrKtKotv9dRU4&ithint=file%2cpdf

You're free to use any part of this code. Please just cite your source and please don't use this code for academic misconduct.

This is only a sampling of the code.

The files:

utility.py -  this is where the bulk of the project is. It does many things.
(if I had to do things over again I would have organized this into several files):
  - It contains the list of function words. 
  - It divides the monolithic Federalist Paper text file into individual files (one for each Paper)
  - It converts documents to bags of words
  - Divides the "other writings" of Madison and Hamilton into individual documents.
  - It puts bag-of-words dictionaries into the text-matrix format our SVM needs
  - It can look at a training set of documents and get the tf-idf features for them, outputting in the format needed for SVM
  - It can write the feature-matrix to disk files
  - with all these functions, it can iterate over the undisputed (training) documents, or the disputed (test) documents.
  
script.py - this calls functions in utility.py to get the function-words feature set for disputed and undisputed papers

testGensim.py - this calls functions in utility.py to get the tf-idf feature set for disputed and undisputed papers

runsvm.py - this runs the SVM program (a third party C program) on the features sets that script.py and testGensim.py wrote to disk.
