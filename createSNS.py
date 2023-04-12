import boto3
from configparser import ConfigParser
from config import Name,email1,email2

#initialize AWS SNS
client = boto3.client('sns')

#creating topic
response = client.create_topic(Name= "Name")
print('topic created')


# ARN of the newly created SNS topic
myfirsttopic_arn = response['TopicArn']

# email subscription for the topic created
response = client.subscribe(
    TopicArn=myfirsttopic_arn,
    Protocol='email',
    Endpoint=email1
    
)
response = client.subscribe(
    TopicArn=myfirsttopic_arn,
    Protocol='email',
    Endpoint=email2
    
)

# Print the subscription ARN
print(response['SubscriptionArn'])