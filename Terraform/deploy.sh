#!/bin/bash
  #Clone repo
  cd /home/ubuntu && git clone https://github.com/geparedesm/aj_fencing_page.git
  # Install docker
  sudo apt-get -y update
  sudo apt-get -y install ca-certificates curl
  sudo install -m 0755 -d /etc/apt/keyrings
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
  sudo chmod a+r /etc/apt/keyrings/docker.asc
  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get -y update
  sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

  # Add docker permissions 

  sudo groupadd docker
  sudo usermod -aG docker ${USER}
  sudo chmod 666 /var/run/docker.sock
  sudo systemctl restart docker

  #Build containers
  sudo docker compose -f /home/ubuntu/aj_fencing_page/docker-compose.yaml up -d