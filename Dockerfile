FROM python:3.11.5

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /src/My_App

EXPOSE 8000

CMD [ "python", "app.py" ]