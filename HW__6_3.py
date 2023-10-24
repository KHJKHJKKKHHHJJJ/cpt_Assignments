exstr = "This is a more advanced comprehension exercise to practice"

wordList = exstr.split()
print([''.join(reversed(x)) for x in wordList if len(x)>=5])


