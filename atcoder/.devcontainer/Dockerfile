FROM python:3.8-bullseye

RUN apt-get update &&\
    apt-get install -y apt-utils dialog

RUN apt-get upgrade -y&&\
    apt-get install -y libboost-dev google-perftools libgoogle-perftools-dev gcc g++ make wget bzip2

# to use Japanese
RUN apt-get install -y -f locales

RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

RUN useradd -m -d /home/docker -s /bin/bash docker
RUN pip install --upgrade pip

CMD /bin/bash
