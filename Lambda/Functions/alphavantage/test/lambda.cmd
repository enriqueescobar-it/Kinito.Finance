echo "COPY AND PASTE YOUR CREDENTIALS AS ENV VAR"

SET AWS_ACCESS_KEY_ID=ASIAUJK4PF4ZBAA4S7W2
SET AWS_SECRET_ACCESS_KEY=CL9oVRIKHimnCeXcOJ5UYKsw4FShifTRhh4bGiXY
SET AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEIb//////////wEaCXVzLWVhc3QtMSJIMEYCIQC++/gbNGP6KPWviTi4dYgdznxtJk6Zw+lPUHcK5BZLuwIhAMum/ZV+F3AAIeBR8hmdMLPsNZWwlQ93GZU+hwTETqqYKqADCF4QABoMMjk0OTM2MDYzNzk0Igzdc59rjzd4jfTfMeEq/QKkreDAkulr2sdRal/WWqCNRHnp15Ei6mApOWlxsq+hpt4jcji8JLa4/qIEgvV7Jm2Izx+BfB64H8p0Y7QOK4krxLF1uQBELofrUWdvCaqHbbG/ngK1jfEynez6oe43Llr4if4POthfr829ECw8Ssx79yBEGzakKNeqzHUW9NvWF0iFUoVC5CW8WPkAgAA5awr+5iSiv+76ySfujbk+Yka8rtMJtn88ZzxIF3HWClm+QKbzkQBMHaYCirpOA64OpBgDuY1cXXe0VBUwZSmHzQIeYF1yfPr4OHxmWr3QcgY5nKIaiB0S1qKzIy5voPsRvg9t3/rttQJvW+TFkQlxaaByd5xBzW4JPMFE4+HaLFlKJ7HukSdrdnfxNazoiaWsLe1LaeEaBes2uvKweW7U6H577DjZSSnP3P0aH6+sYtfmp6ZMiX5IvLXYgNpWjkyPxwhtCnDgYm/If/7by8E5rGH354pdmwif5RpLpHIgrJhVbb0P9+COyL0qFPquarswzfCQoQY6pQHbD22X7F1fWn37udrbk+/3AD7t9w2LHus1ghI8FWGeRvl1gGeq+jkMWx6adn9FarJJwoTfyNK13A3V8sLMWhBQqBUsH2qmmPuRkWJBGtC52LNLlDGxnw0MaDs4POqozplL5vPq07RlQ8XCHaKHyaGP1ywoxhz94ilNYgKIX/TqYvaI3kgFnBCPd0B2VQNpxIWtEtbeBwd4grruLv9tuW1hpNzSi1A=

SET AWS_REGION=ca-central-1

echo "aws sts get-caller-identity" ;
aws sts get-caller-identity
echo "aws configure sso" ;
aws configure sso
echo "docker build . -t lambda-handler:latest" ;
docker build . -t lambda-handler:latest
echo "docker run -p 9000:8080 lambda-handler:latest" ;
docker run -p 9000:8080 lambda-handler:latest
@REM docker run -p 9000:8080 -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOCKER=$AWS_SESSION_TOCKER -e AWS_REGION=$AWS_REGION hello-world ;
@REM curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
