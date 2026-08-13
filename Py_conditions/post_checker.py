"""

Post Checker
------------
Checks whether a given keyword appears anywhere
inside the text which user entered

"""

keyword = input("Enter key word : ")
post = input("Enter the post : ")

if (keyword.lower() in post.lower()):
    print(f"This post mentions {keyword}")
else:
    print(f"This post does not mention {keyword}")