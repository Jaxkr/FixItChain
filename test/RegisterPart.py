from boa.blockchain.vm.Neo.Runtime import CheckWitness
from boa.blockchain.vm.Neo.Storage import GetContext, Put, Delete, Get
from boa.code.builtins import concat


def Main(op, k, v):
    return_val = -999
    context = GetContext()

    # With opcode 1, we create a new itemID, and mark our first repair
    if (op == 1):
        Put(context, k, v)
        return_val = k
        print(k)
    # With opcode 2, we can get the repairs for a given item
    elif (op == 2):
        v = Get(context, k)
        return_val = v
    # With opcode 3, we can append another repair to a given item
    elif (op == 3):
        o = Get(context, k)
        n = concat(o, ";")
        n = concat(n, v)
        Put(context, k, n)
        return_val = n
    

    return return_val