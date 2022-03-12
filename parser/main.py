input = 'SELECT FORM vjdf dgklgjdlgj  dfkgldg jigjergj engjnjfg colum1; SELECT WITH;'
index = [1,7,10,40,43,62]


KEYWORD = ["SELECT","FROM","WHERE","CREATE DATABASE","CREATE TABLE", "DELETE TABLE","DELETE DATABASE"]


 if statment[count].name in self.KEYWORD and statment[count].name != "WHERE": # checks if first Keyword is valid
                    ++count
                    if statment[count].name not in self.KEYWORD and statment[count].name != ";": # checks if second word is valid so only IDS
                        ++count
                        if statment[count].name == ";": # checks if a statment is closed 
                            print("use checkSemantic")
                            count = 0
                            continue
                        elif statment[count].name == "FROM": # checks if the staments has the from keyword
                            ++count
                            if statment[count].name not in self.KEYWORD and statment[count].name not in self.SINGLEKEYWORD: # checks if the stament is a IDS
                                ++count
                                if statment[count].name == "WHERE":
                                    ++count
                                    if statment[count].name not in self.KEYWORD and statment[count].name not in self.SINGLEKEYWORD: # checks if the stament is a IDS
                                        ++count
                                        if statment[count].name == ";":
                                            print("use checkSemantic")
                                            count = 0
                                            continue
                                        else:
                                            print("Error onyl ; is valid")
                                            continue
                                    else:
                                        print("Error only IDS valid")
                                        continue
                                elif statment[count].name == ";": # checks if stamtent is closed
                                    count =0
                                    print("use checkSemantic")
                                    continue
                                else:
                                    print("Error only KEYWORD and ; are valid")
                                    continue
                            else:
                                print("Error onyl IDS is valid")
                                continue
                        else:
                            print("Error Only From, Where or ; are valid")
                            continue
                    else:
                        print("Error no valid IDS")
                        continue
                else:
                    print("Error Statment needs to start with a keyword token")
                    continue


def splitList(valueList,indexList):
    
    lists = []
    
    for i,char in enumerate(indexList):
        
        forList = []
        for j,char2 in enumerate(valueList):
            
            if i ==0 and j <= char:
                forList.append(char2)

            if indexList[i-1]<j  and char>=j:
                forList.append(char2)
        
        lists.append(forList)
        forList=[]

    return lists

def parser(syntax):
    parsed = list(map(list, syntax.split()))
    return parsed


lst = parser(input)




print(index)    
print("Peters Mehtode")
print(splitList(input,index))
print("Patrick Methode")

print(lst)


