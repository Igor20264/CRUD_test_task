FROM python:3.10-slim-buster
LABEL authors="Hlebushek"

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --root-user-action=ignore --upgrade -r /code/requirements.txt
COPY . .

EXPOSE 8000
CMD ["uvicorn","main:app","--host","0.0.0.0","--port", "8000"]
