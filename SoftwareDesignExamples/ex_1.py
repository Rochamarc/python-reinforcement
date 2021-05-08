# Example 1 - Common Degin Mistakes
#
#

list_of_words = ['hello', 'yes', 'goodbye', 'last', 'hello']
print(list_of_words[0] + "," + list_of_words[1] + "," + list_of_words[2] + "," + list_of_words[3])

# solution 2

to_print = ""

for i in range(len(list_of_words)):
	to_print += list_of_words[i]
	if i != len(list_of_words) - 1:
		to_print += ","

print(to_print)

# Solution 3
print(",".join(list_of_words))

# Solution 4
# better
DELIMITER = ","
print(DELIMITER.join(list_of_words)) 