{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<YOUR_ACCOUNT_ID>:group/mlopssagemakeruser"
            },
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::s3awssagemaker",
                "arn:aws:s3:::s3awssagemaker/*"
            ]
        }
    ]
}
