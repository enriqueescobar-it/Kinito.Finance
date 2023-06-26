FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt  .
RUN pip3 install install --upgrade pip
RUN pip3 install --use-pep517 requests
# pyarrow s3fs prettytable
# --target "${LAMBDA_TASK_ROOT}"
#RUN pip3 install --use-pep517 -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY lambda.py ${LAMBDA_TASK_ROOT}

CMD [ "lambda.handler" ]
