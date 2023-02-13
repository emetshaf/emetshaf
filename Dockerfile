FROM python:alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./ .
RUN . ./env prod
RUN python -m api.v1.app