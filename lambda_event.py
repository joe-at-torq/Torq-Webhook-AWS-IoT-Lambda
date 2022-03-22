import json, urllib3
torq_webhook='https://hooks.torq.io/v1/webhooks/2f599...............'

def lambda_handler(event, context):
    #Send IOT Event to Torq WebHook
    payload = event
    encoded_data = json.dumps(payload).encode('utf-8')
    http = urllib3.PoolManager()
    r = http.request('POST', torq_webhook ,body=encoded_data, headers={'Content-Type': 'application/json'})
