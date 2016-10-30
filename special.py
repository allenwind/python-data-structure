import collections

tree = lambda: collections.defaultdict(tree)

dict_ = tree()

dict_['a']['b'] = 'I am OK'
print(dict_)

#json.dumps(dict_)