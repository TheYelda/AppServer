# AppServer
项目后台App Server的代码仓库。

## 后台架构
![](https://raw.githubusercontent.com/TheYelda/AppServer/master/doc/architecture.png)
项目后台采用的技术栈为Nginx+Gunicorn+Flask+MySQL。
- Nginx：Web服务器，向前端提供静态文件服务，同时针对Flask提供的RESTful API服务实现反向代理。
- Gunicorn：Python的WSGI容器，作为Web服务器和Web应用框架的中间层将两者串联起来。
- Flask：Web应用框架，通过WGSI容器Gunicorn与Nginx交互，通过ORM操作MySQL。
- MySQL：关系型数据库管理系统，直接面向数据进行管理。

## 代码目录结构
TODO

## 安装&运行
TODO

## 开发规范
参考[Python开发规范](https://github.com/TheYelda/Dashboard/blob/master/python_code_style_guide.md)。

## 数据模型
TODO

## RESTful API
通过在线工具查看：
<https://agendaservice2.docs.apiary.io/#>
