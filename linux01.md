## linux基础
- linux的常用命令
- 如何搭建测试环境，维护测试环境
- shell了解多少

### 工具介绍
- vmware 虚拟机
- redhat5 操作系统，linux的某一个发行版本
- linux ；市场上主流的操作系统，windows，unix，linux；开源免费
    + 发行版本：redhat ， centos ，ubuntu，debian ,红旗
- 客户端和服务器，windows server 系列2008/2019/2020 ,unix , linux
- redhat系统会自动新增一个超级管理员的用户 root ，密码为创建的用户 密码
- 终端模拟器，-- SCRT，xshell，cmd

# 目录介绍
- linux的最高节点---  /  根目录
- /bin -- 存放常用的命令
- /sbin  -- 存放系统的命令
- /etc  各种配置文件
- /home 家目录，用户目录
- /root root用户的家目录
- /usr  用户一般安装的程序都会放到这里边

- 家目录和根目录？？
    + ~ -- 家目录  / 根目录

## 基础命令
- 切换目录 cd 目录名
- 显示当前的路径  pwd
- . 当前目录   .. 上级目录
- ll 显示当前目录下的文件信息
- ifconfig 看ip
- 路径表示方法
    + 绝对路径  从更目录定位下来的路径
    + 相对路径  和当前位置相对于的，一般为上级，下级等；路径的第一位是 / 
## 系统命令
- 注销  logout  退出当前用户的登陆
- 关机  shutdown     halt     poweroff
- 重启  reboot     shutdown -r now

## 用户管理
- 用户
    + 新建 语法：useradd 用户名 
        + 固定组，固定id，固定备注（全名） 
            + useradd  -g t2 -c "son of boss" -u 511  test6
    + 改密码：语法: passwd 用户名 
    + 修改 usermod  参数1 值1 参数2 值2....  用户名
        + 例子： usermod  -u 522 -c ""  -g t3 -G t2 -l test66      test6
    + 删除 语法 ：userdel [-r] 用户名 
        + -r 可以连用户目录一起删除
    + 查询
        + id 用户名；
        + more  /etc/passwd        
- 组
    + 新建  groupadd  组名
    + 修改 groupmod -g 522 -n t77 t7
    + 删除  如果组里有人不允许删除
        + groupdel 组名
    + 查看
        + + more  /etc/group
- 切换用户
    + su 用户名 --- 环境变量还是原来的
    + su - 用户名   --- 将环境变量也换成新用户的
    + su -  ==== 切换到root用户 相当于 
    + 退出使用   exit  
## 目录管理
- mkdir   新建目录
    + mkdir 目录名
    + mkdir -p  目录/目录   如果父节点不在可以创建
- rmdir 删除目录的
    + 一般使用  rm  -rf  XXXX； ----- 慎重！！！！！
- mv  剪切，改名
    + 语法：mv 源文件  目的文件夹
    + MV 文件  新名字
## 文档管理
- vi 编辑器
    + 新建 文档 除了vi 还有 touch 
    + 修改
    + 常规操作  
        +  vi  要修改的文档名（可以绝对路径）
        + 要进行修改或者写入新的内容 按 i o a进入编辑模式
        + 要保存退出，先 按esc键进入命令模式，再: 键（底行模式） 输入 wq  w--写入保存  q---退出；  :q! ---- 强制退出
    + 如果我们要修改一个文档内容（有内容），一进去显示文档内容为空---肯定是你的名字/路径写错了
    + 特殊操作
        + 一进去定位到固定行首  vi +[n] 文档  不加具体指为末行
        + vi进入后进入命令模式，使用nG进行定位，末行行首G
        + 进入一行的行首 ^   行末 $
        + u -- 撤销
        + 批量替换  :%s/要替换的关键字/替换成的关键字/g  ---全文替换   :%s/test1/AAA/g  将全部的test1关键字替换成AAA
        + 关键字查询  /关键字  从上往下查找 n下一个  N上一个      ?关键字 从下往上查找  n下一个  N上一个
        + 删除  dd  删除整行，  x删除一个 
        + 复制粘贴  nyy 复制n行  p--粘贴 默认到下一行
    - 练习 修改配置文件使普通用户可以使用ifconfig
        + 什么是环境变量
        + sbin是啥
        + 对应隐藏的文件如何查看 ll -a
        + 改完记得重新加载 source XX


