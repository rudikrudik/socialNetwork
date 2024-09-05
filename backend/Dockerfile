FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app .
ENTRYPOINT [ "uvicorn" ]
CMD ["app.main:app", "--host", "0.0.0.0"]
EXPOSE 8000