#!/bin/bash

set -e

# on-create.sh script

unset SUDO_UID
# Install a separate conda installation via Miniconda
WORKING_DIR=~/SageMaker/custom-miniconda
S3_BUCKET="your-s3-bucket-name"
S3_KEY="path/to/miniconda.sh"

# Comment the following lines if you have already run this script before
mkdir -p "$WORKING_DIR"
wget --no-check-certificate https://repo.anaconda.com/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh -O "$WORKING_DIR/miniconda.sh"

# Upload Miniconda installer file to S3
aws s3 cp "$WORKING_DIR/miniconda.sh" "s3://$S3_BUCKET/$S3_KEY"

# Remove the Miniconda installer file from local directory
rm -rf "$WORKING_DIR/miniconda.sh"

# Create a custom conda environment
source "$WORKING_DIR/miniconda/bin/activate"
conda config --add envs_dirs $WORKING_DIR/miniconda/envs
KERNEL_NAME="env-test"
PYTHON="3.8"
conda create --yes --name "$KERNEL_NAME" python="$PYTHON"
conda activate "$KERNEL_NAME"
pip install --quiet ipykernel

# Customize these lines as necessary to install the required packages
# conda install --yes numpy
# pip install --quiet boto3
