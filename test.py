import msvcrt

while 1:
    print ('Testing..')
    # body of the loop ...
    if msvcrt.kbhit():
	    if ord(msvcrt.getch()) == 27:
	        break