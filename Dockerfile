FROM ubuntu:latest
# FROM python:3.6.9-buster

WORKDIR /usr/src/py-hr
COPY . /usr/src/py-hr

RUN apt update -y && apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.6

# RUN pip install -e .
# RUN pip install pytest pytest-mock
# RUN pip install ipython
# RUN pip install grp
# RUN pip install pipenv pytest
# RUN pipenv install pytest
# RUN pipenv shell
# RUN make

# CMD ["pipenv", "run", "python", "--version"]
CMD ["python", "--version"]
