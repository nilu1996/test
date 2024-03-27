#!/bin/bash
set -ex

# PARAMETERS 
IDLE_TIME=600  # in seconds. Change this 
NOTEBOOK_INPUT="s3://biplt-explore/sagemaker/autostop.ipynb"
NOTEBOOK_OUTPUT="output_autostop.ipynb"

# Check if Papermill is installed
if ! command -v papermill &> /dev/null; then
    echo "Error: Papermill is not installed. Please install it using 'pip install papermill'." >&2
    exit 1
fi

# Detect Python install with boto3 install
CONDA_PYTHON_DIR=$(source /opt/conda/bin/activate base && which python)
if $CONDA_PYTHON_DIR -c "import boto3" 2>/dev/null; then
    PYTHON_DIR=$CONDA_PYTHON_DIR
elif /usr/bin/python -c "import boto3" 2>/dev/null; then
    PYTHON_DIR='/usr/bin/python'
else
    # If no boto3 found in Python or Python3, exit
    echo "No boto3 found in Python or Python3. Exiting..."
    exit 1
fi
echo "Found boto3 at $PYTHON_DIR"

# Execute autostop notebook using Papermill
papermill "$NOTEBOOK_INPUT" "$NOTEBOOK_OUTPUT" -p idle_time "$IDLE_TIME" --region "$AWS_DEFAULT_REGION"
