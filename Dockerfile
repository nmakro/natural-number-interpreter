FROM  python:3.6

RUN mkdir /home/nnp

WORKDIR /home/nnp

RUN mkdir /home/app/dist

COPY . .

RUN chmod +x bin/interpreter
