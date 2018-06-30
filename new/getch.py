import getch3
v=0
x=""
def getchmessage():
	global x
	char=getch3.getch()
	if char =="13" :
		print(234)
	x=x+char
	
	print(x)
while v<1:
	getchmessage()
