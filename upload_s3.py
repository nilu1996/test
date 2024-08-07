import urllib.request
import boto3
import time
from datetime import datetime

def send_sns_notification(topic_arn, message, region_name):
    sns_client = boto3.client('sns', region_name=region_name, verify=False)
    sns_client.publish(TopicArn=topic_arn, Message=message)
    print(f"SNS notification sent: {message}")

def check_website_availability(urls, sns_topic_arn, region_name, log_file):
    with open(log_file, 'a') as log:
        for url in urls:
            try:
                response = urllib.request.urlopen(url)
                status_code = response.getcode()
                if status_code == 200:
                    log_message = f"{datetime.now()} - Website {url} is available."
                    print(log_message)
                    log.write(log_message + '\n')
                else:
                    message = f"The website {url} is unavailable. Status code: {status_code}"
                    print(message)
                    log.write(f"{datetime.now()} - {message}\n")
                    send_sns_notification(sns_topic_arn, message, region_name)
            except Exception as e:
                message = f"Failed to connect to the website {url}: {e}"
                print(message)
                log.write(f"{datetime.now()} - {message}\n")
                send_sns_notification(sns_topic_arn, message, region_name)

if __name__ == "__main__":
    website_urls = [
        "https://alteryx.gbt.gbtad.com/",
        "https://sandboxalteryx.gbt.gbtad.com",
        "https://tableau.gbt.gbtad.com/",
        "https://uattableau.gbt.gbtad.com/"
    ]
    sns_topic_arn = "arn:aws:sns:us-east-1:090124397890:Instance-Health-monitoring"
    region_name = "us-east-1"
    log_file = "/home/svc_calinuser177/health_notificatio_scripts/website_monitoring.log"

    check_website_availability(website_urls, sns_topic_arn, region_name, log_file)
