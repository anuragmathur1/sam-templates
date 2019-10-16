# sam-templates
1. ec2-schedule-lambda : SAM template for functions to start and stop ec2 instances based on tags and triggered by cloudwatch events
  $sam package --template-file template.yaml --output-template packaged.yaml --s3-bucket <your-bucket-name> --debug
  $sam deploy --template-file packaged.yaml --stack-name ec2-schedule-lambda --capabilities CAPABILITY_IAM
