# Zabbix Lovato RGK Integration

A production-ready Python integration for monitoring **Lovato RGK** generator controllers with **Zabbix**.

The project collects operational data from multiple Lovato RGK controllers over **Modbus TCP** and automatically publishes it to Zabbix using **Low-Level Discovery (LLD)**. It was originally developed for a production environment to automate monitoring of diesel generator controllers deployed across multiple locations.

---

## Features

- Automatic device discovery using Zabbix Low-Level Discovery (LLD)
- Polls Lovato RGK controllers over Modbus TCP
- Supports monitoring multiple generators from a single configuration
- Automatic creation of Zabbix items through LLD
- Designed for scheduled execution via cron
- Production-tested

---

## Supported Controllers

| Controller | Supported | Tested |
|------------|-----------|--------|
| RGK 900 (SA, MC) | ✅ | — |
| RGK 800 (AMF, SA) | ✅ | ✅ |
| RGK 700 (AMF, SA) | ✅ | — |
| RGK 610 | ✅ | — |

---

## Architecture

```
                +----------------------+
                |  Lovato RGK Devices  |
                +----------+-----------+
                           |
                      Modbus TCP
                           |
                           ▼
                 Python Collector
                           |
                  Discovery + Metrics
                           |
                           ▼
                    Zabbix Server
                           |
                 Low-Level Discovery
                           |
            Items • Triggers • Graphs
```

The collector periodically polls all configured controllers, discovers available devices, and exposes operational metrics to Zabbix through a reusable LLD template.

---

## Background

This project was developed for a production infrastructure where multiple diesel generator controllers had to be monitored continuously.

The primary goal was to eliminate manual Zabbix configuration by automatically discovering generators and collecting their operational metrics on a scheduled basis. Once configured, new devices could be added simply by updating the discovery configuration without modifying the monitoring template.

---

## Requirements

- Python 3.6+
- Zabbix 5.x
- `pymodbus`
- Network connectivity to Lovato RGK controllers

---

## Installation

Clone the repository:

```bash
git clone https://github.com/edelwi/zabbix-rgk-status.git
cd zabbix-rgk-status
```

Install dependencies:

```bash
pip install pymodbus
```

Configure the discovery file:

```json
{
    "data": [
        {
            "{#DGHOST}": "192.168.192.168",
            "{#DGPORT}": "5005",
            "{#DGMEASUREFILE}": "/etc/zabbix/lovato/dgdata/dc-rgk001"
        }
    ]
}
```

Schedule the collector with cron:

```cron
* * * * * python3 /etc/zabbix/lovato/zabbix-rgk-status/zbx-status.py \
    -j /etc/zabbix/lovato/dglld.json
```

Import the supplied Zabbix template:

```
lovato_rgk_templates_zabbix5.xml
```

Finally, attach the template to the appropriate host.

---

## How It Works

1. Read the LLD configuration file.
2. Discover configured Lovato RGK controllers.
3. Poll each controller over Modbus TCP.
4. Collect operational metrics.
5. Publish metrics to Zabbix.
6. Let Zabbix automatically create and maintain monitoring items through Low-Level Discovery.

---

## Technologies

- Python
- Modbus TCP
- Zabbix
- Zabbix Low-Level Discovery (LLD)
- Cron

---

## Production Status

This integration was successfully deployed in a production environment to monitor diesel generator controllers and automate their integration with Zabbix.

The repository is published as a reference implementation of a lightweight industrial monitoring integration built with Python.

---

## License

MIT License
