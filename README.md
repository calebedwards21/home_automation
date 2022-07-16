# Home Automation
## Description
This project will include projects for home automation involving:
- sprinkler controller

## Prerequisites
### Docker
Install Docker Desktop
- Windows [Install](https://docs.docker.com/desktop/install/windows-install/)
- Linux [Install](https://docs.docker.com/desktop/install/linux-install/)

Execute the following command in terminal to start Influx, Grafana, and Chronograf in containers
> docker-compose up -d

To STOP and REMOVE the containers run the following command
> docker-compose down

The services are available on their associated ports:
- Grafana : localhost:3000
- Influx : localhost:8086
- Chronograf : No available UI / Dependent of Influx

Can also view on Docker Desktop and open url or remote in to container from there

Execute Dockerfile
> docker image build -t web_scraper:0.0.1 .