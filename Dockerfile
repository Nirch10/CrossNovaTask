# FROM python:3.7
# COPY . /app
# WORKDIR /app
# RUN pip3 install -r requirements.txt
# EXPOSE 5000
# CMD python ./Task1/WebApp/__init__.py
FROM python:3.7
LABEL maintainer "Nir <localhost@host.com>"
WORKDIR /code
COPY requirements.txt .
# Install dependencies
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH="/"
RUN pip3 install -r requirements.txt
# ADD DBQuery.py ./Task1/WebApp/DBQuery
 ADD Config.py /code/Task1/AppConfig/Config.py
# ADD App.py ./Task1/WebApp/App.py
COPY ./ ./
EXPOSE 8050
CMD ["python", "/code/Task1/WebApp/__init__.py"]