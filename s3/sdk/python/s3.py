import boto3
import sys
import random
import os

def main():
    if len(sys.argv) < 2:
        print("Error: Exactly one argument is required.")
        print(f"Usage: python {sys.argv[0]} <bucket-name>")
        sys.exit(1)

    # Assigning command-line argument to bucketName
    bucketName = sys.argv[1]
    region = 'ap-southeast-2'

    # Getting client
    client = boto3.client('s3', region_name=region)
    
    # Creating bucket
    try:
        response = client.create_bucket(
            Bucket=bucketName,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
        print("Bucket created:", response)
    except client.exceptions.BucketAlreadyExists:
        print(f"Bucket '{bucketName}' already exists.")
    except client.exceptions.BucketAlreadyOwnedByYou:
        print(f"Bucket '{bucketName}' is already owned by you.")

    # Generating a random number of files between 1 and 6
    fileNumber = 1 + random.randint(0, 6)

    for i in range(fileNumber):
        fileName = f"file_{i}.txt"
        filePath = "/tmp/"
        outputPath = os.path.join(filePath, fileName)
        os.makedirs(filePath, exist_ok=True)

        # Creating a random content file
        with open(outputPath, 'w') as f:
            f.write(f"{random.randint(10000, 1000000)}")

        # Uploading the file to S3
        with open(outputPath, 'rb') as data:
            response = client.put_object(
                Bucket=bucketName,
                Key=fileName,
                Body=data
            )
        print(f"Uploaded {fileName} to bucket {bucketName}")

if __name__ == "__main__":
    main()
