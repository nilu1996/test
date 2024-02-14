import urllib.request
import boto3
import time

def send_sns_notification(topic_arn, message, region_name):
    sns_client = boto3.client('sns', region_name=region_name)
    sns_client.publish(TopicArn=topic_arn, Message=message)
    print("SNS notification sent successfully.")

def check_website_availability(url, sns_topic_arn, region_name):
    try:
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        if status_code == 200:
            print("Website is available.")
        else:
            message = f"The website {url} is unavailable. Status code: {status_code}"
            send_sns_notification(sns_topic_arn, message, region_name)
    except Exception as e:
        message = f"Failed to connect to the website {url}: {e}"
        send_sns_notification(sns_topic_arn, message, region_name)

if __name__ == "__main__":
    website_url = "https://devtableau.gbt.gbtad.com/"
    sns_topic_arn = "arn:aws:sns:us-east-1:090124397890:Instance-Health-monitoring"  
    region_name = "us-east-1"  # Replace with your desired AWS region
    while True:
        check_website_availability(website_url, sns_topic_arn, region_name)
        time.sleep(1800)
