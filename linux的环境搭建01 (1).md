## 系统的环境
- 环境 
    + 前端环境(客户端环境)
        + 客户端的安装配置
    + 后端环境（服务器环境）
        + 操作系统 redhat5
        + 数据库 mysql
        + 语言环境（运行环境） - java jdk
        + 服务器软件，web容器，服务器，中间件  - tomcat（apache，iis，weblogic，nginx，jboss。。。。。）
        + 项目
- 本地搭建oa环境
    + 使用工具：winscp ，SCRT ，navicat ，redhat5 ，vmware
    + 安装jdk
        + 新建/usr 建立目录java 将jdk包上传并解压，验证jdk/bin/java 或者javac是否可执行 结果执行报错---系统安全模式打开着的
            + 关闭系统的安全模式 临时关闭 setenforce 0 （重启后失效）
            + 完全关闭 修改 /etc/selinux/config 文件 将selinux=XXX项修改为disabled  再进行reboot
            + 此时再次验证执行java 或者 javac 或者 ./java -version 会执行成功包语法错误
        + 现在java命令已经能运行，但是我需要的是一个系统认识的java命令，于是需要配置环境变量
        + 修改/etc/profile环境变量 在最后添加以下信息 
JAVA_HOME=/usr/java/jdk1.7.0_80
CLASSPATH=.:$JAVA_HOME/lib/
PATH=$PATH:$JAVA_HOME/bin
export PATH JAVA_HOME CLASSPATH
或者
export PATH=$PATH:/usr/java/jdk1.7.0_80/bin
使用source命令使环境变量生效 source /etc/profile
使用 java验证是否配置成功

    + 安装tomcat
        +  在/usr目录下新建tomcat目录 将Tomcat包上传进去 进行解压操作
        + 进入Tomcat之下的bin目录 执行 ./startup.sh 启动Tomcat  
        + 关闭防火墙 service iptables stop   再在外部浏览器上输入 http://IP:8080 查看页面显示
    + 安装mysql 本次使用rpm包进行安装
        + 在/usr/local 下新建mysql目录
        + 将三个rpm包放入该目录 使用rpm -ivh 安装mysql的rpm包，分别先安装 server，devel，client ，如果有依赖需要 --nodeps
        + 在启动mysql（默认安装server包时已经启动）
        + 使用mysql进行验证，直接在命令界面输入mysql查看是否有 mysql>  验证成功再推出 exit
        + 给mysql赋予管理员账号密码 使用命令，在linux命令窗口输入：mysqladmin -u root password "123456" 
        + 使用此账号和密码进行登录：mysql -uroot -p 
        + 进入mysql系统，给其他主机远程连接赋予权限输入：GRANT ALL PRIVILEGES ON *.* TO root@"%" IDENTIFIED BY "123456";
        + 再进行刷新权限： flush privileges;
        + 再查下是否赋予成功：use mysql；   select host,user,password  from user; 查看host项是否有一新的 % 和其他项的信息；
        + 使用宿主机的navicat进行连接 ---- ok
    + 部署项目oa系统
        + 将OA包到tomcat的webapps子目录中，进行解压操作
        + 修改配置文件
            + 数据库的链接文件---修改oa/WEB-INF/proxool.xml   将数据库的用户名和密码修改为安装时设置的配置 -- 主要修改数据库的密码
            + 修改日志文件---修改oa/WEB-INF/log4j.properties 中的log4j.appender.R.File变量值修改为当前OA的log子目录的路径
            + 修改缓存---修改oa/WEB-INF/classes/cache.ccf中的jcs.auxiliary.DC.attributes.DiskPath 修改为当前OA的CacheTemp子目录所在的路径
        + 将项目的sql脚本导入数据库 脚本文件在 oa/setup/redmoonoa.sql
        + 重新启动tomcat，http://linux主机地址:8080/oa/setup设置好OA系统 ---- 进行web界面进行配置链接
        + 登陆系统 admin 密码：111111    链接地址：http://localhost:8080/oa/index.jsp

## 命令汇总
- mkdir   touch  tar -zxvf  ，rpm -ivh/-e  ，mv  cp，chmod， netstat ，ifconfig，tail -f ，more ，vi ，service ，source ，yum ，wget，top，scp ，ps -ef | grep XX   kill ，