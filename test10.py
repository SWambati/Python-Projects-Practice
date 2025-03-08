#list operations
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Stu Sutcliffe", "Pete Best"]
new_beatles = beatles[:]
del new_beatles [3:]

new_beatles.append("Ringo Starr")
print(new_beatles)
print(beatles)
print("Ringo Starr" in beatles)