#!/usr/bin/env python3
import sys
import re
import csv
import operator

# read the .log file and extract error
def ReadFile():
  userDict={}
  with open(sys.argv[1]) as f :
    for line in f.readlines():
      #print(line)
#       Error
      if "ticky: ERROR" in line :
        user_error=re.search(r"ticky: ERROR .* \(([\w\.]+)\)$", line)
        if not user_error[1] in userDict:
          userDict[user_error[1]]={"ERROR":1,"INFO":0}
        else:
          userDict[user_error[1]]["ERROR"]+=1
        #print(user_error)
#        INFo 
      elif "ticky: INFO" in line :
        user_info=re.search(r"ticky: INFO .* \(([\w\.]+)\)$", line)
        if not user_info[1] in userDict:
          userDict[user_info[1]]={"ERROR":1,"INFO":0}
        else:
          userDict[user_info[1]]["INFO"]+=1
        #print(user_info)

    f.close()  
  userDictSorted=sorted(userDict.items(),key=operator.itemgetter(0))
  return userDictSorted
print(ReadFile())

def WriteToCSV():
  userDict=ReadFile()
  with open("user_statistics.csv","w") as f:
    Writer=csv.writer(f)
    Writer.writerow(["Username","ERROR","INFO"])
    for user,dicti in userDict:
      values="{}{}".format(dicti["ERROR"],dicti["INFO"])
      Writer.writerow([user,str(dicti["ERROR"]),str(dicti["INFO"])])
    f.close()
if __name__=="__main__":
  WriteToCSV()

