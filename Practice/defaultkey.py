from collections import defaultdict

from collections import defaultdict

def groupWords(words):
    grouper = defaultdict(list)
    for word in words:
        length = len(word)
        grouper[length].append(word)
    return grouper
print(groupWords("seeya")['sex'])