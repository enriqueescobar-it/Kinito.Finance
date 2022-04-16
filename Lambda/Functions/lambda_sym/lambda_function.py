import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    # TODO implement
    bucket_list = []
    
    for bucket in s3.buckets.all():
        bucket_list.append(bucket.name)

    return {
        "statusCode": 200,
        "body": bucket_list
    }
