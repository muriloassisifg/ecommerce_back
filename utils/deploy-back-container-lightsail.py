import getpass
import gzip
import os
import platform
import subprocess
import tarfile

import paramiko
import paramiko.ssh_exception
from scp import SCPClient

# Configuração inicial: Definindo as variáveis de ambiente
IMAGE_NAME = "ecommerce"
CONTAINER_SERVICE = "container-service-ecommerce"
REGION = "us-east-1"



def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def deploy_to_production():
    print(f"########################### Deploy em produção ###########################")
    commands = [
        f"docker rm -f {IMAGE_NAME}",
        f"docker build -t {IMAGE_NAME} -f Dockerfile.prod .",
        f"aws lightsail push-container-image --region {REGION} --service-name {CONTAINER_SERVICE} --label {IMAGE_NAME} --image {IMAGE_NAME}:latest",
        f"docker image prune -a -f",
        # f"docker builder prune -a"
    ]
    for command in commands:
        print(f"Executando comando: {command}")
        result = os.system(command)
        if result != 0:
            print(f"Erro ao executar comando: {command}")
            return False
    return True


def main():
    clear_terminal()
    if not deploy_to_production():
        print("Erro ao realizar o deploy.")
        return
    else:
        print(
            f"###############################################################################"
        )
        print(
            f"###########################                         ###########################"
        )
        print(
            f"###########################     Deploy Completo     ###########################"
        )
        print(
            f"###########################                         ###########################"
        )
        print(
            f"###############################################################################"
        )


if __name__ == "__main__":
    main()
