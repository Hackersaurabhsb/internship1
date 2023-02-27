
def splitWord(word, numOfChar): 
 	output = [] 
 	for i in range(0,len(word),numOfChar): 
 		output.append(word[i:i+numOfChar]) 
 	return output 
a="saurabh sharma"
print(splitWord(a, 3))
