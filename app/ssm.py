import boto3


class SSMHelper:

    def __init__(self):
        self.ssm = boto3.client('ssm')

    def get_secret(self, secret_name):
        try:
            response = self.ssm.get_parameter(
                Name=secret_name, WithDecryption=True)

            return response['Parameter']['Value']
        except Exception as ex:
            print("exception: ", str(ex))
            return None
