sentence = input("Enter a sentence: ")

chars = {}

for char in sentence:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1
print(chars)



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

"""
max_key = ''

max_value = 0

for k, v in chars.items():
    if v > max_value:
        max_value = v
        max_key = k

most_common_keys = [k for k, v in chars.items() if v == max_value]
print(f'The most commonly occuring characters are {most_common_keys} with each occuring {max_value} times')


from collections import Counter
c = Counter(chars)
max_value = c.most_common()[0][1]
max_keys = [i[0] for i in c.most_common() if i[1] == max_value]
print(f'The most commonly occuring characters are {max_keys} with each occuring {max_value} times')
"""
