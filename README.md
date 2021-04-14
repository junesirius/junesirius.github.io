# 文档说明

本项目为写手“六月的天狼星”的[个站](https://junesirius.github.io)源代码，由作者本人设计、排版、维护。

本文档用于解释网站设计相关的各文件，未提及文件多为Jekyll、Bootstrap等的必要配置文件，无需改动。

网站设计中采用的编程语言为Liquid语言，静态网站生成器为Jekyll，详细文档参见：[Liquid中文文档](https://liquid.bootcss.com/basics/introduction/)、[Jekyll中文文档](https://jekyllcn.com/docs/home/)。

## 目录

- [基本信息设置文件](#基本信息设置文件)
  * [\_config.yml](#_configyml)
  * [\_data/description.yml](#_datadescriptionyml)
  * [feed.xml](#feedxml)
  * [LICENSE](#license)
  * [robots.txt](#robotstxt)
- [排版布局相关文件](#排版布局相关文件)
  * [\_layouts](#_layouts)
    + [default.html](#defaulthtml)
    + [post.html](#posthtml)
  * [\_includes](#_includes)
    + [header.html](#headerhtml)
    + [footer.html](#footerhtml)
    + [sidebar.html](#sidebarhtml)
  * [\_sass](#_sass)
    + [theme.scss](#themescss)
    + [custom\_color.scss](#custom_colorscss)
    + [syntax.scss](#syntaxscss)
- [网站主要界面](#网站主要界面)
  * [index.html（首页）](#indexhtml首页)
  * [categories.md（分类页）](#categoriesmd分类页)
  * [categories-detail.md（分类细节）](#categories-detailmd分类细节)
  * [tags.md（标签页）](#tagsmd标签页)
  * [characters.md（人物页）](#charactersmd人物页)
  * [longnovels.md（长篇小说页）](#longnovelsmd长篇小说页)
  * [archive.md（归档页）](#archivemd归档页)
  * [404.md（报错页）](#404md报错页)
- [存文相关文件](#存文相关文)
  * [\_posts](#_posts)
  * [\_drafts](#_drafts)
  * [assets](#assets)
- [本地调试基本步骤](#本地调试基本步骤)

## 基本信息设置文件

### [\_config.yml](https://github.com/junesirius/junesirius.github.io/blob/master/_config.yml)

- name: 作者笔名
- name_en: 作者英文笔名（此项可空）
- url: 个站链接
- baseurl: 个站根目录（当根目录即为个站链接时，此项可空）
- paginate: 首页的每页文章数量
- permalink: 文章自动生成的网址链接格式

### [\_data/description.yml](https://github.com/junesirius/junesirius.github.io/blob/master/_data/description.yml)

个人签名，默认置于头像下方，位置居中。由`<br>`实现换行。

### [feed.xml](https://github.com/junesirius/junesirius.github.io/blob/master/feed.xml)

在“[https://junesirius.github.io/feed.xml](https://junesirius.github.io/feed.xml)”中集成显示所有文章信息。本文档无需改动。

### [LICENSE](https://github.com/junesirius/junesirius.github.io/blob/master/LICENSE)

版权及许可证信息，采用“[Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode)”。

### [robots.txt](https://github.com/junesirius/junesirius.github.io/blob/master/robots.txt)

面向网络搜索引擎的漫游器（即网络爬虫），设置为拦截所有机器人，禁止爬虫获取本站任意目录。

## 排版布局相关文件

### [\_layouts](https://github.com/junesirius/junesirius.github.io/tree/master/_layouts)

本文件夹下的`default.html`和`post.html`确定各文章页的主要排版布局。

#### [default.html](https://github.com/junesirius/junesirius.github.io/tree/master/_layouts/default.html)

确定每个采用default布局的页面都包含了页眉（header）、页脚（footer）、侧边栏（sidebar），且侧边栏与主要内容的宽度比例为1:3。

#### [post.html](https://github.com/junesirius/junesirius.github.io/tree/master/_layouts/post.html)

在`default.html`的基础上细化确定各文章页格式。

页面首行以`h2`字号显示文章标题。换行显示日期、字数统计、视角、首发位置、阅读量，然后是正文部分。在正文下方分行显示文章所属的分类、所注的标签和人物。页面最末显示分页器，可跳转到按时间顺序发布的前一篇或后一篇。

- **日期**：显示规则为`月-日-年`（可在`_config.yml`的`data_format`下方`title`处修改格式）。
- **字数统计**：采用Liquid语言自带的`size`方法，英文每个字母统计为一字，因此字数统计仅供参考。本地调试时可采用`number_of_words: "auto"`方法将英文每个单词统计为一字得到更准确的字数统计，但该方法在git page中无效，会导致调试错误及网站崩溃。
- **视角**：提取并显示各文章台头的`pov`标签后内容，通常按文章中人称标注`第一/二/三人称`。可省略。
- **首发位置**：提取并显示各文章台头的`origin`标签后内容，按文章首发位置标注。若未在别处公开发表，则标注`github`或省略。
- **阅读量**：借助“[不蒜子](http://ibruce.info/2015/04/04/busuanzi/)”脚本自动统计各文章阅读量，每次点开或刷新页面会进行计数。
- **分类**：提取并显示各文章台头的`categories`标签后内容（同一文章可同时属于多个分类），并统计该分类在本站所有文章中出现次数。
- **标签**：提取并显示各文章台头的`tags`标签后内容（同一文章可同时拥有多个标签），并统计该标签在本站所有文章中出现次数。可省略。
- **人物**：提取并显示各文章台头的`characters`标签后内容（同一文章可同时拥有多个人物），并统计该人物在本站所有文章中出现次数。可省略。

### [\_includes](https://github.com/junesirius/junesirius.github.io/tree/master/_includes)

本文件夹内文件用于设置通用的页眉、页脚、侧边栏样式。

#### [header.html](https://github.com/junesirius/junesirius.github.io/tree/master/_includes/header.html)

- 在\<head\>的\<title\>标签下确定各页面标题显示为：“文章标题 | 作者笔名”
- 在\<head\>的\<link rel="icon"\>标签下设置本站的图标，图标存储位置为[favicon.jpg](https://github.com/junesirius/junesirius.github.io/blob/master/assets/images/favicon.jpg)
- 设置导航栏固定在窗口顶部，不随页面下滑而改变位置
- 导航栏按钮包括：
  - 左上角笔名、**首页**：自动跳转至本站首页
  - **分类**：跳转至categories.html
  - **标签**：跳转至tags.html
  - **人物**：跳转至characters.html
  - **长篇**：跳转至longnovels.html
  - **归档**：跳转至archive.html

#### [footer.html](https://github.com/junesirius/junesirius.github.io/tree/master/_includes/footer.html)

- **版权**：所有者为本站作者（同时标注中文及英文笔名），时间为当前年份。
- **致谢**：致谢者信息及链接存储于[\_data/thanks.yml](https://github.com/junesirius/junesirius.github.io/blob/master/_data/thanks.yml)。

#### [sidebar.html](https://github.com/junesirius/junesirius.github.io/tree/master/_sidebar.html)

依次显示：头像、个签、最近更新、热门圈子、热门标签、长篇连载

- **头像**：图片与本站图标相同（也可选择不同图片），存储于[favicon.jpg](https://github.com/junesirius/junesirius.github.io/blob/master/assets/images/favicon.jpg)，显示为圆形。
- **个签**：文字居中排列，内容存储于[\_data/description.yml](https://github.com/junesirius/junesirius.github.io/blob/master/_data/description.yml)。
- **最近更新**：从所有更新的文章中自动选取最新的五篇，按从新到旧顺序显示标题并提供跳转链接。显示文章数量可进行更改。
- **热门圈子**：统计所有`categories`标签，选取文章数量最多的五个分类，按从多到少顺序显示类别名称及对应文章数量，点击链接可跳转至`categories.html`中对应分类的位置。显示的热门分类数量可进行更改。
- **热门标签**：统计所有`tags`标签，选取文章数量最多的五个标签，按从多到少顺序显示标签名称及对应文章数量，点击链接可跳转至`tags.html`中对应标签的位置，查看拥有该标签的所有文章。显示的热门标签数量可进行更改。
- **长篇连载**：按字母顺序显示所有长篇小说标题，点击链接可跳转至`longnovels.html`中对应位置。

### [\_sass](https://github.com/junesirius/junesirius.github.io/tree/master/_sass)

#### [theme.scss](https://github.com/junesirius/junesirius.github.io/tree/master/_sass/theme.scss)

包含大部分自定义的css格式，包括页眉、页脚、侧边栏、文章页的主要格式。设置个站背景纹理图片为[canvas_bg.jpg](https://github.com/junesirius/junesirius.github.io/blob/master/assets/images/canvas_bg.jpg)。

#### [custom\_color.scss](https://github.com/junesirius/junesirius.github.io/tree/master/_sass/custom_color.scss)

自定义主题色。

- <span style="color: #28323c;">main-color（主题色）：用于页眉、页脚、侧边栏的背景色，及文章正文字体颜色，建议使用深色。本站使用色号为：![#28323c](https://via.placeholder.com/15/36165a/000000?text=+)`#28323c`</span>
- <span style="color: #9d98fc">second-color（悬浮色）：当鼠标悬浮在超链接上时显示的颜色，建议使用浅色。本站使用色号为：![#9d98fc](https://via.placeholder.com/15/9d98fc/000000?text=+)`#9d98fc`</span>
- <span style="color=#36165a;">third-color（标题色）：首页及各文章页显示的文章标题颜色，建议选择深色。本站使用色号为：![#36165a](https://via.placeholder.com/15/36165a/000000?text=+)`#36165a`</span>

#### [syntax.scss](https://github.com/junesirius/junesirius.github.io/tree/master/_sass/syntax.scss)

来自[Jekyll](https://github.com/jekyll/jekyll)，未作更改。

## 网站主要界面

### [index.html（首页）](https://github.com/junesirius/junesirius.github.io/blob/master/index.html)

在`index.html`按时间顺序由新到旧显示文章日期、标题、缩略内容。每页文章数由[\_config.yml](https://github.com/junesirius/junesirius.github.io/blob/master/_config.yml)中`paginator`后的数值进行调整，本站采用每页7篇文章。

每篇文章的缩略内容由各文章页台头`description`标签后内容确定，若该标签为空，则截取除空格外的前150字符（该数值可调整）。

点击各文章标题可进入文章页。

### [categories.md（分类页）](https://github.com/junesirius/junesirius.github.io/blob/master/categories.md)

在`categories.html`页面按字母顺序依序排列所有出现过的文章分类（台头的`categories`），在每个分类下按字母顺序列举所有属于该分类的文章中出现过的标签及人物。

点击各标签可跳转至`tags.html`页面的对应标签位置，点击各人物可跳转至`characters.html`页面的对应位置，点击分类的标题可跳转至`categories-detail.html`页面的对应位置。

### [categories-detail.md（分类细节）](https://github.com/junesirius/junesirius.github.io/blob/master/categories-detail.md)

在`categories-detail.html`页面按字母顺序依序排列所有出现过的文章分类（台头的`categories`），在每个分类下按时间顺序从新到旧列举所有属于该分类的文章。点击文章标题可进入文章页。

### [tags.md（标签页）](https://github.com/junesirius/junesirius.github.io/blob/master/tags.md)

在`tags.html`页面按字母顺序依序排列所有出现过的标签（台头的`tags`），在每个标签下按时间顺序从新到旧列举所有注有该标签的文章。点击文章标题可进入文章页。

### [characters.md（人物页）](https://github.com/junesirius/junesirius.github.io/blob/master/characters.md)

在`characters.html`页面按字母顺序依序排列所有出现过的人物（台头的`characters`），在每个人物下按时间顺序从新到旧列举所有出现该人物的文章。点击文章标题可进入文章页。

### [longnovels.md（长篇小说页）](https://github.com/junesirius/junesirius.github.io/blob/master/longnovels.md)

在`longnovels.html`页面按字母顺序依序排列所有出现过的长篇小说（台头的`long_novels`），在每个长篇小说标题下按时间顺序从新到旧列举所有属于该长篇系列的连载文章。点击文章标题可进入文章页。

### [archive.md（归档页）](https://github.com/junesirius/junesirius.github.io/blob/master/archive.md)

在`archive.html`页面按时间顺序从新到旧列举所有文章标题，并在右侧标注发表时间。点击文章标题可进入文章页。

### [404.md（报错页）](https://github.com/junesirius/junesirius.github.io/blob/master/404.md)

当无法在主站根目录下找到对应页面时自动跳转到`404.html`页面，显示“404 未找到页面 Page not found”。本页较为简陋，可进行更多设计。

*一个冷知识*：当直接输入404.html时显示的“未找到页面”是一句谎言，因为实际已找到这个`404.html`网页，否则不会出现这句提示。

## 存文相关文件

### [\_posts](https://github.com/junesirius/junesirius.github.io/blob/master/_posts)

本文件夹用于储存文章，所有文章的文件名必须遵守`年-月-日-标题.md`的格式。

文章台头需被包含在两行`---`之间，有以下内容：

- layout: `post`，不用修改
- title: 文章标题，需小心特殊字符可能无法被html语言编译，例如`&`需用`&amp;`代替。
- date: 发表时间，格式为`年-月-日 分:秒`。不可早于真实时间，否则无法编译成功。
- categories: 文章所属分类，同一篇文章可属于多个分类，由`["分类1", "分类2"]`的格式进行区分，注意此处的引号和逗号都必须是英文字符。
- characters: 文章中出现人物，当拥有多个人物时使用`["人物1", "人物2"]`的格式进行区分，否则在人名出现空格时会被默认分割为不同人物。此项可为空。
- tags: 文章标签，拥有多个标签时用`["标签1", "标签2"]`的格式进行区分。
- pov: 文章写作视角，可写`第一/二/三人称`。此项可省略。
- origin: 文章首发位置，未向外发表的文章可省略此项或写`github`。
- long_novels: 同一篇长篇连载小说的各文章的此项需统一，这样才能在`longnovels.html`页面被归类在同一个长篇标题下。
- description: 文章简介，用于展示在首页，字数不限。若省略，则在首页自动展示文章前150字（该字数可在`index.html`页调整）。
- published: `true`/`false`。此项默认为`true`，若填写`false`，则该文章不会出现在个站首页，即使本地调试时使用`--drafts`选项也不会出现。

### [\_drafts](https://github.com/junesirius/junesirius.github.io/blob/master/_drafts)

本文件夹存储所有不打算发表在个站的草稿文章，文件标题、台头格式等可不遵守`_posts`的格式要求。当git page网站在线编译时会自动忽略本文件夹，但在本地调试时可通过`--drafts`，命令进行编译查看。

### [assets](https://github.com/junesirius/junesirius.github.io/blob/master/assets)

本文件夹用于存放图片、视频、音乐等多媒体文件，在文章页通过嵌入的方式进行展示。

## 本地调试基本步骤

1. 安装ruby：可使用[RubyInstaller](https://rubyinstaller.org/)；
2. 安装并更新gem：`gem update`；
3. 安装jekyll：`gem install jekyll bundler`；
4. 进入个站所在文件夹，在命令行中运行`jekyll server`，在`localhost: 4000`查看本地编译的个站，可通过终端报错信息帮助debug（因为git page的编译报错信息中提示信息通常较少）；
5. 在命令行中运行`jekyll server --drafts`可将`_drafts`中文章也展示在本地编译的个站中；
6. 在命令行中运行`jekyll server --port xxxx`可将默认`4000`端口修改为任意端口的`localhost: xxxx`；
7. gemlock最新一次自动更新后，`jekyll`命令可能失效，可使用`bundle exec jekyll`命令作为替代，`--port`和`--drafts`用法仍同上；
8. 详细的jekyll文档参见：[https://jekyllrb.com/docs/](https://jekyllrb.com/docs/)。