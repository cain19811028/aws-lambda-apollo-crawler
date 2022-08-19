#!/bin/sh

# VAR
app_name=aws-lambda-apollo-crawler
bucket_name=cain-2022
region=ap-northeast-1

main()
{
    download_chromedriver_for_mac
}

function download_chromedriver_for_mac()
{
    echo "downloading chrome driver and headless_chromium"
    # remove previous driver and binary (empty folder selenium-binaries)
    rm -rf chromedriver

    # create folder if not present
    mkdir -p chromedriver

    # download and unzip driver and binary from https://chromedriver.storage.googleapis.com/
    curl -SL https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_mac64.zip > chromedriver/chromedriver.zip
    unzip chromedriver/chromedriver.zip -d chromedriver
    rm chromedriver/chromedriver.zip

    sudo -H cp chromedriver/chromedriver /opt/chromedriver
    sudo -H ln -fs /opt/chromedriver /usr/local/bin/chromedriver
}

main "$@"