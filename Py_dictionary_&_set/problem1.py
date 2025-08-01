# Write a program to create a dictionary of Bangla words with values as their English translation. Provide user with an option to look it up!

words={
    "ami" : "myself",
    "tumi" : "yourself",
    "ke" : "who",
    "ki" : "what",
    "kake" : "whom"
}

userValue=input("enter bangla word - ")
print(words[userValue])