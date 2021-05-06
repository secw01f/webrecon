#! /bin/bash

if [ $# == 0 ]
then
  echo "wrS3subtakeover.sh"
  echo "Takes a WebRecon directory as an argument and searches for subdomain takeovers based on AWS S3 buckets that have been removed and CNAME DNS entries"
  echo ""
  echo "Usage:"
  echo "./wrS3subtakeover.sh example/"
  echo "sh wrS3subtakeover.sh example/"
  exit
fi

cd $1
cd "out/"

domains=()

options=$(cat index | grep "(404" | awk 'BEGIN { FS = "[ /]" }{print $6}')

for option in $options; do
  domains+=($option)
done

for domain in "${domains[@]}"; do
  cd $domain && echo "___________________________________" &&echo $domain && dig CNAME $domain | grep "s3" && echo ""
  files=$(ls | grep -v "aquatone" | grep -v "gf")
  for file in $files; do
    echo "Filename: $file" && cat $file | grep "Code" && cat $file | grep "BucketName" && echo "___________________________________"
  done
  echo ""
  cd ..
done
