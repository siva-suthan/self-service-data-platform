import requests
import boto3
import os
import json

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_params(latest_record_timestamp,credentials):
    """
        This function forms the base_url, payload, header
    """
    base_url = credentials.host

    headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "authorization": "Basic U1B1c2VybmFtZTpTUHBhc3N3b3Jk"
    }

    payload = {
        "credentials": "",
        "parse": False,
        "url": base_url
    }

    return base_url, payload, headers



def get_api_secrets(api_name):
    """
        This function is used to retreive the credentials stored in the secret manager
        {'engine': 'mysql',
        'host': 'twitterapp2.abcdefg.us-east-1.rds.amazonaws.com',
        'password': '-)Kw>THISISAFAKEPASSWORD:lg{&sad+Canr',
        'port': 3306,
        'username': 'ranman'}
    """

    secrets = boto3.client("secretsmanager")
    rds = json.dumps(secrets.get_secret_value(SecretId=api_kms_name)['SecretString'])
    print(rds)
    return rds
    
def get_latest_record_timestamp(api_name):
    """
        This function returns the latest record timestamp
    """
    timestamp = ''
    return timestamp

def get_data(base_url, payload, header):
    """
        This function will extract and store data to the relavant db
        and returns new ltest record timestamp
    """
    response = requests.post(url, json=payload, headers=headers)

    df = pd.Dataframe(json.loads(response.json))
    df.to_sql()
    new_latest_record_timestamp = max(df['timestamp'])

    return new_latest_record_timestamp
    
def update_latest_record_timestamp(new_latest_record_timestamp):
    """
        This function will update the status table with the new value
    """

        
def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    api_name = event.get('api_name')
    credentials = get_api_secrets(api_name)

    latest_record_timestamp = get_latest_record_timestamp(api_name)

    base_url, payload, header = get_params(latest_record_timestamp,credentials)

    new_latest_record_timestamp = get_data(base_url, payload, header)

    update_latest_record_timestamp(new_latest_record_timestamp)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "latest_record_timestamp ": new_latest_record_timestamp
        })
    }