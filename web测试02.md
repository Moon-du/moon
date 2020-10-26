## web测试工具
- xenu  死链接测试工具
- 抓包
    + f12 （浏览器自带的，开发者工具，控制台）
        + elements 显示html的  定位元素用 web自动化
        + console  控制台，js调试的，页面运行js报错的信息
        + newwork 勾选preserver log  查看请求响应报文 get  post请求
    + httpwatch ---ie上抓 ie8
        + 关注 postdata post的传参
        + header 请求的头部和响应的头部
        + content 响应的内容
        + stream  请求和响应的所有数据
    + fiddler 
        + 怎么抓怎么看 请求响应，正文
        + filter过滤
        + composer 接口测试
        + autoresponseder --自动响应  mock
        + https证书的安装
            + tools-fiddler options-https--勾选**traffic-actions-到处导出证书到桌面（第二个）
            + 打开chrome -- 设置 --证书管理 - 导入 --下一步到底 重启chrome和fiddler
        + 断点  请求前和响应后  --- 调试，查看具体的请求和响应的
        + 手机设置代理 抓手机的流量 -- app上说
    + wireshark  -- 抓的很全
        + 选择网卡 进行抓包
        + 设置过滤 ip.addr == 地址  and 协议（http） ip.src (源)  ip.dst (目的ip)  tcp.dstport(目的端口)
        + https://www.cnblogs.com/nmap/p/6291683.html