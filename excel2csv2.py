# import the required libraries
import openpyxl
import csv, json, os
import pandas as pd
  
# open given workbook 
# and store in an excel object 
excel = openpyxl.load_workbook("gis_iit_matrix.xlsx")
  
# select the active sheet
sheet = excel.active

# get rows
# rows = sheet.rows
  
# writer object is created
col = csv.writer(open("tmp.csv", 'w', newline=""), escapechar='\\', quoting=csv.QUOTE_NONNUMERIC)  

# write the header
col.writerow([cell.value for cell in list(sheet.rows)[0]])

# writing the data in csv file
for r in list(sheet.rows)[1:]:
    # row by row write 
    # operation is performed
    # col.writerow([('"' + cell.value + '"') for cell in r])
    # col.writerow([("\"{}\"".format(cell.value)) for cell in r])
    # myrow = [json.dumps(cell.value) for cell in r]
    # myrow = [("\"{}\"".format(cell.value)) for cell in r]
    myrow = []
    #for i, cell in r:
    #	if i == 0:
    #		myrow.append("\"{}\"".format(cell.value))
    #for cell in r:
    #	myrow.append(cell.value)
    myrow.append("\"{}\"".format(r[0].value))
    for cell in r[1:]:
    	myrow.append(cell.value)
    col.writerow(myrow)
  
# read the csv file and 
# convert into dataframe object 
## df = pd.DataFrame(pd.read_csv("in.csv"))
  
# show the dataframe
## df

# replace quotes (""") with (") inplace

replacements = {'"""':'"'}

#lines = []
#with open('in.csv') as infile:
#    for line in infile:
#        for src, target in replacements.items():
#            line = line.replace(src, target)
#        lines.append(line)
#with open('in.csv', 'w') as outfile:
#    for line in lines:
#        outfile.write(line)

with open('tmp.csv') as infile, open('in.csv', 'w') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)

# remove (delete) tmp.csv
os.remove("tmp.csv")


