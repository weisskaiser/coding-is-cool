words = ["dog", "deer", "deal","dealer"]
trie:dict = {}

def query(prefix):

    i_trie = trie
    for c in prefix:
        if c in i_trie:
            i_trie = i_trie[c]
        else:
            return []

    return get_rec(prefix, i_trie)

def get_rec(prefix, trie):
    lst = []
    if '$' in trie:
        lst.append(prefix)
    for c in trie.keys():
        if c != '$':
            lst.extend(get_rec(prefix+c,trie[c]))
    return lst

def addToTrie(trie:dict, arg:str):

    for c in arg:
        if c in trie:
            trie = trie[c]
        elif c not in trie:
            trie[c] = {}
            trie = trie[c]
    trie['$'] = {}

for word in words:
    addToTrie(trie, word)

assert query("de") == ["deer", "deal","dealer"]