FROM mcr.microsoft.com/playwright:focal

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN apt install -y python3-pip && pip3 install -r requirements.txt

WORKDIR /app
ADD . /app

CMD ["pytest"]
