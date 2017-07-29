import sys
import json

#PARSES FLAT JSON IN FILE TO CSV FORMAT
def parse_json():
	if(len(sys.argv) == 3):
		input_file = sys.argv[1]
		output_file = sys.argv[2]
		parse_file(input_file, output_file)
	else:
		print("Need to provide two arguments: 'input file name' and 'output file name'")

#PARSES FILE
#@PARAM input_file: file name of file containing json to parse
#@PARAM output_file: file name of file to output csv formatted string
def parse_file(input_file, output_file):
	print("Parsing json: " + input_file)
	print("Outputting to: " + output_file)
	json_to_parse = json.load(open(input_file, "r"))
	key_map = get_key_indices(json_to_parse)
	create_csv_output(json_to_parse, key_map, output_file)

#CREATES CSV FORMATTED STRINGS
#@PARAM json_to_parse: json parsed into dict()
#@PARAM key_map: dict() of json key->csv column index
#@PARAM output_file: file name of file to output csv formatted string
def create_csv_output(json_to_parse, key_map, output_file):
	csv_columns = get_csv_columns(key_map)
	write_file = open(output_file, "w")
	write_file.write(csv_columns + "\n")
	for i in range(len(json_to_parse)):
		csv_format = []
		for j in range(len(key_map)-1):
			csv_format.append(",")

		for key in json_to_parse[i]:
			index = key_map[key]
			if index != len(key_map)-1:
				csv_format[index] = str(json_to_parse[i][key]) + ","
			else:
				csv_format.append(str(json_to_parse[i][key]))

		csv_string = ""
		for csv_item in csv_format:
			csv_string += csv_item
		
		write_file.write(csv_string + "\n")

	write_file.close()

#GETS CSV COLUMNS AS STRING OF JSON KEYS
#@PARAM key_map: dict() of json key->csv column index
def get_csv_columns(key_map):
	return ",".join(key_map.keys())

#GETS ALL KEYS IN JSON INTO DICT(KEY->COLUMN INDEX)
#@PARAM json_to_parse: json parsed into dict()
def get_key_indices(json_to_parse):
	key_map = {}
	next_column_index = 0
	for i in range(len(json_to_parse)):
		for key in json_to_parse[i]:
			if key not in key_map:
				key_map[key] = next_column_index
				next_column_index+=1

	return key_map



parse_json();