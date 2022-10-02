Window: Title
根据活动编辑器控制窗口标题。变量是根据上下文替换的:

- "${activeEditorShort}": 文件名 (例如 myFile.txt)。
- "${activeEditorMedium}": 相对于工作区文件夹的文件路径 (例如, myFolder/myFileFolder/myFile.txt)。
- "${activeEditorLong}": 文件的完整路径 (例如 /Users/Development/myFolder/myFileFolder/myFile.txt)。
- "${activeFolderShort}": 文件所在的文件夹名称 (例如, myFileFolder)。
- "${activeFolderMedium}": 相对于工作区文件夹的、包含文件的文件夹的路径, (例如 myFolder/myFileFolder)。
- "${activeFolderLong}": 文件所在文件夹的完整路径 (例如 /Users/Development/myFolder/myFileFolder)。
- "${folderName}": 文件所在工作区文件夹的名称 (例如 myFolder)。
- "${folderpath}": 文件所在工作区文件夹的路径 (例如 /Users/Development/myFolder)。
- "${rootName}": 打开的工作区或文件夹的名称 (例如 myFolder 或 myWorkspace)。
- "${rootPath}": 打开的工作区或文件夹的文件路径 (例如 /Users/Development/myWorkspace)。
- "${appName}": 例如 VS Code。
- ${remoteName}: 例如 SSH
- ${dirty}: 表明活动编辑器具有未保存更改的时间的指示器。
- "${separator}": 一种条件分隔符 ("-"), 仅在被包含值或静态文本的变量包围时显示。




Terminal › Integrated › Tabs: Description
控制显示在标题右侧的终端说明。根据上下文替换变量:

- ${cwd}: 终端的当前工作目录
- ${cwdFolder}: 终端的当前工作目录，当值与- 初始工作目录不同时，显示在多根工作区或单个根- 工作区中。在 Windows 上，仅当启用 shell - 集成时才会显示此内容。
- ${workspaceFolder}: 在其中启动终端的工作- 区
- ${local}: 指示远程工作区中的本地终端
- ${process}: 终端流程的名称
- ${separator}: 仅在由带有值或静态文本的变- 量括住时才显示的条件分隔符(" - ")。
- ${sequence}: 进程提供给终端的名称
- ${task}: 指示此终端与任务关联



Terminal › Integrated › Tabs: Title
控制终端标题。根据上下文替换变量:

- ${cwd}: 终端的当前工作目录
- ${cwdFolder}: 终端的当前工作目录，当值与初始工作目录不同时，显示在多根工作区或单个根工作区中。在 Windows 上，仅当启用 shell - 集成时才会显示此内容。
- ${workspaceFolder}: 在其中启动终端的工作区
- ${local}: 指示远程工作区中的本地终端
- ${process}: 终端流程的名称
- ${separator}: 仅在由带有值或静态文本的变量括住时才显示的条件分隔符(" - ")。
- ${sequence}: 进程提供给终端的名称
- ${task}: 指示此终端与任务关联