#this program counts word frequency in a sentence

def frequency_count(sentence):
    words = sentence.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] +=1
        
        else:
            frequency[word] = 1

    return frequency
sentence = input("Enter a sentence: ")

result = frequency_count(sentence)

print("Word frequency count: ")

for word, count in result.items():
    print(f"{word}: {count}")

