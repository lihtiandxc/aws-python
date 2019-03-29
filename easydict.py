from easydict import EasyDict as edict
import json

def lambda_handler(event, context):
    # TODO implement
    d = edict({'foo':3, 'bar':{'x':1, 'y':2}})
    output = d.foo
    print(output)   #return 3
    print(d.bar.x)  #return 1
