文件变化实时监控工具(代码审计/黑盒/白盒审计辅助工具)

基于项目修改 https://github.com/TheKingOfDuck/FileMonitor

Python库依赖：watchdog、time、sys

修改代码实现:


    1 修复无例外路径时监控失效
    2 新添可设置多个例外路径，以逗号','分割
    3 优化代码结构
    4 修改信息输出为中文
    5 修复python2中文乱码问题
