#!/bin/sh

# VAR
app_name=aws-lambda-apollo-crawler
bucket_name=kellyapollo
region=ap-northeast-1

# PATH
selenium_lib_path=layer/chromium-binaries
python_dep_path=layer/python-dependencies

main()
{
    download_chromedriver_and_headless_chromium

    install_python_dependencies

    deploy
}

"""
Message: session not created: Chrome version must be >= 68.0.3440.0\n  (Driver info: chromedriver=2.42.591071 (0b695ff80972cc1a65a5cd643186d2ae582cd4ac),platform=Linux 4.14.214-164.339.amzn2.x86_64 x86_64)
Mapping Table:
chromedriver.zip 2.37 => headless-chromium.zip v1.0.0-41
chromedriver.zip 2.41 => headless-chromium.zip v1.0.0-47 (chrome version must be >= 67.0.3396.0)
chromedriver.zip 2.42 => headless-chromium.zip v1.0.0-51 (chrome version must be >= 68.0.3440.0)
chromedriver.zip 2.43 => headless-chromium.zip v1.0.0-55 (chrome version must be >= 69.0.3497.0)
"""
function download_chromedriver_and_headless_chromium()
{
    echo "downloading chrome driver and headless_chromium"
    # remove previous driver and binary (empty folder selenium-binaries)
    rm -r -f $selenium_lib_path/

    # create folder if not present
    mkdir -p $selenium_lib_path/

    # download and unzip driver and binary from https://chromedriver.storage.googleapis.com/
    curl -SL https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip > $selenium_lib_path/chromedriver.zip
    # curl -SL https://chromedriver.storage.googleapis.com/71.0.3578.80/chromedriver_linux64.zip > $selenium_lib_path/chromedriver.zip => fail: Message: 'chromedriver' executable may have wrong permissions
    # curl -SL https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip > $selenium_lib_path/chromedriver.zip => fail
    unzip $selenium_lib_path/chromedriver.zip -d $selenium_lib_path/
    rm $selenium_lib_path/chromedriver.zip

    # download files from: https://github.com/adieuadieu/serverless-chrome/releases/tag/v1.0.0-41
    curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip > $selenium_lib_path/headless-chromium.zip
    unzip $selenium_lib_path/headless-chromium.zip -d $selenium_lib_path/
    rm $selenium_lib_path/headless-chromium.zip
}

function install_python_dependencies()
{
    sudo -H rm -r -f ${python_dep_path}
    sudo -H mkdir -p ${python_dep_path}/python/lib/python3.7/site-packages
    sudo -H python3 -m pip install --upgrade pip
    sudo -H python3 -m pip install -r requirements.txt -t ${python_dep_path}/python/lib/python3.7/site-packages
}

function deploy()
{
    sam deploy --template-file template.yaml --stack-name $app_name --s3-bucket $bucket_name --region $region --profile default --capabilities CAPABILITY_NAMED_IAM
}

main "$@"