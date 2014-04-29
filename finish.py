import subprocess
import time
import os
import signal

def check_pid(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def kill_process(pid):
    os.kill(pid, signal.SIGTERM)
    while (check_pid(pid)):
        time.sleep(2)

ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
grep1 = subprocess.Popen(['grep', 'log-analyzer'], stdin=ps.stdout, stdout=subprocess.PIPE)
grep2 = subprocess.Popen(['grep', '-v', 'grep'], stdin=grep1.stdout, stdout=subprocess.PIPE)
awk = subprocess.Popen(['awk', '{print $2}'], stdin=grep2.stdout, stdout=subprocess.PIPE)
pid, err = awk.communicate()
pid = pid.strip()
if (pid != ""):
    assert not "\n" in pid
    kill_process(int(pid))
    print("shutdown log analyzer successfully!")
    if os.path.isfile('realtime-chart-1.0/RUNNING_PID'):
        f = open('realtime-chart-1.0/RUNNING_PID','r')
        pid = f.read()
        pid = pid.strip()
        assert not "\n" in pid
        kill_process(int(pid))
        print("finish successfully!")