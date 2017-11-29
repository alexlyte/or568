# from boto.s3.connection import S3Connection

# conn = S3Connection('access-key','secret-access-key')
# bucket = conn.get_bucket('bucket')
# for key in bucket.list():
#     print key.name.encode('utf-8')

import boto3
import botocore
#client = boto3.client('s3') #low-level functional API
#all_objects =  client.list_objects(Bucket = 'kaggle-tsa')
#print(all_objects)
#KEY = "sample/00360f79fd6e02781457eda48f85da90.aps"
KEY = "tsa_datasets/stage1/aps/00360f79fd6e02781457eda48f85da90.aps"

s3 = boto3.resource('s3') #high-level object-oriented API

try:
    my_bucket = s3.Bucket('kaggle-tsa').download_file(KEY,'./00360f79fd6e02781457eda48f85da90.aps') 
    print(my_bucket)
    #subsitute this for your s3 bucket name. 
except botocore.exceptions.ClientError as e:
    print(e)

# import pandas as pd

# obj = client.get_object(Bucket='kaggle-tsa', Key='path/to/my/table.csv')
# grid_sizes = pd.read_csv(obj['Body'])


# from io import BytesIO

# obj = client.get_object(Bucket='my-bucket', Key='path/to/my/array.npy')
# array = np.load(BytesIO(obj['Body'].read()))



