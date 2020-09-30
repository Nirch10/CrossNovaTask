
FROM python:3.7
LABEL maintainer "Nir <localhost@host.com>"
WORKDIR /code
COPY requirements.txt .
# Install dependencies
RUN pip3 install -r requirements.txt
COPY . .
# ADD DBQuery.py ./Task1/WebApp/DBQuery
#ADD Config.py /code/Task1/AppConfig/Config.py
# ADD App.py ./Task1/WebApp/App.py
EXPOSE 8050
CMD ["python", "/code/main.py"]