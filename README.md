# 性能测试工具
此工具主要功能是进行自动化的性能测试，并能实时画出性能图。

目前只能利用ssh到远端服务器运行ifstat, iostat,top等命令来监控服务器状态，通过分析这些命令的输出实时画出性能图并保存到日志中。

不过，以后可以很方便的添加新的命令，并解析输入内容来画出性能图。计划中要添加的命令：运行YCSB，监控服务端的状态和客户端YCSB的TPS和latency。
## 用法
python run.py [options]

通过-p指定性能测试的类型，目前仅支持basic，即ssh到远端服务器运行ifstat, iostat等命令。-p默认值是basic。

通过-s指定要监控的服务器集群，用逗号分隔。例子：-s root@lab74,cloud@lab193

通过-w指定最后保存性能图的网页的路径。当跑完性能测试之后，你需要运行finish.sh来结束性能测试，并保存性能图。例子：-w /var/www

运行完run.py之后，你可以通过浏览器访问http://localhost:9000来查看实时性能图。运行完finish.sh之后，通过浏览器访问你-w指定的路径来查看性能图。
## 实现
此工具仅仅只是一个wraper，它利用了另外两个项目：[realtime-chart](https://github.com/cloud-fan/realtime-chart)和[log-analyzer](https://github.com/cloud-fan/log-analyzer).

如果对源码有兴趣，可以看下这两个项目。