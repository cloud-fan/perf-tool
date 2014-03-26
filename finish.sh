ps aux|grep log-analyzer|grep -v grep|awk '{print $2}'|xargs kill > /dev/null 2>&1
sleep 5
if [ -f realtime-chart-1.0/RUNNING_PID ]; then
cat realtime-chart-1.0/RUNNING_PID|xargs kill > /dev/null 2>&1
fi