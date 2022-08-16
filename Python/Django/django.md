[toc]

# 官方文档

https://docs.djangoproject.com/zh-hans/3.2/

# 建立项目

## 建立虚拟环境

> python -m venv ll_env

<!-- ll_env 为文件名,可自取 -->


## 激活虚拟环境

> source ll_env/Scripts/activate

要想停止使用虚拟环境
> deactivate


## 安装 Django

> pip install django


## 在 Django 中创建项目

> django-admin startproject learning_log .

<!-- 这个命令末尾的句点让新项目使用合适的目录结构,不能够忽略它 -->

该命令创建了一个名为 learning_log 的目录，同时还创建了 manage.py。
后者是一个简单的程序，接受命令并将其交给 Django 的相关部分运行。我们将用这些命令来管理使用数据库和运行服务器等任务。

目录 learning_log 包含4个文件，最重要的是 settings.py、urls.py 和 wsgi.py

### settings.py

> 指定 Django 如何与系统交互以及如何管理项目。在开发项目的过程中，我们将修改其中一些设置，并添加一些设置。

### urls.py

> 告诉 Django 应创建哪些页面来响应浏览器请求。

### wsgi.py

> 帮助 Django 提供它创建的文件，这个文件名是 Web服务器网关接口（Web server gateway interface）的缩写


## 创建数据库

> python manage.py migrate

我们将修改数据库称为**迁移（migrate）**数据库。首次执行命令 migrate 时，将让 Django 确保数据库与项目的当前状态匹配。在使用 SQLite 的新项目中首次执行这个命令时，Django 将新建一个数据库。

<!-- SQLite 是一种使用单个文件的数据库，是编写简单应用程序的理想选择，因为它让你不用太关注数据库管理的问题 -->

## 启动服务器并查看项目

> python manage.py runserver

关闭服务器
> Ctrl + C


# 创建应用程序

> python manage.py startapp learning_logs

<!-- learning_logs 是应用程序名 -->

命令 startapp appname 让 Django 搭建创建应用程序所需的基础设施。在这里 Django 将创建一文件夹，其中包含的最重要的几个文件是 models.py、admin.py 和 views.py。


## 定义模型

在 models.py 中定义模型

## 激活模型

在 settings.py 中找到 INSTALLED_APPS，并将前面的应用程序添加到该列表中
务必将自己创建的应用程序放在默认应用程序前面，这样能够覆盖应用程序的行为



接下来，需要让 Django 修改数据库，使其能够存储与模型 Topic 相关的信息

> python manage.py makemigrations learning_logs

命令 makemigrations 让 Django 确定该如何修改数据库，使其能够存储与前面定义的新模型相关联的数据。Django 将会创建一个迁移文件，这个文件将在数据库中为模型 Topic 创建一个表

然后应用这种迁移，让 Django 替我们修改数据库：

> python manage.py migrate

<!-- 每当需要修改 “学习笔记” 管理的数据时，都采用如下三个步骤：修改 models.py，对 learning_logs 调用 makemigrations，以及让 Django 迁移项目 -->



## Django 管理网站

Django 提供的**管理网站（admin site）**让你能够轻松地处理模型。网站管理员能够使用管理网站，而普通用户不能使用。



### 创建超级用户

Django 允许创建具备所有权限的用户，即**超级用户**，**权限**决定了用户可执行的操作。

> python manage.py createsuperuser

使用超级账户访问管理网站：访问 `http://localhost:8000/admin/`



### 向管理网站注册模型

Django 自动在管理网站中添加了一些模型，如 User 和 Group，但对于我们创建的模型，必须手工进行注册

在 admin.py 中注册模型



### 添加主题

在管理网站中点击 Add 进行添加



## 定义模型 Entry

为使用户能够在学习笔记中添加条目，需要定义相关的模型。每个条目都与特定主题相关联，这种关系称为**多对一关系**，即多个条目可关联到同一个主题

请将 Entry 模型的代码放在文件 models.py 中



## 迁移模型 Entry

添加新模型后，需要再次迁移数据库



## 向管理网站注册 Entry

我们还需要在 admin.py 中注册模型 Entry

返回到 `http://localhost/admin`，便可以开始添加条目



## Django shell

输入一些数据后，就可通过交互式终端会话以编程方式查看这些数据了。这种交互式环境称为 Django shell，是测试项目和排除故障的理想之地。

示例：

> python manage.py shell
```shell
>>> from learning_logs.models import Topic
>>> Topic.objects.all()

>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)

>>> t = Toic.objects.get(id=3)
>>> t.text
>>> t.date_added

# 我们还可以查看与主题相关联的条目
# 要通过外键关系获取数据，可使用相关模型的小写名称、下划线和单词 set
>>> t.entry_set.all()
```


# 创建页面：学习笔记主页

使用 Django 创建页面的过程分三个阶段：定义 URL，编写视图和编写模板。
<!-- 实际上按照什么顺序完成这三个阶段无关紧要 -->

URL模式描述了 URL 是如何设计的，让 Django 知道如何将浏览器请求与网站 URL 匹配，以确定返回哪个页面。
每个 URL 都被映射到特定的视图——视图函数获取并处理页面所需的数据。
视图函数通常使用模板来渲染页面，而模板定义页面的总体结构。

## 映射 URL

编写 urls.py



## 编写视图

视图函数接受请求中的信息，准备好生成页面所需要的数据，再将这些数据发送给浏览器——这通常是使用定义页面外观的模板实现的

在 views.py 中编写视图



## 编写模板

模板定义页面的外观，而每当页面被请求时，Django 将填入相关的数据。模板让你能够访问视图提供的任何数据

在文件夹 learning_logs 中新建一个名为 templates 的文件夹，并在 templates 中新建一个 learning_logs 文件夹（为了方便 Django 明确进行解读），然后在其中新建 html 模板



# 创建其它页面

我们将创建两个显示数据的页面，其中一个列出所有的主题，另一个显示特定主题的所有条目。对于每个页面，我们都将指定 URL 模式、编写一个视图并编写一个模板。

但在这样做之前，我们先创建一个父模板，项目中的其它模板都将继承它



## 模板继承

创建网站时，一些通用元素几乎会在所有页面中出现。在这种情况下，可编写一个包含通用元素的父模板，并让每个页面都继承这个模板，而不必在每个页面中重复定义这些通用元素


### 父模板

编写 base.html

<!-- 注意不能让注释中出现 {% %} 字样，否则其将会被误认为模板标签的标志导致错误 -->

### 子模版

首先重写 index.html，使其继承 base.html



### 显示所有主题的页面

依旧是定义 URL、视图、模板



### 显示特定主题的页面

需要创建一个专注于特定主题的页面，它显示该主题的名称以及所有条目。我们同样将定义一个新的 URL 模式，编写一个视图并创建一个模板。此外，还将修改显示所有主题的页面，让每个项目列表都变为到相应主题页面的链接



# 用户账户

## 让用户输入数据

我们先来添加几个页面，让用户能够输入数据。我们让用户添加新主题，添加新条目以及编辑既有条目。

### 添加新主题

1. 用于添加主题的表单

让用户输入并提交信息的页面都是表单。用户输入信息时，我们需要进行验证，确认提供的信息时正确的数据类型，而不是恶意的信息。然后，对这些有效信息进行处理，并将其保存到数据库的合适地方。这些工作很多都是由 Django 自动完成的。

在 Django 中，创建表单的最简单方式是使用 ModelForm，它根据我们定义的模型中的信息自动创建表单。请创建一个名为 forms.py 的文件，将其存储到 models.py 所在的目录，并在其中编写表单

2. URL 模式 new_topic

3. 视图函数 new_topic()

函数 new_topic() 需要处理两种情形。一是刚进入 new_topic 页面（在这种情况下应显示空表单）；而是对提交的表单数据进行处理，并将用户重定向到页面 topics

4. GET 请求和 POST 请求

创建 Web 应用程序时，将用到的两种主要请求类型是 GET 请求和 POST 请求。对于知识从服务器读取数据的页面，使用 GET 请求；在用户需要通过表单提交信息时，通常使用 POST 请求。处理所有表单时，都将指定使用 POST 方法。

5. 模板 new_topic

创建模板 new_topic

6. 链接到页面 new_topic

在页面 topics 中添加到页面 new_topic 的链接


### 添加新条目

1. 用于添加新条目的表单
2. URL 模式 new_entry
3. 视图函数 new_entry
4. 模板 new_entry
5. 连接到页面 new__entry


### 编辑条目

接下来创建一个让用户能够编辑既有条目的页面

1. URL 模式 edit_entry
2. 视图函数 edit_entry()
3. 模板 edit_entry
4. 链接到页面 edit_entry



## 创建用户账户

建立用户注册和身份验证系统，让用户能够注册账户，进而登录和注销。为此，我们将新建一个应用程序，其中包含与处理用户账户相关的所有功能。这个应用程序将尽可能使用 Django 自带的用户身份验证系统来完成工作。同时还需要对模型 Topic 稍做修改，让每个主题都归属于特定用户

### 应用程序 users

首先用命令 startapp 创建一个名为 users 的应用程序

### 将 users 添加到 settings.py 中

### 包含 users 的 URL

### 登录页面

我们将使用 Django 提供的默认视图 login

1. 模板 login.html

用户请求登录页面时，Django 将使用一个默认的视图函数，但我们依旧需要为这个页面提供模板。默认的身份验证视图在文件夹 registration 中查找模板，因此我们需要创建这个文件夹。为此，在目录 learning_log/users/ 中创建一个名为 templates 的目录，再在这个目录中新建一个名为 registration 的目录，在下面新建模板 login.html

2. 链接到登录页面

在 base.html 中添加到登录页面的链接，让所有页面都包含它。用户已登录时，我们不想显示这个链接，因此将它嵌套在一个{% if %}标签中

### 注销

1. 在 base.html 中添加注销链接

现在需要提供一个让用户注销的途径。为此，我们将在 base.html 中添加一个注销链接。用户单击这个链接时，将进入一个确认其已注销的页面


2. 注销确认页面

成功注销后，用户希望获悉这一点。因此默认的注销视图使用模板 logged_out.html 渲染注销确认页面。


### 注册页面

接下来创建一个页面供新用户注册。我们将使用 Django 提供的表单 UserCreationForm，但编写自己的视图函数和模板

1. 注册页面的 URL 模式

2. 视图函数 register()

在注册页面首次被请求时，视图函数 register() 需要显示一个空的注册表单，并在用户提交填写好的注册表单时对其进行处理。如果注册成功，这个函数还需让用户自动登录。

3. 注册模板
4. 链接到注册页面


## 让用户拥有自己的数据

### 使用 @login_required 限制访问

Django 提供了装饰器 @login_required，让你能够轻松地只允许已登录用户访问某些页面。
装饰器（decorator）是放在函数定义前面的指令，Python 在函数运行前根据它来修改函数代码的行为。

1. 限制访问显示所有主题的页面

每个主题都归特定用户所有，因此应只允许已登录的用户请求显示所有主题的页面

2. 全面限制对项目 “学习笔记” 的访问

在项目 “学习笔记” 中，将不限制对主页和注册页面的访问，并限制对其它所有页面的访问

### 将数据关联到用户

现在，需要将数据关联到提交它们的用户。只需将最高层的数据关联到用户，更低层的数据就会自动关联到用户。
例如，咋爱项目 “学习笔记中” 最高层的数据时主题，而所有条目都与特定的主题相关联。只要每个主题都归属于特定用户，就能确定数据库中的每个条目的所有者

修改模型 Topic，在其中添加一个关联到用户的外键。这样做之后，必须对数据库进行迁移。最后，必须修改某些视图，使其只显示与当前登录的用户相关联的数据。

1. 修改模型 Topic

2. 确定当前有哪些用户

迁移数据库时，Django 将对数据库进行修改，使其能够存储主题和用户之间的关联。为执行迁移，Django 需要知道该将各个既有主题关联到哪个用户。最简单的方法是，将既有主题都关联到超级用户。为此需要知道该用户的 ID。

启动 Django shell 会话

```shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()

>>> for user in User.objects.all():
...     print(user.username, user.id)
```

3. 迁移数据库

知道用户 ID 后，就可以迁移数据库了。这样做时，Python 将询问你是要暂时将模型 Topic 关联到特定用户，还是在文件 models.py 中指定默认用户。请选择第一个选项。

<!-- 当然，你可以重置数据库而不是迁移它，但如果这样做，既有的数据都将丢失。如果你确实想要一个全新的数据库，可执行命令 python manage.py flush，这将重建数据库结构。如果这样做，你还需要重新创建超级用户 -->


### 只允许用户访问自己的主题

修改 views.py 中的函数 topics()

### 保护用户的主题

在视图函数 topic() 获取请求的条目前执行检查

### 保护页面 edit_entry

### 将新主题关联到当前用户



# 设置应用程序的样式并部署


## 设置项目 “学习笔记” 的样式

### 应用程序 django-bootstrap4

我们将使用 django-bootstrap4 将 Bootstrap 集成到项目中。这个应用程序下载必要的 Bootstrap 文件，将其放到项目的合适位置，让你能够在项目中使用样式设置指令

> pip install django-bootstrap4

接下来需要在 settings.py 的 INSTALLED_APPS 中添加应用程序 django-bootstrap4

### 使用 Bootstrap 设置项目 “学习笔记” 的样式

Bootstrap 是一个大型样式设置工具集，还提供了大量模板，可应用于项目以创建独特的总体风格。要查看 Bootstrap 提供的模板，可访问其官方网站，单击 Examples 并找到 Navbars。我们将使用模板 Navbars static，它提供了简单的顶部导航栏以及用于放置页面内容的容器。

## 部署学习笔记

### 注册 Heroku 账户

### 安装 Heroku CLI

### 安装必要的包

虚拟状态下安装：

为管理 Heroku 使用的数据库，psycopg2 包必不可少
> pip install psycopg2==2.7.*

django-heroku 包用于管理应用程序的各种配制，使其能够在 Heroku 服务器上正确地运行。这包括管理数据库，以及将静态文件存储到合适的地方，以便能够妥善地提供它们 。静态文件包括样式规则和 JavaScript 文件。
> pip install django-heroku

gunicorn 包让服务器能够实时地支持应用程序
> pip install gunicorn

### 创建文件 requirements.txt

Heroku 需要知道项目依赖于哪些包，因此我们使用 pip 生成一个文件，在其中列出这些包

> pip freeze > requirements.txt

命令 freeze 让 pip 将项目中当前安装的所有包的名称都写入文件 requirements.txt

我们部署 “学习笔记” 时，Heroku 将安装 requirements.txt 列出的所有包，从而创建一个环境，其中包含在本地使用的所有包。有鉴于此，我们可以深信在部署到 Heroku 后，项目的行为将于本地系统上完全相同。当你在自己的系统上开发并维护各种项目时，这将是一个巨大的优点

### 指定 Python 版本

查看 Python 版本
> python --version

在 manage.py 所在的文件夹中新建一个名为 runtime.txt 的文件，并在其中输入

```txt
python-3.10.6
```

这个文件应只包含一行内容，以上面所示的格式指定你的 Python 版本。请确保输入小写的 python

### 为部署到 Heroku 而修改 settings.py

### 创建启动进程的 Procfile

Procfile 告诉 Heroku 应该启动哪些进程，以便正确地提供项目需要的服务。请将这个只包含一行代码的文件命名为 Procfile，但不指定文件扩展名，再将其保存到 manage.py 所在的目录中

```Procfile
web: gunicorn learning_log.wsgi --log-file -
```

这行代码让 Heroku 将 Cunicorn 用作服务器，并使用 learning_log/wsgi.py 中的设置来启动应用程序。标识 log-file告诉 Heroku 应将哪些类型的事件写入日志


### 使用 Gir 跟踪项目文件

Git 是一个版本控制程序，让你能够在每次成功实现新功能后都拍摄项目代码的快照。无论出现什么问题，都可轻松地恢复到最后一个可行的快照。每个快照都称为

1. 安装 Git

先检查是否已经安装了 Git
> git --version

2. 配置 Git

Git 跟踪是睡修改了项目，即便项目由一个人开发也亦如此。未进行跟踪，Git 需要知道你的用户名和电子邮箱。因此，你必须提供用户名，但对于练习项目，可以编造一个电子邮箱：

> git config --global user.name "kobayashi"
> git config --global user.email "eric@example.com"

3. 忽略文件

在 manage.py 所在的文件夹中创建一个名为 .gitignore 的文件（请注意：这个文件以句点打头，且不包含扩展名），并在其中输入以下代码：

```
ll_env/
__pycache__/
*.sqlite3
```

这里让 Git 忽略目录 ll_env，还指定不跟踪目录 __pycache__

*.sqlite3 让 Git 忽略所有扩展名为 .sqlite3 的文件

4. 提交项目

我们需要为 “学习笔记” 初始化一个 Git 仓库，将所有必要的文件都加入该仓库，并提交项目的初始状态

> git init
在学习笔记所在的目录中初始化一个空仓库

> git add .
将未被忽略的文件都加入这个仓库

> git commit -am "Ready for deplyment to heroku"
标志 -a 让 Git 在这个提交中包含所有修改过的文件，-m 让 Git 记录一条日志消息

> git status


### 推送到 Heroku

在活动的虚拟环境中，执行下面的命令

> heroku login
> (heroku login -i)

jacklink853@gmail.com
Kobayashi@2003

> heroku create
让 Heroku 创建一个空项目。Heroku 生成的项目名由两个单词和一串数字组成，但以后可修改这个名称。

> git push heroku master
让 Git 将项目的分支 master 推送到 Heroku 刚才创建的仓库中。Heroku 将使用这些文件在其服务器上创建项目

执行了这些命令后，项目就部署好了，但还未做全面配置。为核实正确地启动了服务器进程，需要执行：
> heroku ps

可以在浏览器中打开这个应用程序了：
> heroku open

### 在 Heroku 上建立数据库

为建立在线数据库，需要再次执行命令 `migrate`，并应用在开发期间生成的所有迁移。要对 Heroku 项目执行 Django 和 Python 命令，可使用命令：heroku run

> heroku run python manage.py migrate

命令执行后，Heroku 创建一个终端会话来执行命令 migrate。Django 应用默认迁移以及我们在开发 “学习笔记” 期间生成的迁移

### 改进 Heroku 部署

1. 在 Heroku 上创建超级用户

我们知道可以使用命令 heroku run 来执行一次性命令，但也可以这样执行命令：在连接到 Heroku 服务器的情况下，使用命令 heroku run bash 打开 Bash 终端会话。Bash 是众多 Linux 终端运行的语言。我们将使用 Bash 终端会话来创建超级用户，以便访问在线应用程序的管理网站：

> heroku run bash

> python manage.py createsuperuser

创建之后，你就可以在在线应用程序的 URL 末尾添加 /admin/ 来登录管理网站了

2. 在 Heroku 上创建对用户友好的 URL

重命名：
> heroku apps:rename learning-log

### 确保项目的安全

当前，部署的项目存在严重的安全问题：settings.py 包含设置 DEBUG = True，指定在发生错误时显示调试信息。开发项目时，Django 的错误页面显示了重要的调试信息，如果将项目部署到服务器后还保留这个设置，将给攻击者提供大量可利用信息

在在线项目中，我们将设置一个环境变量，以控制是否显示调试信息。环境变量时特定环境中设置的值。这是在服务器上存储敏感信息并将其与项目代码分开的方式之一

现在修改 settings.py


### 提交并推送修改

> git commit -am "Set DEBUG based on environment variables."

<!-- 错误信息：Error while running '$ python manage.py collectstatic --noinput'
解决：heroku config:set DISABLE_COLLECTSTATIC=0
 -->

> git status

> git push heroku master


### 在 Heroku 上设置环境变量

> heroku config:set DEBUG=False


### 创建自定义错误页面

1. 创建自定义模板

在最外层的文件夹 learning_log 中新建一个名为 templates 的文件夹。在该文件夹内创建一个名为 404.html 的文件

然后对 settings.py 做细微修改

2. 在本地查看错误页面

首先在本地设置中设置 DEBUG=False

查看后，将本地 DEBUG 的值重新设为 True

3. 将修改推送到 Heroku

> git add .
> git commit -am "Added custom 404 and 500 error pages"
> git push heroku master

### 设置 SECRET_KEY

### 将项目从 Heroku 删除

> heroku apps:destroy --app appname