#################################
#
#		Program Description:
#		
#		
#		author: johnathan would
#		email: jwood0118@kctcs.edu
#		last edit: 
#		for: 
#	user,password,760.0,75.0
#	mwimpelberg,test1,1000.0,100.0
#	jwood,test2,1000.0,100.0
#	dkrebs,test3,1000.0,100.0
#
# use only in the directory of an empty text file named EXACTLY "users.txt" ###
#
########################################################
import os

userFile = open('users.txt', 'r+')
userFile.seek(0)
userFile.write('user,password,760.0,75.0')
userFile.seek(32)
userFile.write('\nmwimpelberg,test1,1000.0,100.0')
userFile.seek(64)
userFile.write('\njwood,password,1000.0,100.0')
userFile.seek(96)
userFile.write('\ndkrebs,test3,1000.0,100.0')
userFile.close()

for x in range(0,10):
        print "loading"
        for y in range(0,10):
                os.system('cls' if os.name == 'nt' else 'clear')
users = [] # blah blah i need this
userFile = open('users.txt', 'r')
userFile.seek(0)
users.append((str(userFile.readline).strip().split(',')))
userFile.seek(32)
users.append((str(userFile.readline).strip().split(',')))
userFile.seek(64)
users.append((str(userFile.readline).strip().split(',')))
userFile.seek(96)
users.append((str(userFile.readline).strip().split(',')))
userFile.close()

for x in range(0, len(users)):
        print str(users[x])
print " default users.txt Generated"



