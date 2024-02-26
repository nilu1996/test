Hello Chandan,

Here are the steps we've taken and the observations:

1. We initiated the creation of a test AWS SageMaker domain in the sandbox account.
2. Upon creation, SageMaker tiles appeared on the AWS Access console.
3. We followed the process outlined in the shared link.
4. To restrict access, we attempted to transition the tiles from the AWS console to the Okta setup. Integration of the tile creation URL with the Okta setup was successful.
5. However, attempting to add users from Okta did not grant access until we added users from the AWS SageMaker domain setup.
6. Our efforts to limit access involved creating roles such as Data Scientists, MLOps Engineers, etc., as suggested by AWS documentation. We aimed to assign persona-based access within SageMaker.
7. Unfortunately, when we created these roles and attached them to specific users, they were added alongside existing roles previously created with AWS SageMaker.
8. To address this issue, I plan to schedule a call with the AWS team, including the IAM team, on Wednesday to seek further clarification and resolve these challenges.

Please let me know if you need any additional information or if there are further actions to be taken.

Thank you.
