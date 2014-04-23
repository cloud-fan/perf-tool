import subprocess
import time
import os

ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
grep1 = subprocess.Popen(['grep', 'log-analyzer'], stdin=ps.stdout, stdout=subprocess.PIPE)
grep2 = subprocess.Popen(['grep', '-v', 'grep'], stdin=grep1.stdout, stdout=subprocess.PIPE)
awk = subprocess.Popen(['awk', '{print $2}'], stdin=grep2.stdout, stdout=subprocess.PIPE)
pid, err = awk.communicate()
pid = pid.strip()
if (pid != ""):
    assert not "\n" in pid
    subprocess.call(['kill', pid])
    time.sleep(5)
    if os.path.isfile('realtime-chart-1.0/RUNNING_PID'):
        f = open('realtime-chart-1.0/RUNNING_PID','r')
        pid = f.read()
        pid = pid.strip()
        assert not "\n" in pid
        subprocess.call(['kill', pid])
        print("finish successfully!")
