FROM python:3
WORKDIR /usr/src/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app .
COPY .env .
ENTRYPOINT [ "uvicorn" ]
CMD ["main:app", "--host", "0.0.0.0"]
EXPOSE 8000