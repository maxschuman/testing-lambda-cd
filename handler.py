def handler(event, context):
    print(event)
    return {
	    "statusCode": 200,
	    "headers": {},
	    "body": "Hello, world!"
    }

def branch_handler(event, context):
	return {
		"statusCode": 200,
		"headers": {},
		"body": "bar"
	}