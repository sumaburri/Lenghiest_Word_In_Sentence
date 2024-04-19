
sentence = input('Enter a Sentence : ')
words = sentence.split()
new_l = []

for word in words:
    if word not in new_l:
        new_l.append(word)

hl=0
for word in new_l:
    if len(word) > hl:
        hl = len(word)

for word in new_l:
    if len(word)  == hl:
        print(word)


