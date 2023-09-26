vowels = 'aeiouAEIOU'
vowel_count = {}

sentence = [i for i in input('enter a sentence: ') if i in vowels]
for char in sentence:
    vowel_count[char] = vowel_count.get(char, 0) + 1

print(vowel_count)
