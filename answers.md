# 1.
## a) Describe what the program does:
The program gets the user too input a sentence.
Then it counts the number of occorunces of each character in the sentence and stores them in a dictionary.
It then prints the resulting dictionary.

## b) 
`char` represents a character in the sentence.
The program iterates over every character in the sentence

## c)
`chars` is of type `dictionary`

## d)
`keys` - The character being counted
`values` - The number of time the character occurs

## e)
There are no changes in the behaviour of the program

## f)
The get operation returns the value associated with the key and if the value is not found instead of raising a `KeyError` it returns `None` or a specified value.

## g)
```py
vowels = 'aeiouAEIOU'
vowel_count = {}

sentence = [i for i in input('enter a sentence: ') if i in vowels]
for char in sentence:
    vowel_count[char] = vowel_count.get(char, 0) + 1

print(vowel_count)
```

## h)
```py
vowels = 'aeiouAEIOU'
count = {}
sentence = input('enter a sentence: ')
count['vowels'] = len([i for i in sentence if i in vowels])
count['consonants'] = len(sentence) - count['vowels']

print(count)
```

## i)


