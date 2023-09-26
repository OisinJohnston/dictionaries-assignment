vowels = 'aeiouAEIOU'
count = {}
sentence = input('enter a sentence: ')
count['vowels'] = len([i for i in sentence if i in vowels])
count['consonants'] = len(sentence) - count['vowels']

print(count)

