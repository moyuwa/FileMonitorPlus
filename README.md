文件变化实时监控工具(代码审计/黑盒/白盒审计辅助工具)

基于项目修改 https://github.com/TheKingOfDuck/FileMonitor (20200628更新:相关问题原项目已修复，请移步原项目下载，当前项目仅作历史记录)

Python库依赖：watchdog、time、sys，支持Python2、3

修改代码实现:


    1 修复无例外路径时监控失效
    2 新添可设置多个例外路径，以逗号','分割
    3 优化代码结构
    4 修改信息输出为中文
    5 修复python2中文乱码问题


为方便大家使用，已用pyinstaller打包生成了windows10免环境程序，访问

https://github.com/moyuliu/FileMonitorPlus/releases/tag/1.0 

点击链接下载

fileMonitor.zip


