#this program removes duplicates from a list 

people = ["Lucy", "Julius", "Chris", "Ordell", "Kimmie", "Suki", "Julius", "James", "Lucy"]
people_2 =[]
for person in people:
    if person not in people_2:
        people_2.append(person)

print (people_2)