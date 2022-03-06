import anytree

# parser class to create a parser object that divides an list of sql tokens
# into separate lists of statements
class parser():

    # init the parser object with the token list form a lexer.
    # creates 2 empty lists for handleing separator in semi and
    # a list for the paresd SQL statements
    def __init__(self,tokenList):
        self.tokenList = tokenList
        self.statement = []
        self.semi = []
    
    # prints the name of every token object of a statment
    # debug purpose
    def printStatementName(self):
        for i, lists  in enumerate(self.statement):
            print("New Statement")
            for j ,objects in enumerate(lists):
                print(objects.name)
    
    
    # detects every semicolon in the token list an saves the index
    # of them in self.semi, after that calls splitList()
    def detectSyntax(self): 
        for i,token in enumerate(self.tokenList):
            if token.name == ';':
                self.semi.append(i)
        self.statement = self.splitList(self.tokenList,self.semi)
    
    # splits the valueList of tokens into separat lists anlong
    # the index values of indexList
    def splitList(self,valueList,indexList):
        
        lists = []

        # enumerate over the indexList
        for i,char in enumerate(indexList):
            
            # creates a list to save the evaluated tokens it the inner for-loop
            forList = []

            #iterates over the valueList 
            for j,char2 in enumerate(valueList):
                
                # first case when we are in the indexList index 0,
                # as long as the index of the valueList is smaller then
                # the value of the indexList at index 0 we append the 
                # token objects to the for list
                if i ==0 and j <= char:
                    forList.append(char2)
               
                # for every case afte indexList index =0,
                # starts to append token objects from indexList value i-1
                # until the index of inner for loop is => the value of indexList i
                if indexList[i-1]<j  and char>=j:
                    forList.append(char2)
            
            # safes the inner for-loop list in list and clears them
            lists.append(forList)
            forList=[]
        return lists  
        

    


    


