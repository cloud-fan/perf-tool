#!/usr/bin/env python

import os
import sys
import time
import optparse
import subprocess

def parserOption(parser):
    parser.add_option('-p','--perf-type',dest='perfType',
    help='specify the type of performance test to run. now only suppprt basic',
    default='basic')

    basic = optparse.OptionGroup(parser,'basic Options',
    'These Options is used for basic mode.')

    basic.add_option('-s','--servers',dest="servers",
    help='specify the servers to monitor in the format of "usename1@hostname1,usename2@hostname2,..."')

    basic.add_option("-w", "--web-path",dest="webPath",
    help='specify the path of web dir to store the result web pages',
    default='/var/www')

    parser.add_option_group(basic)

    (options,args) = parser.parse_args()

    if(options.perfType == 'basic'):
        if(not options.servers):
            parser.error('servers not given for basic mode!')

    return (options,args)

if __name__=='__main__':
    parser = optparse.OptionParser()
    (options,args) = parserOption(parser)

    subprocess.Popen(["bash", "realtime-chart-1.0/bin/realtime-chart"])
    time.sleep(5)

    if (options.perfType == "basic"):
        subprocess.Popen(["java", "-jar", "log-analyzer.jar", "basic", options.webPath, options.servers, "CPU,network,disk,memory"])
        print("start successfully! Now Please visit http://localhost:9000 to view the charts")
