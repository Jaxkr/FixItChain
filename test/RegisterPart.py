from boa.blockchain.vm.Neo.Runtime import CheckWitness
from boa.blockchain.vm.Neo.Storage import GetContext, Put, Delete, Get
from boa.code.builtins import concat


def Main(op, k, v):
    return_val = -999
    context = GetContext()

    if (op == 1):
        Put(context, k, v)
        return_val = k
        print(k)
    elif (op == 2):
        v = Get(context, k)

        return_val = v

    return return_val