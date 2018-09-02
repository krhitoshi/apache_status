#!/usr/bin/env python

import sys
import requests


class ApacheStatus:
    url = 'http://localhost/server-status?auto'
    indexes = {'total_accesses': 'Total Accesses:',
               'total_kbytes': 'Total kBytes:',
               'cpu_load': 'CPULoad:',
               'uptime': 'Uptime:',
               'busy_workers': 'BusyWorkers:',
               'idle_workers': 'IdleWorkers:'}

    def __init__(self, argv):
        self.argv = argv
        self.program_name = self.argv[0]

    def arg_error(self):
        usage = 'Usage: %s %s' % (self.program_name,
                                  '|'.join(ApacheStatus.indexes.keys()))
        sys.exit(usage)

    def get_apache_status(selfl):
        r = requests.get(ApacheStatus.url)
        return r.text

    def main(self):
        if len(self.argv) != 2:
            self.arg_error()

        key = self.argv[1]
        index = ApacheStatus.indexes.get(key)
        if not index:
            self.arg_error()

        res = self.get_apache_status()
        lines = res.split('\n')
        value = None
        for line in lines:
            if line.find(index) == 0:
                value = line.replace(index, '')
                value = value.strip()
                if key == 'cpu_load':
                    value = float(value)
        if not value:
            sys.exit('Not Found Index: %s' % index)
        print(value)


if __name__ == '__main__':
    s = ApacheStatus(sys.argv)
    s.main()
