import os
import requests
import boto3
import json

from botocore.client import Config

def getFunction(bucket_name, file_name):
  print bucket_name
  return "You got {0} from the {1} bucket!".format(file_name, bucket_name)

def postFunction(bucket_name, file_name, payload):
  print payload
  return "You posted {0} to the {1} bucket!".format(file_name, bucket_name)  
