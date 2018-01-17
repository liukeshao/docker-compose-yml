#!/usr/local/bin/python3

import subprocess

default_composes = ['mysql', 'nginx', 'postgres', 'redis']

for compose in default_composes:
    command = "/usr/local/bin/docker-compose -f " + compose + "/docker-compose.yml pull"
    print(command)
    subprocess.call(command, shell=True)

for compose in default_composes:
    command = "/usr/local/bin/docker-compose -f " + compose + "/docker-compose.yml up -d"
    print(command)
    subprocess.call(command, shell=True)

subprocess.call(["/usr/local/bin/docker", "ps"])