import yaml
from jinja2 import Environment, FileSystemLoader
import os


if not os.path.exists('./generated'):
    os.makedirs('./generated')

if not os.path.exists('./generated/configuration'):
    os.makedirs('./generated/configuration')


# set current directory
ENV = Environment(loader=FileSystemLoader('.'))

# Get configuration variable
with open("config.yaml") as y:
    configuration = yaml.load(y, Loader=yaml.Loader)

##### Generate atomix configuration #####

 # get template
baseline = ENV.get_template("./template/atomix.conf.j2")
# create file
file = open('./generated/configuration/atomix.conf', 'w')
# Generate config
config = baseline.render(data=configuration)
# Store in file
file.write(config)
file.close

##### Generate onos configuration #####

# get template
baseline = ENV.get_template("./template/cluster.json.j2")
# create file
file = open('./generated/configuration/cluster.json', 'w')
# Generate config
config = baseline.render(data=configuration)
# Store in file
file.write(config)
file.close


# ##### Generate docker compose configuration #####

# get template
baseline = ENV.get_template("./template/docker-compose.yaml.j2")

# create file
file = open('./generated/docker-compose.yaml', 'w')

# create config
config = baseline.render(data=configuration)

file.write(config)
file.close