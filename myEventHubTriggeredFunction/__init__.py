import logging
import azure.functions as func
import json

def main(event: func.EventHubEvent):    
    for e in event:
        event_str = e.get_body().decode('utf8')
        logging.info(f'myEventHubTriggeredFunction|local|{event_str}')
