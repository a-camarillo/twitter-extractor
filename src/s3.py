import boto3
import os
import json

def read_credentials(file_path):
    ''' get credentials from given json file path '''
    with open(file_path,'r') as f:
        credentials = json.load(f)
    return credentials

def initialize_client(service,access_key,secret_access_key):
    ''' initializes an AWS client using boto3 '''
    client = boto3(service,access_key,secret_access_key)
    return client

def file_to_s3(file_path,aws_client,bucket_name,file_key):
    ''' uploads file into s3 bucket '''
    if os.listdir(file_path):
        for item in os.listdir(file_path):
            aws_client.upload_file(file_path+item,bucket_name,file_key)
        print('files uploaded to s3')
    else:
        print('no files in given directory')
       
