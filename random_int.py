# save this file as random_int.py
from random import randint
def randlist(r, usedlist, done):
	sum = 0
	alpha = ["a","A","b","B,","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","!","@","#","$","%","^","&","*","(",")","-","_","=","+",":","|","\\"]
	usedlist[r] = 1
	c = alpha[r]
	print (len(usedlist))
	for i in range (len(usedlist)):
		sum = sum + usedlist[i]
	#print (c, usedlist, "sum", sum)
	if sum == 6:
		done = True
	return c, usedlist, done 
	
def main():
	# initial variables
	used = [0,0,0,0,0,0]
	done = False #boolean
	######################
	while done == False:
		r = randint(0,5) # make a random number
		c,used,done = randlist(r, used, done)
		#print (used,)
		print(c,end="")
main()


