import os
import requests
import boto3
import json

from botocore.client import Config

with open('ECSconfig.json') as config_file:
  config = json.load(config_file)

def getFunction(bucket_name, file_name):
  print bucket_name
  return "You got {0} from the {1} bucket!".format(file_name, bucket_name)

def postFunction(bucket_name, file_name, payload):
  print payload
  fileJson = json.dumps(payload)
  print fileJson
  print bucket_name
  print file_name

  s3 = boto3.resource('s3',use_ssl=False,endpoint_url=config['ecs_url'],aws_access_key_id=config['ecs_user_id'],aws_secret_access_key=config['ecs_user_access_key'],config=Config(s3={'addressing_style':'path'}))

  response = s3.Object(bucket_name,file_name).put(Body=fileJson)
  print(response)

  return "You posted {0} to the {1} bucket!".format(file_name, bucket_name)  
