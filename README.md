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
```
└──server：服务端开发的源码
     ├─app：服务端主要代码
     │    ├─__init__.py：初始化app对象
     │    ├─model：定义数据模型及数据表相关操作
     │    │    ├─__init__.py：初始化数据库连接
     │    │    ├─...
     │    │
     │    └─api：各模块API
     │         ├─__init__.py：初始化api命名空间
     │         ├─...
     │
     ├─instance
     │    └─config.py：私密配置文件
     ├─config.py：普通配置文件
     ├─run.py：入口文件
     └─requirements.txt：第三方包需求文件
```

## 安装&运行
### 安装
```bash
# 安装虚拟环境virtualenv
pip install virtualenv
# 克隆仓库
git clone https://github.com/TheYelda/AppServer
# 切换到项目源码目录
cd AppServer/server
# 新建虚拟环境并指定Python版本
virtualenv venv -p python3
# 激活虚拟环境
source venv/bin/activate
# 安装第三方模块
pip install -r requirements.txt
```
**注**：如果开发中引入了新的第三方模块，请用下列命令更新`requirements.txt`：
```bash
pip freeze > requirements.txt
```

### 运行
```bash
# 生产模式
python run.py
# 测试模式，同时指定端口
python run.py -m test -p 10086
```
**注**：运行项目前，需要在server目录下新建`instance`目录，并在`instance`目录下新建`config.py`文件，在`config.py`中添加项目的私密配置，例如：

```python
DB_USERNAME = 'username'      # MySQL用户名
DB_PASSWORD = 'password'      # MySQL密码
DB_NAME = 'yelda'             # 数据库名称
SECRET_KEY = 'I wont tell u'  # 用户会话管理秘钥
PHOTOS_FOLDER = 'yelda/photos'                  # 头像图片文件夹
MEDICAL_IMAGES_FOLDER = 'yelda/medical-images'  # 医疗图像文件夹
MAX_CONTENT_LENGTH = 16 * 1024 * 1024           # 上传文件大小限制
```

## 开发规范
- 代码风格参考[Python开发规范](https://github.com/TheYelda/Dashboard/blob/master/python_code_style_guide.md)。
- Git的使用参考[Git开发规范](https://github.com/TheYelda/Dashboard/blob/master/git_collaboration_guide.md)。

## 数据模型
![](https://raw.githubusercontent.com/TheYelda/Dashboard/master/docs/images/db.png)

## RESTful API
<https://github.com/TheYelda/Dashboard/blob/master/docs/design/api.md>
