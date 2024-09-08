FROM python:3
WORKDIR /usr/src/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT [ "uvicorn" ]
CMD ["app.main:app", "--host", "0.0.0.0"]
HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1
EXPOSE 8000
