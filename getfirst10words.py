strings = "one two three four five six seven eight nine ten eleven twelve"

#long
words = strings.split() #separating words by whitespace
ten = words[:20] #getting first 20 words as list form 
tenstrings = '  '.join(ten) #converting list to string

#short
test = strings.split()[:5]
teststrings = ' '.join(test)

#best
tenstrings = '  '.join(strings.split()[:5])

print(f'There are {len(words)} words')
print(tenstrings)
print(test)