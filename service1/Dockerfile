FROM python:latest

RUN curl -sL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog
    
RUN  ./deploy --version_service1=v1.0

ENV fprocess="python2 entrypoint.py"
COPY entrypoint.py /

EXPOSE 8080
CMD [ "fwatchdog" ]
