FROM python:3.10-slim-buster

# update pacakge
RUN apt-get update && apt-get insall -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
# copy to code directory 
COPY . /code

# set permissions
RUN chmod +x /code/src

RUN pip install --no-cache-dir --upgrade -r code/src/requirements.txt

# port, fastapi should use this port 
EXPOSE 8005

WORKDIR /code/src

#Allow access all the packages (python env variable) with location
ENV PYTHONPATH "${PYTHONPATH}:/code/src"

# run the cmd inside the working directory, which will use the setup.py file 
CMD pip install -e .


