# 🌐伪本地化演示程序

![image](https://github.com/suntrise/Pseudo-localization-Demo/assets/89229642/186c45e6-fbdf-46ee-9438-1d3a28d57216)

这是一个伪本地化工具, 可用于某些本地化工作用途, 当然也可以作为一个玩具或者工具~

![GitHub Action](https://github.com/suntrise/Pseudo-localization-Demo/actions/workflows/build.yml/badge.svg)
![GitHub all releases](https://img.shields.io/github/downloads/suntrise/Pseudo-localization-Demo/total)
![GitHub Repo stars](https://img.shields.io/github/stars/suntrise/Pseudo-localization-Demo)
![GitHub contributors](https://img.shields.io/github/contributors/suntrise/Pseudo-localization-Demo)
![GitHub](https://img.shields.io/github/license/suntrise/Pseudo-localization-Demo)
![Python require](https://img.shields.io/badge/python-≥3.7-brightgreen.svg)


网页版：https://suntrise.github.io/pseudo

## 👇使用

如果您没有Python环境且比较懒, 可以移步Release下载, tar.gz版本适用于Linux, exe版本适用于Windows, 其他操作系统建议下载源码并执行

注意, 要在本地查看并修改源码, 需要安装Python, 版本最少为3.7以保障兼容性

### 🚀依赖安装

运行...

~~~Bash
pip install flet
pip install pyperclip
~~~

若要使用或编辑Mini, 还需额外执行...

~~~Bash
pip install fleter
~~~

以上如果嫌一个一个来麻烦，可以直接执行..

~~~Bash
pip install -r requirements.txt
~~~

若需编辑旧版, 还需要额外运行...

~~~Bash
pip install PyQt5 
~~~

使用`PyQt6`稍加修改其实也行, 不过组件可能会变大

如果嫌慢可以改用清华源, 参考[此处](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

### 🛠️编译

#### Pyinstaller (简单)

运行......

~~~Bash
pip install pywin32
pip install pyinstaller
~~~

定位到代码根目录, 运行......

~~~Bash
pyinstaller pslo.pyw -F -w -i pslo_icon.ico
~~~

Mini版则执行

~~~Bash
pyinstaller pslo_mini.pyw -F -w -i pslo_icon.ico
~~~

编译完可能需要Wine或者Crossover才可以运行, 因此我们依旧推荐直接执行pyw文件或使用下一种方案

#### Nuitka (推荐)

请提前安装好**Visual Studio生成工具**或者**GCC(MinGW)**(使用MinGW需要在命令行添加`--mingw`)

运行......

~~~Bash
pip install nuitka
~~~

定位到代码根目录, 运行......

~~~Bash
nuitka pslo.pyw --onefile --windows-disable-console --windows-icon-from-ico=pslo_icon.ico --standalone --show-progress
~~~

Mini版则执行

~~~Bash
nuitka pslo_mini.pyw --onefile --windows-disable-console --windows-icon-from-ico=pslo_icon.ico --standalone --show-progress
~~~

*注: 部分系统可能要将`nuitka`改为`nuitka3`*

Linux完成编译后须执行......

~~~Bash
chmod +x [编译后文件名].bin
~~~

才可以执行

该方法适用于Windows和Linux, 参数可以按需添加, 详见[此处](https://github.com/Nuitka/Nuitka/)

## 🗒️备注

- 经过测试, 在虚拟机下运行可能会造成非正常闪烁现象, 可能是flet库的驱动驱动兼容的问题

- macOS由于条件原因没法测试, 望有条件的用户可以为我们提供相应的帮助与支持!

- 若想获取最新测试版本, 可以看看Action里面哟(未经过完整测试)

- 代码写的有点难看, 望各位大佬多多指导!

## 📦使用到的第三方项目

### 2.x 及更新版本

[flet-dev/flet](https://github.com/flet-dev/flet)

[asweigart/pyperclip](https://github.com/asweigart/pyperclip)

### 1.x

[Riverbank Computing PyQt5](https://www.riverbankcomputing.com/software/pyqt/)

## 📄许可协议

使用**WTFPL**许可协议开源[^注], 你想干嘛就干嘛

![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png)

[^注]: 或许可以解释为**W**indows **T**iny **F**orm **P**seudo-**L**ocalization
