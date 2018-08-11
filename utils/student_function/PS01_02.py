def getremove_last(l):
    assert len(l)>0, "no elements"
    return l[-1], l[:-1] if len(l)>1 else []