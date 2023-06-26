# M5TDEVAYFB9PI5WM

mkdir ticker-lambda
cd ticker-lambda

touch lambda_function.py
nano lambda_function.py

python3.8 -m venv venv
.\venv\bin\activate

.\venv\Scripts\python.exe -m pip install --upgrade pip

.\venv\Scripts\python.exe -m pip install --use-pep517 requests
.\venv\Scripts\pip3.8.exe install --use-pep517 requests
pip install requests

.\venv\Scripts\pip3.8.exe freeze > requirements.txt
.\venv\Scripts\pip3.8.exe install --use-pep517 -r .\requirements.txt

zip -r lambda_function.zip lambda_function.py

aws lambda create-function --function-name my-lambda-function --runtime python3.8 --handler lambda_function.lambda_handler --role <your-lambda-role-arn> --zip-file fileb://lambda_function.zip


provider "aws" {
  region = "us-east-1"
}

resource "aws_lambda_function" "ticker_function" {
  function_name = "ticker-function"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  timeout       = 10
  memory_size   = 128

  // Replace "<path_to_lambda_function>" with the path to the directory containing lambda_function.py
  filename      = "<path_to_lambda_function>/lambda_function.py"

  environment {
    variables = {
      ALPHA_VANTAGE_API_KEY = "<your_alpha_vantage_api_key>"
    }
  }
}

output "lambda_function_arn" {
  value = aws_lambda_function.ticker_function.arn
}
