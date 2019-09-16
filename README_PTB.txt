README.txt 

Authors: Martin Horst, Kadir Gundogdu

Ling 473, Project 1, August 8, 2019


Main
------------------------------
Proj1.py

Results
------------------------------
Sentence: 4670
Noun Phrase: 13221
Verb Phrase: 7920
Ditransitive Verb Phrase: 28
Intransitive Verb Phrase: 121

Specs
------------------------------
Project 1 required us to count constituents that were parsed and annotated 
through the Penn Tree Bank. 

Approach
-------------------------------
We used a Python dictionary to structure the different constituents that the 
came across in the file. Where we needed to be more specific, IE for Intransitive
Verbs and Ditransitive Verbs, RegEx and a stack-like structure were implemented, 
respectively. These approaches worked with 99% coverage over the entire corpora that
was required as per the project specs. 

Problems
-------------------------------
This assignment challenged us from a number of different fronts. We struggled to understand 
the connection between the wrapper language and our program, as well as the SSH server and the 
condor system. Besides the systematic knowledge barriers, finding the correct algorithm to find
the Ditransitive verbs proved too much for this assignment; we know that there were (supposedly) 
34 DTV and 123 ITV in the corpus, but our algorithm missed 8 of them total. On individual test files,
the python program worked flawlessly, but time constraints prevented us from debugging the issues wholly. 
