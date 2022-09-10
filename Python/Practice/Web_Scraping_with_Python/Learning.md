# BeautifulSoup

## 运行 BeautifulSoup

当你创建一个 BeautifulSoup 对象时，需要传入两个参数：

`bs = BeautifulSoup(html.read(), 'html.parser')`

- 第一个参数时该对象所基于的 HTML 文本，第二个参数指定了你希望 BeautifulSoup 用来创建该对象的解析器。在大多数情况下，你选择任何一个解析器都差别不大
- `html.parser` 是 Python 3 中的一个解析器，不需要单独安装
- 另一个常用的解析器是 `lxml`，可以通过 pip 进行安装 `pip3 install lxml`
- `html5lib` 也是一个常用的解析器

BeautifulSoup 还可以使用 urlopen 直接返回的文件对象，而不需要先调用 `.read()` 函数

**获取页面中所有指定的标签**

`bs.find_all(tagname, tagAttributes)`

**get_text()**

- get_text() 会清除你正在处理的 HTML 文档中的所有标签，然后返回一个只包含文字的 Unicode 字符串

## BeautifulSoup 中的 find() 和 find_all()

这两个函数能够帮助你通过标签的不同的属性轻松地过滤 HTML 页面，查找需要的标签组或单个标签

定义：

`find_all(tag, attributs, recursive, text, limit, keywords)`
`find(tag, attributs, recursive, text, keywords)`

- 标签参数 tag —— 你可以传递一个标签的名称或多个标签名称组成的 Python 列表做标签参数
- 属性参数 attributs 用一个 Python 字典封装一个标签的若干属性和对应的属性值
- 递归参数 recursive 是一个布尔变量。如果你将其设置为 True， find_all 会根据你的要求去查找标签参数的所有子标签，以及子标签的子标签；如果 recursive 设置为 False， find_all就只查找文档的一级标签。