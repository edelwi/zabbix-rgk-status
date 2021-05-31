# zabbix-rgk-status

Zabbix Template and python script with Low Level Discovery (LLD) for Lovato RGK series generating set controllers.

## Prerequisites:

    - python 3.6
    - pymodbys 2.5
    - zabbix 5

## Installation:

    - Install pymodbys module `pip install pymodbys`.
    - Fill LLD json file (/etc/zabbix/lovato/dglld.json) with generating set controllers parameters on Zabbix server or any other 
        server with access to generators.
> Example:
>```json
>{
>    "data":[
>        { "{#DGHOST}":"192.168.192.168",   "{#DGPORT}":"5005", "{#DGMEASUREFILE}":"/etc/zabbix/lovato/dgdata/dc-rgkXXX"}
>    ]
>}
>```
    - Add zbx-status.py to the cron:
>Example:
> 
>```* * * * * python3 /etc/zabbix/lovato/zabbix-rgk-status/zbx-status.py -j /etc/zabbix/lovato/dglld.json```

    - Import template lovato_rgk_templates_zabbix5.xml to the Zabbix.
    - Add Template Lovato RGK Status to appropriate server.

### Supported generating set controllers:

    - RGK 900 (SA, MC)
    - RGK 800 (AMF, SA)
    - RGK 700 (AMF, SA)
    - RGK 610

## Tested on:

    - RGK 800
    - CentOS Linux release 7.9.2009 (Core)
    - Python Python 3.6.8
    - Zabbix 5.0.7

