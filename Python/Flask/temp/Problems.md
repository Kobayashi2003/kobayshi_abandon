https://flask.net.cn/

# 启动 venv 报错

.\venv\Scripts\activate : 无法加载文件 D:\myproject\venv\Scripts\Ac
tivate.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:
/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Polici
es。


解决：管理员启动powershell

> set-executionpolicy remotesigned

# 解决“command not found: flask

> >>> export PATH=$PATH:~/.local/bin/

> >>> vim ~/.zshrc
export PATH=$PATH:~/.local/bin/