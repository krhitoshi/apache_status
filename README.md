# apache_status

A Python script and a Zabbix template to retrieve and monitor Apache status data.

## Installation

```
ExtendedStatus On
<Location /server-status>
    SetHandler server-status
    Require ip ::1
</Location>
```

```
$ sudo apachectl -t
$ sudo apachectl graceful
```

```
$ curl http://localhost//server-status?auto
Total Accesses: 79820
Total kBytes: 400659
CPULoad: 7.89602e-6
Uptime: 7092181
ReqPerSec: .0112546
BytesPerSec: 57.8489
BytesPerReq: 5140
BusyWorkers: 1
IdleWorkers: 4
Scoreboard: ___.W_..........................................................................................................................
```

```
$ git clone https://github.com/krhitoshi/apache_status.git
$ sudo cp apache_status/apache_status.py /usr/local/bin/
$ sudo cp apache_status/userparameter_apache.conf /etc/zabbix/zabbix_agentd.d/
$ sudo systemctl restart zabbix-agent.service
```

```
$ /usr/local/bin/apache_status.py total_accesses
79832
```

```
$ zabbix_agentd -t "apache.total_accesses"
apache.total_accesses                         [t|79838]
```
