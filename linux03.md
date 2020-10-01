- whereis和 which  用于查找可执行程序
## 系统设置命令
- alias 给命令起别名
    + 语法：alias 新名字=原命令 + [参数]
    + 例子：alias ll="ls -l"
    + 删除别名：unalias 别名
- echo 打印内容 一般会和export 等变量，在shell脚本中使用  
    + 打印字符  echo 字符    ----  echo  123
    + 打印变量  echo $变量名  ---- echo  $a     前提设置a=1
    + shell中的使用  ，执行shell 使用  ./   或者 绝对链接（注意需要执行权限）；或者 sh  shell脚本
- export 提交环境变量
    + export a=1 后续在搭建环境中会多次涉及
- unset删除变量
- source  1、重新加载配置文件    2、执行sql脚本
## 网络通信命令
- ifconfig 看ip的 查看网络信息的
    + 一般默认是动态获取的ip
    + redhat5的网卡配置配置文件 /etc/sysconfig/network-scripts/ifcfg-eth0
    + dhcp ---动态获取   static -- 静态获取
- hostname 查看主机名称     /etc/sysconfig/network
- uname -a查看系统信息  在性能测试时候需要知道服务器的内核信息
- cat /proc/version  查看具体版本信息
- netstat  查看端口的占用情况
    + netstat -anp | grep XX 搜索XX端口/XX进程的端口占用情况
    + 例子 查看SCRT使用22端口连接服务器的情况 listen状态和established状态
- ping命令 查看网络是否能连接上,在传输/连接之前，使用此命令进行验证网络是否畅通
    + ping ip
    + ping www.baidu.com
- telnet 远程访问 跨服务器访问
    + telnet ip 端口  默认为23端口 
    + 就可以验证对方XX端口是否畅通
- ssh 远程访问 默认22端口，跨到其他的主机上
    + 语法：ssh 用户名@ip    ssh root@192.168.3.106
    + 实际可以跨越到开发的主机上进行对代码的编译打包操作
- scp 远程复制文件， 传输文件
    + 取语法：scp [-r]（如果是目录则需要加-r） 用户名@ip:绝对路径文件   存放本地的位置路径
        + 例子：scp  -r  root@192.168.3.106:/root/app    ./   -- 取目录app
        + 例子：scp root@192.168.3.106:/root/app/test1.log   ./
    + 传文件： scp [-r]   存放本地的位置路径   用户名@ip:绝对路径文件 例子：scp   ./tt.log   root@192.168.3.106:/root/app
    + 不用跨越到对方去
    + 可以模糊匹配多个传输
- ftp和sftp
    + 语法 sftp  root@192.168.3.106  通过 get 文件  获取   ；  put 文件  上传
    + 支持模糊批量操作
    + sftp root@192.168.3.106
    + get test1.log  -- 获取远程主机上的文件 test1.log到本地目录
    + put yy.txt   ---  上传本地目录文件yy.txt 到远程主机
## 磁盘管理命令
- df 查看磁盘
- du 查看指定的文件/目录的磁盘空间
    + du -b test1.log -- -b 按照字节统计
- mount 挂载 一般都是挂载到 /mnt上
    + 语法：mount 分区 路径  -- mount /dev/sda1 /mnt
    + 解除挂载 umount  挂载点/分区 -- umount /boot
## 资源查看
- top  实时监控系统的资源情况和进程情况；主要关注cpu和内存
- vmstat 不是实时的  ， vmstat  间隔时间  输出次数 
- lsof 一般用来查看端口的占用情况
    + lsof -i:端口号
    + lsof  -i:22  查看22端口的占用情况，可以看到具体占用端口的进程信息，是否监听等信息
- ps 查看进程的
    + ps -ef  查看系统运行哪些进程  主要关注 pid--进程号  cmd -- 名 ；一般和 | grep进行组合使用
    + 停止进程  kill [-9] pid
    + 例子：查询出链接SCRT的ssh服务的进程号，并杀死  ps -ef | grep ssh ----- pid   ;  kill  [-9]   pid  进行停止 ； 如何再次启动：进入主机端命令界面：service  sshd  start
    + 找出占用内存资源最多的前 10 个进程
    + # ps -auxf | sort -nr -k 4 | head -10
    + 找出占用 CPU 资源最多的前 10 个进程
    + # ps -auxf | sort -nr -k 3 | head -10
## 压缩包管理
- .rar 现在linux不能进行解压，如果需要用此包需要安装专门的rar命令
- .7z
- .gz
    + 使用gzip进行压出来的 
    + gzip压缩只能单个压成单个
    + 压语法：gzip [-r] 要压缩的文件  -- 如果是目录则-r，递归和继承
    + 默认不保留源文件
    + 解压：gzip [-d][-r] 要解压的压缩文件  gzip -d == gunzip  如果是目录则-r递归和继承
    + 支持模糊匹配 使用gzip * 压当前目录下的所有文件
- .zip
    + 可以压缩目录和文件
    + 压缩语法：zip [-r] 新的压缩包名.zip  源文件
        + zip -r app1.zip app1
    + 解压语法：unzip 新的压缩包名.zip
        + unzip app1.zip
    + 会保留源文件
- .bz2   bzip2和bunzip2语法同gzip和gunzip
    + 压缩效率更高一点，所以用的稍微多一点
- .tar
    + 压缩：tar -cvf 新包.tar 源文件
        + tar -cvf app1.tar app1/
    + 解压：tar -xvf 新包.tar
        + tar -xvf app1.tar
    + 如果要解压到指定的位置 -C 位置
- .tar.gz /.tgz
    + 压缩：tar -zcvf 新包.tar.gz 源文件
        + tar -zcvf app1.tar.gz app1/
    + 解压：tar -zxvf 新包.tar.gz 
        + tar -zxvf app1.tar.gz
    + 如果要解压到指定的位置 -C 位置
        + tar -zxvf app1.tar.gz -C /
- .war java项目包  jar -xvf XXX.war
- .jar 开发人员专用的jar包，里边是class文件
- .rpm -- 安装包；是redhat系统默认包----具体在搭建环境的时候会用
    + 查询已经安装了XXX rpm包
        + rpm -qa | grep XXX
    + 安装rpm包
        + rpm -ivh XXXX.rpm [--force] [--nodeps]
            + --force 强制   --nodeps 不依赖
    + 卸载rpm
        + rpm -e XXX程序 [--force] [--nodeps]
    + 升级rpm
        + rpm -Uvh XXXX.rpm/链接地址
