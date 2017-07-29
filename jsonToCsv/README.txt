Summary
Script takes in file with json string in it and parses into CSV file format.
CSV format ordering is in the same order that unique json keys appear.
Takes 2 command line arguments, an input file to parse, and an output file to output CSV format strings to.

Run with:
	python jsonParser.py <inputFile.txt> <outputFile.txt>


Notes
**Written in Python 3.6

-Only working on 'flat' json structure. Can add method to flatten json before parsing.
-CSV ordering is simply the order in which the json keys first appear. Currently ordering stored in map '["key1": 1 (csvOrder), "key2": 2, ...]' so it can be easily changed to desired csv ordering

-Any questions, email me at: david.truong510@gmail.com
