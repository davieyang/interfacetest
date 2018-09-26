在工程的跟目录新建一个脚本：run_main.py,用来执行全部用例
在工程下创建以下几个pakage包:
--case:这个包放test开头的测试用例，也可以放一些封装接口的方法，如：loginblog(如果封装的接口比较多，也可以单独放一个包）

--common:这个包放一些公共的方法，如：读取excel文件方法，读取mysql、oracle，logger.py这个是封装日志的输入

--config:cfg.ini这里是配置文件，如邮箱的一些参数：收件人，发件人，密码等,readConfig.py用于读取配置文件

--logs:这里存放日志信息

--report:这里存放测试报告