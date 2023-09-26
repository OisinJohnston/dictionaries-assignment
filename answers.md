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
```py
count = {}
sentence = input('enter a sentence: ').split()

for i in sentence:
    count[i] = count.get(i, 0) + 1

print(count)
```

## j)

### I
It prints the key value pair with the highest value.

### II
The one that is encountered first is printed.
This may be fixed like this:
```py
from collections import Counter
c = Counter(chars)
max_value = c.most_common()[0][1]
max_keys = [i[0] for i in c.most_common() if i[1] == max_value]
print(f'The most commonly occuring characters are {max_keys} with each occuring {max_value} times')
```

## k)

I prefer the first implementation, I think it is more pythonic and is simpler too understand and reads like english, which is ideally how all code should be

The code could be altered like so:

```py
max_key = []

max_value = 0

for k, v in chars.items():
    if v > max_value:
        max_value = v
        max_key = [k]
    if v == max_value:
        max_key += [k]

# most_common_keys = [k for k, v in chars.items() if v == max_value]
print(f'The most commonly occuring characters are {max_key} with each occuring {max_value} times')
```

## l)

