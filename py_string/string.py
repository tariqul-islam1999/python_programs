name="tariqul Islam Faisal"
nameShort1=name[0:9] # for shorting the string
nameShort2=name[:8] # left side default take 0
nameShort3=name[-4:-1] # reverse index start with -1 from the last
length=len(name) # len() for calculate the string size
end=name.endswith("isal") # for check the string's last words
start=name.startswith("tari") # for check the string's first words
cap=name.capitalize() # for capitalize only the 1st word
upr=name.upper() # convert all the string into upper case
lwr=name.lower() # convert all the string into lower case
find=name.find("Islam") # find the word position from string
replc=name.replace("Faisal","Faysal") # replace the old word

print(replc)
