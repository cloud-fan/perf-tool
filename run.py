#!/usr/bin/env python

import os
import sys
import time
import optparse
import subprocess

def parserOption(parser):
    parser.add_option('-p', '--perf-type', dest='perfType',
    help='specify the type of performance test to run. now only suppprt basic and top',
    default='basic')

    parser.add_option("-t", "--tag", dest="tag",
    help="specify the tag to prepend to result web pages dir name, default is the perf type")

    parser.add_option('-s', '--servers', dest="servers",
    help='specify the servers to monitor in the format of "usename1@hostname1,usename2@hostname2,..."')

    parser.add_option("-w", "--web-path", dest="webPath",
    help='specify the path of web dir to store the result web pages',
    default='/var/www')

    top = optparse.OptionGroup(parser,'top Options',
    'These Options is used for top mode.')

    top.add_option("-P", "--process", dest="process",
    help="specify the process name to run top")

    parser.add_option_group(top)

    (options,args) = parser.parse_args()

    if(not options.servers):
        parser.error('servers not given!')

    if(options.perfType == 'top'):
        if(not options.process):
            parser.error('process name not given!')

    return (options,args)

def check_server_start():
    logFile = 'realtime-chart-1.0/logs/application.log'
    while not os.path.isfile(logFile):
        time.sleep(2)
    f = open(logFile,'r')
    content = f.read()
    while ("Listening for HTTP" not in content):
        f.close()
        time.sleep(2)
        f = open(logFile,'r')
        content = f.read()

parser = optparse.OptionParser()
(options,args) = parserOption(parser)

if not os.path.isdir(options.webPath):
    print("the path of web dir '" + options.webPath + "' is not a dir or does not exsit!")
    sys.exit()

tag = options.tag if options.tag else options.perfType

subprocess.call(["python", "finish.py"])
subprocess.Popen(["bash", "realtime-chart-1.0/bin/realtime-chart"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
check_server_start()

if (options.perfType == "basic"):
    subprocess.Popen(["java", "-jar", "log-analyzer.jar", tag, options.webPath, options.servers, "CPU,network,disk,memory"])

if (options.perfType == "top"):
    subprocess.Popen(["java", "-jar", "log-analyzer.jar", tag, options.webPath, options.servers, "CPU,network,disk,memory,top:" + options.process])

print("start successfully! Now Please visit http://localhost:9000 to view the charts")
