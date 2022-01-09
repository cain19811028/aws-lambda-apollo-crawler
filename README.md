# aws-lambda-apollo-crawler

#### Development
```bash
sh deploy.sh

or

sudo pip3 install -r requirements.txt --upgrade --target layer/python-dependencies

sam deploy --template-file template.yaml --stack-name aws-lambda-apollo-crawler --s3-bucket cain-2021 --region ap-northeast-1 --profile default --capabilities CAPABILITY_NAMED_IAM
```

#### Resolve chromedriver unexpectedly exited. Status code was: -9
```bash
xattr -d com.apple.quarantine /usr/local/bin/chromedriver
```