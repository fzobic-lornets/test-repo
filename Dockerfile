FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl git python3
RUN pip install flask requests

WORKDIR /app
COPY . .
EXPOSE 8080
CMD ["python3", "src/app.py"]
