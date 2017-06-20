#write a program that counts the number of characters in a sentense
import pprint
print("Enter a Sentence")
Sentence=input()
count={}
for character in Sentence:
	count.setdefault(character,0)
	count[character]=count[character]

print(count)
