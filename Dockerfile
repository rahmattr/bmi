# Base Image
FROM python:latest  

# Label and Credits
LABEL \
  name="SimpleBMICalc" \
  author="Rahmat Ramadhan <rahmat.ramadhan@gmail.com>" \
  description="A Simple BMI Calculator REST API"

# Copy requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt &&  \
    rm /tmp/requirements.txt

# Make directory for app
RUN mkdir /app
WORKDIR /app
VOLUME /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]