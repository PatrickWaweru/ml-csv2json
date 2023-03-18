#!/usr/bin/python3

import csv, json, sys; 
# print(json.dumps([dict(r) for r in csv.DictReader(sys.stdin)]))

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create an array
    data = []
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        # csvReader = csv.DictReader(csvf, delimiter='\t', quoting=csv.QUOTE_NONE)
        csvReader = csv.DictReader(csvf, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            # key = rows['FacilityCode']
            # data[key] = rows
            # print(rows)
            data.append(rows)
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        # jsonf.write(json.dumps(data, indent=4))
        jsonf.write(json.dumps(data, indent='\t', separators=(',', ': ')))
         
# Driver Code
 
# Decide the two file paths according to your
# computer system
csvFilePath = r'in.csv'
jsonFilePath = r'out.json'
 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)

