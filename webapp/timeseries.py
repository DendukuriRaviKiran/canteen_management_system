#Python3 program to calculate Root Mean Square 

import math 
#Function that Calculate Root Mean Square 
def rmsValue(arr): 
	square = 0
	mean = 0.0
	root = 0.0
	
	n = len(arr)
	#Calculate square 
	for i in range(0,n): 
		square += (arr[i]**2) 
	
	#Calculate Mean 
	mean = (square / (float)(n)) 
	
	#Calculate Root 
	root = math.sqrt(mean/len(arr)) 
	
	return root+arr[n-1] 

#Driver code 
if __name__=='__main__': 
	arr = [1, 2, 3, 6] 
	n = len(arr) 
	print(rmsValue(arr)) 

#This code is contributed by Shashank_Sharma 
