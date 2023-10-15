FROM python:3.11
WORKDIR /backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY /backend/requirements.txt /backend/
RUN pip install -r requirements.txt

COPY . /backend/
CMD [ "python", "-m" , "main" ]