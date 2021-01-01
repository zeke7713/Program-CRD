#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import run as x 
#importing the main file("code" is the name of the file I have used) as a library 


x.create("chennai",75)
#to create a key with key_name,value given and with no time-to-live property


x.create("che",60,560) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("chennai")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("che")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("chennai",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it

x.delete("chennai")
#it deletes the respective key and its value from the database(memory is also freed)


