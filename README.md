# CSV NORMALIZER TOOL #

## ENVIRONMENT/BUILD: ##
- Use a Mac computer with macOS High Sierra version 10.13
- Install [Python3](https://www.python.org/downloads/). I used version 3.7.2. 
- Use the "pip" tool (automatically installed with python3) to install the pytz, and datetime packages. Check to see they are installed with the "list" command.
	```
	python3 -m pip install datetime
	python3 -m pip install pytz
	python3 -m pip list
	```
- You're finished setting up!

## USAGE: ##
```
python3 csv_normalizer.py input_csv_file
```
- Open a terminal
- Navigate to the directory that contains csv_normalizer.py, nrmlz.py, and an input .csv file
- The tool takes the input .csv file as a command line argument. 
- Execute "python3 csv_normalizer.py input_csv_file" to run
- The output .csv file will be generated in the same directory, with filename "OUTPUT_"+input_csv_file

## EXAMPLE: ##
```
python3 csv_normalizer.py sample.csv
``` 
- OUTPUT_sample.csv generated in current directory

## ANALYSIS: ##
- space complexity O(1) : only one row of .csv data is held in memory at a time
- time  complexity O(n) : runtime has a linear relation to the number of .csv rows

## REQUIREMENTS: ##
These requirements were extracted from the prompt. 
They are commented in the source code --near where they are fulfilled--for easy traceability

REQ# | Details
-----|-----------------
0.1  | Please write a tool that reads a CSV formatted file on `stdin`... 
0.2  | ...and emits a normalized CSV formatted file on `stdout`
1    | The Timestamp column should be formatted in ISO-8601 format.
2    | The Timestamp column should be assumed to be in US/Pacific time; please convert it to US/Eastern.
3    | All ZIP codes should be formatted as 5 digits. If there are less than 5 digits, assume 0 as the prefix.
4    | All name columns should be converted to uppercase. There will be non-English names.
5.1  | The Address column should be passed through as is, except for Unicode validation. 
5.2  | Please note there are commas in the Address field; your CSV parsing will need to take that into account. Commas will only be present inside a quoted string.
6    | The columns `FooDuration` and `BarDuration` are in HH:MM:SS.MS format (where MS is milliseconds); please convert them to a floating point seconds format.
7    | The column "TotalDuration" is filled with garbage data. For each row, please replace the value of TotalDuration with the sum of FooDuration and BarDuration.
8    | The column "Notes" is free form text input by end-users; please do not perform any transformations on this column. If there are invalid UTF-8 characters, please replace them with the Unicode Replacement Character.
9    | If a character is invalid, please replace it with the Unicode Replacement Character.  If that replacement makes data invalid (for example, because it turns a date field into something unparseable), print a warning to `stderr` and drop the row from your output.
