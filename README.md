# aws-snapshot-alyzer

Project to manage AWS ec2 instance snapshots

## About

This is a demo project and uses boto3 to manage AWS ec2 instance snapshots.

# Configuring

shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`


# Running

`pipenv run python shotty/shotty.py` <command> <--project PROJECT_NAME>

*command* is list, start, stop
*project* is optional
