# CSS

> 为网络添加样式

[toc]

## 术语解释

CSS规则 = 选择器 + 声明块

### 选择器

> 选择器：选中元素（花括号前面），用来确定样式的范围

1. **ID选择器**：选中的是对应**ID值**的元素`
```CSS
<head>
    ……
    <style>
        #test{
            color:red;
            background-color:lightblue;
            text-align:center;
        }
    </style>
</head>
<body>
    <h1>……</h1>
    <p id="test">……</p>
    <p>……</p>
</body>
```

2. **元素选择器**：可以选择页面上所有的同一元素，与该元素的位置无关
```CSS
<head>
    ……
    <style>
        p{
            color:red;
            background-color:lightblue;
            text-align:center;
        }
    </style>
</head>
<body>
    <h1>……</h1>
    <p>……</p>
    <p>……</p>
</body>
```

3. **类选择器**
```CSS
<head>
    ……
    <style>
        .red{
            color: red;
            background-color: lightblue;
            text-align: center;
        }
        .big-center{
            font-size: 3em;

            text-align: center;
        }
    </style>
</head>
<body>
    <h1 class="red big-center">……</h1>
    <p class="red">……</p>
    <p>……</p>
</body>
```

### 声明块

> 声明块：（出现在花括号内）声明块中包含很多声明（属性），每一个声明（属性）表达了某一方面的样式

## CSS代码书写位置

1. **内部样式表**

>书写在style元素内部（通常把该元素放在head标签内，方便浏览器在读取网页时能最先将样式读取，但并不是一定放在这）

2. 内联样式表
```CSS
直接书写在元素的style属性中
<h1 style="color:red; background-color:lightblue;">
```

3. 外部样式表[推荐]

> 将样式书写到独立的CSS文件中

```CSS
<head>
    ……
    <link rel="stylesheet" href="./CSS/index.css">
</head>
```
1). 外部样式表可以解决多页面样式重复的问题
2). 有利于浏览器缓存，从而提高页面响应速度
3). 有利于代码分离（HTML和CSS代码分离），更容易阅读和维护

# 常见样式声明

1. **color**

元素内部的文字颜色

**预设值**：定义好的单词

**三原色，色值**：光学三原色（红、绿、蓝），每种颜色可以使用 0-255 之间的数字来表达，色值

```html
rgb表示法：
color:rgb(0,140,140);

hex（16进制）表示法：
#红绿蓝
color:#008c8c;
```
<!--
淘宝红：#ff4400 #f40
黑色：#000
白色：#fff
红色：#f00
绿色：#0f0
蓝色：#00f
灰色：#ccc
-->

2. **background**

元素背景颜色

3. **font-size**

元素内部文字的尺寸大小

单位：
1) px：绝对单位 像素，（简单理解为文字的高度占多少个像素）
2) em：相对单位 相对于父元素的字体大小（最终都会换算为真实的像素值）
<!-- em指的是父元素的字体大小 -->

每个元素必须有字体大小，如果没有声明，则直接使用父元素的字体大小，如果没有父元素，则使用基准字号（浏览器所设置的字号）

> user agent: UA，用户代理（浏览器）

<!-- CSS中的注释方式为 /*（注释内容）*/ -->

4. **font-weight**

文字粗细程度，可以取值为数字，可以取值为预设值（normal（相当于 400）、bold（相当于 700））

> strong元素，默认的样式为加粗

```CSS
<strong>
    表示重要的，不能忽略的
</strong>
```

1. **font-family**

文字类型

必须用户计算机中存在的字体才会有效

使用多种字体，以匹配

```CSS
div{
    font-family: consolas,微软雅黑,Arial,sans-serif;
}
/* sans-serif，非衬线字体 */
```

6. **font-style**

字体模式，通常用它设置斜体（italic）

> i元素，默认样式是倾斜字体；实际使用的时候，通常用它表示一个图标（非正式）

> em元素，默认样式为斜体字体，表示强调内容

7. **text-decoration**

文本修饰（给文本加线）

> a元素：默认样式为添加下划线
> del元素：表示错误的内容，默认样式为 text-decoration: line-through
> s元素：表示过期的内容，默认样式也为 line-through

8. **text-indent**

首行文本缩进
<!-- indent：缩进 -->

9. **line-height**

每行文本的高度，该值越大，每行文本的距离越大

设置行高为容器的高度，可以让单行文本垂直居中

行高可以设置为纯数字，表示相当于当前元素的字体大小

10. **width**

宽度

11. **height**

高度

12. **letter-space**

文字间隙

13. **text-aligh**

元素内部文字的水平排列方式'


# 选择器

选择器的作用：帮助你精准地选中想要的元素

## 简单选择器

1. ID选择器
2. 元素选择器
3. 类选择器
4. 通配符选择器

*，表示选中所有元素

```CSS
* {
    color:red;
}
```

5. 属性选择器

根据属性名和属性值选中元素

```CSS
/* 选中所有具有href属性的元素 */
[href] {
    color:red;
}

/* 选中具有href属性并且具有相应属性值的元素 */
[href=value] {
    color:blue;
}

[attr~=value] {
    /* 匹配带有一个名为attr的属性的元素，其值正为value，或者匹配带有一个attr属性的元素，其值有一个或者更多，至少有一个和value匹配。
    注意，在一列中的好几个值，是用空格隔开的。 */
}

[attr|=value] {
    /* 匹配带有一个名为attr的属性的元素，其值可正为value，或者开始为value，后面紧随着一个连字符。 */
}

/* 其它的具体查mdn */
```

6. 伪类选择器

选中某些元素的某种状态

<!-- 元素前要加 :  -->

hover：鼠标悬停状态

```CSS
a:hover {/* 选中鼠标悬停时候的a元素（若:前不写元素名称则默认选中所有元素） */
    color:red;
}
```

active：激活状态，一般是指鼠标按下状态

```CSS
a:active {/* 选中鼠标按下时的a元素 */
    color:red;
}
```

link：超链接未访问时的状态

```CSS
a:link {
    color:blue;
}
```

visited：超链接访问过后的状态

```CSS
a:visited {
    color:black;
}
```

如果需要同时书写这四个元素，则需要按照link、visited、hover、active的顺序进行书写

7. 伪元素选择器

<!-- 元素前要加 :: -->

before

```CSS
span::before {/* before将会自动生成一个无名元素，且该元素将会出现在span的最前部分 */
    /* 特殊元素content,只能出现在before或after中，用于表示该元素中的内容 */
    content:"《》";
}
```

after

用法类似于before

## 选择器的组合

1. 并且 —— （什么都不加）

```CSS
p.red {
    text-indent: 2em;
    line-height: 2;
}
```

2. 后代元素 —— 空格

```CSS
.red li {/* 选中的是class为red的元素的后代元素ui */
    color: red;
}
```

3. 子元素 —— >

```CSS
.abc > .bcd {
    /*blank*/
}
```

4. 相邻兄弟元素 —— +

```CSS
.special + li {/* 选中class为special的元素和它的下一个li元素*/
    /*blank*/
}
```

5. 兄弟元素 —— ~

```CSS
.special ~ li {/* 选中class为special的元素以及它下面的所有li元素*/
    /*blank*/
}
```

## 选择器的并列

多个选择器，用逗号分隔

语法糖

```CSS
div,
p {
    /*blank*/
}
```

# 层叠

> 层叠样式表

声明冲突：同一份样式，多次应用到同一个元素

层叠：解决声明冲突的过程，浏览器自动处理（权重计算）

## 1. 比较重要性

重要性从高到低：

> 作者样式表：开发者书写的样式

1）作者样式表中的!important样式

2）作者样式表中的普通样式

3）浏览器默认样式表中的样式

## 2. 比较特殊性

总体规则：选择器选中的范围越窄越特殊

具体规则：通过选择器，计算出一个4位数（xxxx）

1. 千位：如果是内敛样式，记1，否则记0
2. 百位：等于选择器中所有id选择器的数量
3. 十位：等于选择器中所有类选择器、属性选择器、伪类选择器的数量
4. 个位：等于选择器中所有元素选择器、伪元素选择器的数量

<!-- 该四位数是逢256进一，因此在实际使用的时候并不需要考虑进位的问题 -->

## 3. 比较原次序

代码书写**靠后**的胜出

## 应用

1. 重置样式表

书写一些作者样式，覆盖浏览器的默认样式

重置样式表，覆盖浏览器的默认样式

常见的重置样式表：normalize.css、reset.css、meyer.css

2. 爱恨法则

link > visited > hover > active（由使用逻辑安排其原次序）


# 继承

子元素会继承父元素的**某些**CSS属性

通常，跟**字体内容相关**的属性都能被继承


# 属性值的计算过程

一个元素一个元素依次渲染，顺序按照页面文档的树形目录结构进行

渲染每个元素的前提条件：该元素的所有CSS属性必须有值

一个元素，从所有属性都没有值，到所有属性都有值，这个计算过程，叫做属性的计算过程

1. **确定声明值**

参考样式表中没有冲突的声明，作为CSS属性值

2. **层叠冲突**

对样式表有冲突的声明使用层叠规则，确定CSS属性值
<!-- 比较重要性 特殊性 源次序 -->

3. **使用继承**

对仍然没有值的属性，若可以继承，则继承父元素的值

4. **对仍然没有值的属性，使用默认值**

特殊的两个CSS取值：

- **inherit**：手动（强制）继承，将父元素的值取出应用到该元素

- **initial**：初始值，将该属性设置为默认值


# 盒模型

box：盒子，每个元素在页面中都会生成一个矩形区域（盒子）

盒子类型：

1. 行盒，display等于inline的元素
2. 块盒，display等于block的元素

display默认值属性为inline

行盒在页面中不换行，块盒在页面中独占一行

浏览器默认样式表设置的块盒：容器元素，h1~h6，p

常见的行盒：span、a、img、video、audio

## 盒子的组成部分

无论是行盒、还是块盒、都由下面几个部分组成，从内到外分别是：

1. 内容 content

width、height，设置的是盒子内容的宽高

内容部分通常叫做整个**盒子的内容盒 content-box**

2. 填充（内边距） padding

盒子边框到盒子内容的距离

padding-left、padding-right、padding-top、padding-bottom

padding：简写属性

padding：上 右 下 左

填充区 + 内容区 = **填充盒 padding-box**

3. 边框 border

边框 = 边框样式 + 边框宽度 + 边框颜色
<!-- 都为简写属性（速写属性） -->
边框样式：border-style
边框宽度：border-width
边框颜色：border-color

边框 + 填充区 + 内容区 = **边框盒 border-box**

4. 外边距 margin

边框到其它盒子的距离

margin-top、margin-left、margi-right、margin-bottom

