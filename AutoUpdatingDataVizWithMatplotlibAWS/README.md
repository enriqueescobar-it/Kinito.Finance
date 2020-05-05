# AWS

## EC2

## S3

Simple Storage Service, popular cloud computing offerings in Amazon Web Services to store files and access them later through public-facing URLs.

To store these files, create AWS S3 `bucket`, a folder that stores files in AWS.

To do this, first navigate to the S3 dashboard within Amazon Web Services

On the right side of the Amazon S3 dashboard, click Create `bucket`

Call it `kike-first-bucket`

https://aws.amazon.com/s3/

https://s3.console.aws.amazon.com/s3/bucket/create?region=ca-central-1

Leave it for public access

Download access key CSV

### Manage Bucket

https://s3.console.aws.amazon.com/s3/buckets/kike-first-bucket/?region=ca-central-1

### Configure AWS CLI

```powershell
aws configure
```

### S3 Browser

```powershell
choco install s3browser awslambdapscore awcli
```

### Python

Use AWS SDK library for python importing `import boto3`

```bash
pip3 install boto3 -U
```