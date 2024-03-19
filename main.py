from flask import Flask, request, jsonify
import json

app = Flask(__name__)

"""
 Returns a formatted 'standard' DF CX response, with richContent formatted selectable list. 
 Relevant links:
 - https://cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/fulfillment
 - https://cloud.google.com/dialogflow/cx/docs/concept/webhook#webhook-response
 - https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/WebhookResponse
 - https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/WebhookRequest
 """
@app.post("/list_deals")
def list_deals():
  req_data = request.get_json()
  print(json.dumps(req_data))

  deals = mock_deals_list()
  rich_content = [list_item_from_deal(deal) for deal in deals["items"]]

  return jsonify(
     {
       'fulfillment_response': {
          'messages': [
            {
              "payload": {
                "richContent": [
                  rich_content
                ]
              },
            }
          ]
        }
     }
  )

"""
Returns a formatted 'standard' DF CX response, with RichContent formatted info component
"""
@app.post("/show_deal")
def show_deal():
  req_data = request.get_json()
  print(json.dumps(req_data))

  deal_id = req_data["sessionInfo"]["parameters"]["deal_id"]
  print(deal_id)

  deal = mock_deal(deal_id);

  return jsonify({
    'fulfillment_response': {
      'messages': [
        { 
          "payload": {
            "richContent": [
              [
                {
                  "type": "info",
                  "title":deal["title"],
                  "subtitle": deal["state"]
                }
              ]
            ]
          },
        }
      ]
    }
  })
  
def list_item_from_deal(deal):
  return {
    "title": deal["title"],
    "type": "list",
    "event": {
      "event": f'deal_selected_{deal["id"]}',
    }
  }

def mock_deals_list():
  return {
    "items": [
      {
        "id": 1,
        "title": "Deal One",
        "state": "draft",
        "currency": "USD",
        "security_type": "string",
        "price_per_security": 0.1,
        "minimum_investment": 0,
        "maximum_investment": 0,
        "issuer": {},
        "enterprise": {},
        "deal_type": "other_or_unknown",
        "investors": {},
        "funding": {}
      },
      {
        "id": 2000,
        "title": "Deal Two Thousand",
        "state": "draft",
        "currency": "USD",
        "security_type": "string",
        "price_per_security": 0.1,
        "minimum_investment": 0,
        "maximum_investment": 0,
        "issuer": {},
        "enterprise": {},
        "deal_type": "other_or_unknown",
        "investors": {},
        "funding": {}
      }
    ]
  }

def mock_deal(id: None):
  deal = None
  if id:
    deals = mock_deals_list()
    deal = next((deal for deal in deals["items"] if deal["id"] == int(id)), None)
  
  return deal if deal else mock_deals_list()["items"][0]
