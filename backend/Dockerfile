FROM python:3.11-slim-buster as builder
WORKDIR /backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /backend/
RUN pip install -r requirements.txt

FROM python:3.11-slim-buster
WORKDIR /backend
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /opt/venv /opt/venv
COPY . /backend/
CMD [ "python", "./main.py" ]