import json

def lambda_handler(event, context):
    e = event
    eObjsDump = json.dumps(e)
    eObjsLoad = json.loads(eObjsDump)
    # print(eObjsLoad['Service'])
    try:
        if eObjsLoad['Service'] == 'Warmer':  # configure cloudwatch rule with Rate and and Constant JSON input to have Service as Key and Warmer as Value
            return False
    except Exception as error:
        return False
