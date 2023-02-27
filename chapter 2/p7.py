count=0
def isTripleDouble(word): 

 	global count  
 	i = 1 
 	while i < len(word): 
 		if word[i] == word[i-1]: 
 			count += 1 
 			i+=2 
 		else: 
 			count = 0 
 			i+=1 
 	if count == 3: 
 		return True 
 	else: 
 		return False
a="ssssssh"
print(isTripleDouble(a))
print(count)