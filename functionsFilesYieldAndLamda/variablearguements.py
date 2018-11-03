def var_args(name , *args):
    print(name)
    print(args)

## Pay attention to signature
def var_args_withkeys(name , **kwargs):
    print(name)
    print(kwargs["description"],kwargs["feedback"],kwargs["subscriber"])
