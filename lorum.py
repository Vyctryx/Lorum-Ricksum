import random
import re
from random import randint
import argparse
import string

# Lyrics and puctuation
# Note - do not put spaces after commas in strings!
a = "we're no strangers to love"
b = "you know the rules and so do I"
c = "you know the rules and so do I"
d = "a full commitment's what I'm thinking of"
e = "you wouldn't get this from any other guy"
f = "I just wanna tell you how I'm feeling"
g = "gotta make you understand"
h = "never gonna give you up"
i = "never gonna let you down"
j = "never gonna run around and desert you"
k = "never gonna make you cry"
l = "never gonna say goodbye"
m = "never gonna tell a lie and hurt you"
n = "we've known each other for so long"
o = "your heart's been aching but you're too shy to say it"
p = "inside we both know what's been going on"
q = "we know the game and we're gonna play it"
r = "and if you ask me how I'm feeling"
s = "don't tell me you're too blind to see"
filler_a = "ooh"
filler_b = "give you up"
filler_c = "never gonna give,never gonna give"
pu_a = "."
pu_b = ","
pu_c = "!"

# sentence and filler lists
sen = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]
fill = [filler_a, filler_b, filler_c]

# ratio lists
dist = [sen, sen, sen, fill]
punc = [pu_a, pu_a, pu_a, pu_a, pu_b, pu_b, pu_b, pu_b, pu_b, pu_b, pu_b, pu_c]
final_punc = [pu_a, pu_a, pu_a, pu_c]

parser = argparse.ArgumentParser()
parser.add_argument("n")
args = parser.parse_args()

# check for sentence-ending punctuation and capitalize
def uppercase_sentences(blob):
	expr = "\.|!"

	cap_lines = []

	lines = re.split(expr, blob)
	punct = re.findall(expr, blob)

	lines = [l for l in lines if l.strip()]

	for li in lines:
		li = li[:1].upper() + li[1:]
		cap_lines.append(li)

	result = ""

	for ind in range (0,len(lines)):
		result += cap_lines[ind]
		try:
			result += punct[ind] + " "
		except: pass

	return result

#####

for pa in range(0, int(args.n)):

	sentence = []
	num_sentences = randint(10, 40)

	# append strings to make a paragraph
	for it in range(0, num_sentences):
		sentence.append(random.choice(random.choice(dist)))
		sentence.append(random.choice(punc))

	blob = "".join(sentence)
	blob = uppercase_sentences(blob)
	blob = blob.strip()

	if blob[-1] in string.punctuation:
		blob = blob[:-1]
	
	blob = blob + random.choice(final_punc) + "\n"
	blob = blob.replace(",", ", ")
#	print blob
	return blob
