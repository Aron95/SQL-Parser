import parser as pr

teststring ='SELECT  column2 FROM   table_name;CREATE TABLE boy;DELETE TABLE boy;boy SELECT FROM colum2;'

KEYWORD = ["SELECT","FROM","WHERE","CREATE DATABASE","CREATE TABLE", "DELETE TABLE","DELETE DATABASE"]

SINGLE_KEYWORD = ["{","}","(",")",";",",","*"]
white_space = " "
sIndex = 0 
tokenNumber = 1

token = []
lexeme = ''

# Defines a token of an sql statment. Holds following values:
# identifyer for the word, name of the word, what number it was in a string,
# starting point of the word in the string and end point, these are indexes.
class toke():
    def __init__(self,identifyer,name,number,sIndex,eIndex):
        self.identifyer = identifyer
        self.name = name
        self.number = str(number)
        self.sIndex = str(sIndex)
        self.eIndex = str(eIndex)
    # method to print the data of a token
    def printTokenData(self):
        print("The Token is a "+self.identifyer+ " Name: "+self.name+" with number: "
                +self.number+" starts at: "+ self.sIndex+ " ends at: "+self.eIndex)


print(teststring)

#enumerate over every char in a teststring.
for i,char in enumerate(teststring):

    # set starting Index for the next word in the string.
    # after every enumartion the lexeme will set empty.
    # so the next starting Index will be i
    if lexeme == '':
        sIndex = i
    
    # if char is not a white space or Lexeme ==  DELETE or TABLE  adds it to lexeme
    if char != white_space:
         lexeme += char
         

    if lexeme == "DELETE" or lexeme == "CREATE":
        lexeme +=white_space
        continue

    # if char is in Single Keywords, it create a token object with the nesseary data
    # count tokenNumber up and clears the lexeme 
    if char in SINGLE_KEYWORD:
        tokenObject = toke('SINGLE_KEYWORD',char,tokenNumber,i,i)
        token.append(tokenObject)
        tokenNumber +=1
        lexeme = ''
    
    # checks if its the last char in string, error protection
    if i+1 < len(teststring):
        
        # if next char is a separator for sql proceed
        if teststring[i+1] == white_space or teststring[i+1] in SINGLE_KEYWORD:
        
            # if lexem is in Keyword, it creats a token object with ist nesseary data
            # count tokenNumber up
            if lexeme in KEYWORD:
                tokenObject = toke('KEYWORD',lexeme,tokenNumber,sIndex,i)
                token.append(tokenObject)
                tokenNumber +=1

            # if lexem is not in Keyword its an IDS and create a token object with its 
            # nesseary data, count tokenNumber up
            if lexeme not in KEYWORD:
                if lexeme not in SINGLE_KEYWORD and lexeme != '':
                    tokenObject = toke('IDS',lexeme,tokenNumber,sIndex,i)
                    token.append(tokenObject)
                    tokenNumber +=1

            # after that clears lexeme for next for iteration
            lexeme = ''

#for toke in token:
    #toke.printTokenData()


parser = pr.parser(token)
parser.detectSyntax()
parser.printStatementName()
print("_______________________________________________")
parser.validSyntaxCheck()


