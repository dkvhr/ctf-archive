FROM ubuntu:latest

RUN apt update -y && apt install gcc socat -y

WORKDIR /app

COPY . .

RUN gcc -fno-stack-protector -no-pie -zexecstack -o program program.c

RUN mv flag.txt /flag.txt

RUN mv entrypoint.sh /entrypoint.sh && chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
