## NLP
series of NLP scripts in python: language classification, syllabification of Thai, Penn Tree Bank analyzer, 

# Penn Tree Bank Counter
The Penn Tree Bank Counter takes in all PTB files from a location and outputs the number of sentence, VP, NP, Ditransitive VP and Intransitive VP constituents present in the directory. Download PTB files from https://catalog.ldc.upenn.edu/LDC99T42 to get started, and then run 
```
python3 PennTreeBankCounter.py your_directory 
```
from the command line to start counting constituents

# Human Genome Search
The files _TrieNode_ and _TrieMain_ are the main files for a Trie implementation of a DNA sequencing and searching program. Taking inspiration from the files found as part of the human genome project ( http://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit ), the Main file matches target DNA sequences in _targets.txt_ to substrings found in the downloadable files in a single pass. 
To get started, download 
``` 
targets.txt
TrieNode.py
TrieMain.py
__init__
```
and from the directory containing all of the files, run the following command:
```
TrieMain.py targets downloadable_files
``` 
from a command line terminal. Be warned, due to the size of DNA files, this may take a while, depending on your individual box's processing speed.
