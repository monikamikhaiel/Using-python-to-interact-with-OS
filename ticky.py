#!/usr/bin/env python3
import sys
import re
import csv
import operator

# read the .log file and extract error
def ReadFile():
  errorDict={}
  with open(sys.argv[1]) as f :
    for line in f.readlines():
      #print(line)
      error=re.search(r"ticky: ERROR ([\w ]*) ", line)
      #print(error)
      if error ==None:
        continue
      errorDict[error[1]]=errorDict.get(error[1],0)+1
    f.close()  
  errorDictSorted=sorted(errorDict.items(),key=operator.itemgetter(1),reverse=True)
  return errorDictSorted
print(ReadFile())

def WriteToCSV():
  ErrorDict=ReadFile()
  with open("error_message.csv","w") as f:
    Writer=csv.writer(f)
    Writer.writerow(["Error","Count"])
    Writer.writerows(ErrorDict)
    f.close()
if __name__=="__main__":
  WriteToCSV()

