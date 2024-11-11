from lib import log # 日志输出库

# 预备输出
log.out(0, "Basic Information ready...")

# 基本信息
ver = "1.0 Alpha"
author = "ASTerisk Games"
auth_abbr = "ASTerisk Games"
title = "PsExtra Desktop " + ver + " by " + auth_abbr
updmd = """
# PsExtra Desktop Release Notes

## 1.0 Alpha (November 11, 2024)

1. Initial release.
"""

# 定义内容
what_text = """
伪本地化(pseudo-localization, 语言环境 **qps-ploc, qps-plocm, qps-ploca, en-XA, en-XB**), 

是通过模拟本地化过程, 以有效地调查在本地化中出现的问题

_(如字符无法正常显示, 或因字符串过长而导致语段显示不完整等)_。

在伪本地化过程中, 英文字母会被替换为来自其他语言的重音符号和字符。

_(例如, 字母 a 可以被 **αäáàāāǎǎăăåå** 中的任何一个替换)_,

还会添加分隔符等以增加字符串长度。

例: “Windows Photo Gallery (Windows 照片库)”→“ [1iaT9][ Ẅĭпðøωś Þнôтŏ Ģάŀļєяÿ !!! !] ”

### 更多信息: 

- https://docs.microsoft.com/zh-cn/globalization/methodology/pseudolocalization

- https://zhuanlan.zhihu.com/p/613293858
"""
about_text = "伪本地化演示程序 " + ver + "\n开发者: " + author +"\n贡献者、使用到的第三方项目详见 GitHub 项目仓库\n(https://github.com/suntrise/Pseudo-localization-Demo)\nMade with ❤ for YOU!\n使用WTFPL许可协议开源 (不涉及使用到的第三方库)" 
