#Mozda nisam dobro razumijo ovo sam napravio da pokrenem u terminalu s komanodom python script.py 
#Sad ak je trebo ukomponirat u kreiranju image onda bi treblo dodati u Dockerfile npr:
# ....
# ...... 
# RUN: script.py
# ........... 
# CMD["...","script.py"]
# a može i u docker-compose ali bi drugačije trebala izgledat skripta.
import subprocess


#Postavi  versions za services
SERVICE1_VERSION = "v1.0"
SERVICE2_VERSION = "v1.0"

 #Build image za service1 s tag-om
subprocess.run(["docker", "build", "-t", f"service1:{SERVICE1_VERSION}", "-f", "service1/Dockerfile", "service1/"])

 #Build image za service2 s tag-om
subprocess.run(["docker", "build", "-t", f"service2:{SERVICE2_VERSION}", "-f", "service2/Dockerfile", "service2/"])

# Komanda za pokretanje  Docker Compose za startanje microservices-a
subprocess.run(["docker-compose", "up", "-d", "--build"])


