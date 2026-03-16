def ho(wagon=None):
    if wagon is None:
        return "Ho!"
    return "Ho " + wagon

print(ho(ho(ho())))
