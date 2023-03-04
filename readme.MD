----
Run `start.sh` to setup and run the file
---

Run this to generate the config files for docker
```
python3 generate.py
```

It always expects a config.yaml in current directory. The config.yaml should be in the following format:
```
atomix_docker: atomix/atomix:3.1.12
onos_docker: onosproject/onos:2.7.0

self:
  hostname_onos: onos-1
  ip_onos: 13.233.216.209
  hostname_atomix: atomix-1
  ip_atomix: 13.233.216.209

atomix:
- hostname: atomix-1
  ip: 13.233.216.209
- hostname: atomix-2
  ip: 3.109.132.79
- hostname: atomix-3
  ip: 65.2.29.57


onos:
- hostname: onos-1
  ip: 13.233.216.209
- hostname: onos-2
  ip: 3.109.132.79
- hostname: onos-3
  ip: 65.2.29.57
```
