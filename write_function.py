def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

user = ["mwimpelberg","test1","1000.0","100.0"]
user = str(user)
replace_line("users1.txt", 1, (user+"\n"))

#this works, but I need to get that string into the correct
#format into the word file.

#for testing I recommend dragging this file and the users file
#into a seperate directory until you get it tweaked so that the
#user input matches what the text file looks like.  Once it does
#we got this problem whipped I think.
