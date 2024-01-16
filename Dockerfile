# Use an official Python image

FROM python

# Set the Working Directory inside the container

WORkDIR /usr/scr/app

# Copy the current dictory into container directory /usr/scr/app

COPY . .

# install the dependency

RUN pip install -r requirements.txt

# Run the application

CMD ["python", "./random_fact.py"]
