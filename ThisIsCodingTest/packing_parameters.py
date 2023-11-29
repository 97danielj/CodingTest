# positional arguments 만 받을 때
def save_ranking(*args):
    print(args)
save_ranking('ming', 'alice', 'tom', 'wilson', 'roy')

def save_ranking2(**kwargs):
    print(kwargs)
save_ranking2(first='ming', second='alice', fourth='wilson', third='tom', fifth='roy')