import json

def lambda_handler(event, context):
    e = event
    eObjsDump = json.dumps(e)
    eObjsLoad = json.loads(eObjsDump)
    # print(eObjsLoad['Service'])
    try:
        if eObjsLoad['Service'] == 'Warmer':  # configure cloudwatch rule with Rate and and Constant JSON input to have Service as Key and Warmer as Value
            return False # for warming purpose, so to terminate the function ASAP when the service is equal to warmer
    except Exception as error:
        return False # the event JSON object can come in with different Key, so Catch the error and terminate the function
