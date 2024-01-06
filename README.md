# aws-lambda-apollo-crawler

#### Development
```bash
sh deploy.sh

or

sudo pip3 install -r requirements.txt --upgrade --target layer/python-dependencies

sam deploy --template-file template.yaml --stack-name aws-lambda-apollo-crawler --s3-bucket cain-2023 --region ap-northeast-1 --profile default --capabilities CAPABILITY_NAMED_IAM
```

#### Resolve FileNotFoundError: [Errno 2] No such file or directory: '/opt/chromedriver'
```
sudo cp layer/chromium-binaries/chromedriver /opt/chromedriver
sudo ln -fs /opt/chromedriver /usr/local/bin/chromedriver

sudo cp layer/chromium-binaries/headless-chromium /opt/headless-chromium
sudo ln -fs /opt/headless-chromium /usr/local/bin/headless-chromium
```

#### Resolve chromedriver unexpectedly exited. Status code was: -9
```bash
xattr -d com.apple.quarantine /usr/local/bin/chromedriver
```