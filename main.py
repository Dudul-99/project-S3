# Import the necessary libraries
import os
import boto3
from dotenv import load_dotenv
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION")
DIRECTORY = '.' 

def main():
    print("in main method")

    s3_client = boto3.client(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    
    # Get a list of all CSV files in the directory
    csv_files = [f for f in os.listdir(DIRECTORY) if f.endswith('.csv')]

    # Upload each CSV file to the S3 bucket
    for file_name in csv_files:
        response = s3_client.upload_file(file_name, AWS_S3_BUCKET, file_name)
        print(f"File {file_name} uploaded successfully: {response}")


if __name__ == "__main__":
    main()
