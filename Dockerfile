FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN chmod +x entrypoint.sh
# RUN chown root entrypoint.sh

RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["sh", "entrypoint.sh"]