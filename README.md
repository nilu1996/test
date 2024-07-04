Hi Nilesh, Adithya
Please use STS token with IAM role for accessing S3 location, Using boto3.

I think we discussed this but was dropped somewhere in priorities. We have certain audits, and this can’t go on so please work on this change on priority.

Following processes are using S3 Secret and access keys:
GTDR Python script
Few WellsFargoBi Lambda functions

All these needs to be updated and use the STS token method.
