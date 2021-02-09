import json

def buildTrie(words):
    root = {}

    for word in words:
        curr = root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['-'] = word 

    return root

root = buildTrie(["support", "sup", "salt", "sal", "salvage"])
print(json.dumps(root))
