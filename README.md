Introduction to MLOps
MLOps integrates ML models into production systems and infrastructure, covering the entire ML lifecycle.
MLOps requires cross-functional collaboration among data scientists, ML engineers, IT staff, and DevOps teams.
Amazon SageMaker MLOps includes features like Amazon SageMaker Projects, SageMaker Pipelines, and SageMaker Model Registry.
SageMaker MLOps Components
SageMaker Pipelines: Creates and manages ML workflows with storage and reuse capabilities.
SageMaker Model Registry: Centralizes model tracking and simplifies deployment.
SageMaker Projects: Introduces CI/CD practices, environment parity, version control, testing, and automation.
Integration with Third-Party Tools
Built-in templates integrate with tools like Jenkins and GitHub.
Custom project templates can integrate SageMaker Pipelines with other CI/CD tools.
Solution Overview
Architecture: Automates model build pipeline including data preparation, model training, evaluation, and registration in the SageMaker Model Registry.
Deployment: Trained model is deployed to staging and production environments upon manual approval.
Detailed Components and Tools
GitHub: Used for version control and source code management.
GitHub Actions: Automates stages of the ML pipeline like data validation, model training, and deployment.
AWS CloudFormation: Initiates model deployment and sets up SageMaker endpoints.
AWS CodeStar: Links GitHub repository with AWS resources.
Amazon EventBridge: Tracks modifications in the model registry and triggers Lambda functions.
AWS Lambda: Initiates model deployment workflow in GitHub Actions.
Amazon SageMaker: Configures pipelines, endpoints, code repositories, and the model registry.
AWS Secrets Manager: Stores GitHub personal access tokens securely.
AWS Service Catalog: Implements SageMaker projects through templates.
Amazon S3: Stores model artifacts.
Prerequisites
GitHub and AWS accounts.
SageMaker Studio domain.
AWS CLI installed and configured.
AWS CodeStar connection to GitHub.
Secrets for GitHub personal access token in Secrets Manager.
IAM user for GitHub Actions with appropriate permissions.
Step-by-Step Implementation
Set up AWS CodeStar connection.
Store GitHub token in Secrets Manager.
Create IAM user for GitHub Actions.
Clone GitHub repository and configure secrets.
Deploy Lambda function and publish Lambda layer for dependencies.
Create custom SageMaker project template using provided CloudFormation template.
Deploy project from SageMaker Studio:
Create project in SageMaker Studio using custom template.
Configure environment variables in GitHub workflow files.
Final Setup
Update AWS_REGION and SAGEMAKER_PROJECT_NAME in GitHub workflow files.
Run pipelines, make changes, and push to GitHub to trigger automated pipelines.
