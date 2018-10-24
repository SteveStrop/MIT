def how_many(aDict):
    return sum(len(v) for v in aDict.values())


def do_biggest(aDict):
    try:
        return max((len(v), k) for k, v in aDict.items())[1]
    except ValueError:
        return 'None'


def biggest():
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'e': ['frog']}

    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    return do_biggest({})
