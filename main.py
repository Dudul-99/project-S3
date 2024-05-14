import os
import boto3
from dotenv import load_dotenv

load_dotenv()
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION")
LOCAL_FILE="data_team_finale.csv"
NAME_FOR_S3="data_team_finale.csv"


def main():
    print("in main method")

    s3_client = boto3.client(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    
    response = s3_client.upload_file(LOCAL_FILE, AWS_S3_BUCKET, NAME_FOR_S3)

    print("File uploaded successfully: {response}")


if __name__ == "__main__":
    main()
