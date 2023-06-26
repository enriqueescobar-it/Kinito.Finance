#!/bin/bash
python3.8 -m venv venv ;
venv/bin/python3.8 -m pip install --upgrade pip ;

venv/bin/pip3.8 install --use-pep517 typing boto3 ;

venv/bin/pip3.8 install pandas -t pandas38/python/lib/python3.8/site-packages ;
#venv/bin/pip3.8 install --use-pep517 -r .\requirements.txt ;

venv/bin/pip3.8 install --use-pep517 typing boto3 pandas pyarrow s3fs prettytable ;
venv/bin/pip3.8 freeze > requirements-ubuntu.txt ;
venv/bin/pip3.8 install --use-pep517 -r requirements-ubuntu.txt ;

export AWS_ACCESS_KEY_ID="ASIAUJK4PF4ZA6F7UURH"
export AWS_SECRET_ACCESS_KEY="qZX0HxpKXga6vWRkSOAONl7JpoRtzaEFaa0ArBTx"
export AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEPf//////////wEaCXVzLWVhc3QtMSJHMEUCIQDfYItqLlJshhMnn0WxIR0QSVcd5VNwB6YcZwR3HheiewIgVbd8ZlXjgH4hnUKCPMrV9kNKAnerJYf3bBiClg90zPMqqQMIgP//////////ARAAGgwyOTQ5MzYwNjM3OTQiDJSPfaH2oNpA4z4J5yr9AhK+EVudunwIZfXX5oi5Q/rS8srLYelwrhvvrqbr8CD4xc0612MBMjP+l5s5NEdpr9QviTmuCd+atrAAF1nN7WZIEIbNAxBt+EpfvWB2b5vAvO4qN7QXqz9gam6cugGetB6kU51q28Rm8yFW7TkJPkyceyICuyZQQ9p7j9P95jIershl12seDgK+fQ/krnagNz3ZfSSmGO9h4CYCBcMqO/SmekQIgTcKGmGpGL6AmjLWHsgs2H3OiT2sRAogxEMtvbGk0RCanLyrJJX4RNC4Uwb2xJ3yKXYtSP/pJYT2FxdmFR9QoLqOzVz8mw3FGE9vDR0mq38gNHD23YWIH31msxkYWJgfImPre0RUDMk9Aj7DVLhAIQmFxGDGKQE6LSqDMr6rPYbQR/ABioUZA3XUouxItffO4mVJcJz7BpthzNbI4SFvoPhVcnrLcCpFTvozivN4XspSAf/YXjRTWue8nSUv8U+IdllaQdpwiKF4z4zT4d7JPszKFNaWaGkrMTCmypCfBjqmAb0FKBwUiGarS3IMbrGOJoKDQq5aFWY0GARxNKpC2cMiksbRfpf5bBf3qagA43J3VtQz+WVbid5XWoD/sR31TVXViXRZpyGvp8xzzY1ByTHO6ACffKVHndNcmUFAQGiO7t/UBFWwl+YtBbJgh9JExwKelixKjP6rAK82GnWMMBy7dZfK551Gi1V8JAXnoelSKcS34YhKLvz1k6E34xVTvtLDvDq5wKY="

export AWS_REGION="ca-central-1" ;

#echo "aws sts get-caller-identity" ;
#aws sts get-caller-identity ;

echo "aws configure sso" ;
aws configure sso ;

echo "docker build . -t lambda-handler:latest" ;
docker build . -t lambda-handler:latest ;
docker build -f Dockerfile . -t lambda-handler:latest ;

echo "docker run -p 9000:8080 lambda-handler:latest" ;
docker run -p 9000:8080 lambda-handler:latest ;

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"in_bucket": "eescobars3bucket", "in_csv": "jrv-images-id-url.csv"}' ;
