def add_to_dict(d, key1, key2, val):
    
    if not key1 in d.keys():
        d[key1] = {}
    d[key1][key2] = val
    return d