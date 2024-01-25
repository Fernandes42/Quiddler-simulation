import pickle

with open('trie.pkl', 'rb') as f:

    trie = pickle.load(f) # deserialize using load()
    print(trie.search("APPLE"))