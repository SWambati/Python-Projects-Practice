#the program contains a list of The Beatles members. List methods have been used
beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)
new_members = ["Stu Sutcliffe", "Pete Best"]
for member in new_members:
    beatles.append(member)
    

print(beatles)
del beatles[3]
del beatles[-1]
print(beatles)

beatles.insert(0, "Ringo Starr")
print(beatles)

print("The Fab",len(beatles))