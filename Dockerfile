# start from a small Python 3.10 image, same generation as my venv
FROM python:3.10-slim

# all the app files will live in /app inside the container
WORKDIR /app

# install the packages listed in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the project (hello.py, templates, and so on)
COPY . .

# Flask listens on 5000 inside the container.
# On the Mac, map that to 5001 because AirPlay already uses 5000:
# docker run --name pra3 -p 5001:5000 pra3-flask
EXPOSE 5000

# 0.0.0.0 means accept connections from outside the container
CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0", "--port=5000"]
