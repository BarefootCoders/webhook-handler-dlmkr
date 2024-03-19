# DialogFlow Webhook Handler Examples 

A Flask application containing two endpoints utilizing recommended approach to clickable list of deals, and show deal details. 

The intention is to illustrate the json format required for 'standard' webhook response 
to initiate successful 'fulfillment' in DialogFlow. 

### To run Flask application:
```sh
python -m venv .venv #optional?
source .venv/bin/activate #optional?
pip install -r requirements.txt
flask --app main run --port 3000 --debug
```

### Endpoints

`/list_deals`: 
 Returns a formatted 'standard' DF CX response, with richContent formatted selectable list. 
 Relevant links:
 - https://cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/fulfillment
 - https://cloud.google.com/dialogflow/cx/docs/concept/webhook#webhook-response
 - https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/WebhookResponse
 - https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/WebhookRequest

 `/show_deal`:
Returns a formatted 'standard' DF CX response, with RichContent formatted info component

### Embed Example + click handler

See [embed.html](/embed.html)

DialogFlow CX does not support passing parameters, or data when triggering an Event from client. To address, we add a listener script, and set `deal_id` session parameter before submitting custom event. 


