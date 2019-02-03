#CVS NORMALIZER TOOL | GARRETT GRUBE | 1/31/19 | Truss Work Sample | csv_normalizer.py
#This script opens a .csv file and for each row normalizes the data, and prints it to a new .csv file
#see README.md for requirements extracted from the prompt

import csv, io, nrmlz, sys, warnings

def main(f):

	with io.open(f, mode='r', encoding='utf8', errors="replace") as csv_file:		#REQ_0.1 | read a CSV file on 'stdin'								
		with open("OUTPUT_"+f, mode="w", encoding='utf-8') as norm_csv_file:		#REQ_0.2 | emit a normalize CSV file on 'stdout'
			
			csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"') 		#REQ_5.2 | quotechar parameter handles commas in the address field
			csv_writer = csv.writer(norm_csv_file, delimiter=",",
				quotechar='"', quoting=csv.QUOTE_MINIMAL)
			
			lineCount = 1
			for row in csv_reader:
				try:
					if lineCount != 1:												#do not normalize header row
						row = nrmlz.normalize(row)
				except:																#REQ_9 | print a warning to stderr if replacement makes data invalid						
					warnings.warn("error - row could not be parsed and was dropped from output") 
				else:
					csv_writer.writerow(row)										#REQ_9 | drop row from output if replacement makes data invalid										
					lineCount += 1

if(len(sys.argv) != 2):
	print("Must provide input .csv file as command line arguement")
else:
	main(sys.argv[1])