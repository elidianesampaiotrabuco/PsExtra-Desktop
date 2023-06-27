import flet as ft
import random
import pyperclip
import webbrowser
import requests

# 基本信息
ver = "v3.4p"
author = "Suntrise (STR)"
auth_abbr = "STR"
title = "伪本地化演示程序 " + ver +" by "+auth_abbr
updmd = """
# 更新日志

## v3.4p - 2023.6.27

1. 新增元音重复；

## v3.3p（By What_Demon） - 2023.6.24

1. 加入检查更新;
2. 细节、逻辑进行优化.

## v3.2p - 2023.6.23

1. 新增 en-XB (倒序语段) 的伪本地化方式;
2. 新增配色设置;
3. 新增“清空历史记录”.

## v3.1p - 2023.6.23

1. 引入历史记录功能;
2. 布局进行小改.
"""

# 字符集
arra = ["ä", "ā", "á", "ǎ", "à", "ă", "å", "ǻ", "ã", "ǟ", "ǡ", "ǻ", "ȁ", "ȃ", "ȧ", "ᶏ", "ḁ", "ẚ", "ạ", "ả", "ấ", "ầ", "ẩ", "ẫ", "ậ", "ắ", "ằ", "ẳ", "ẵ", "ặ", "ɑ", "α", "ά", "ὰ", "ἀ", "ἁ", "ἂ", "ἃ", "ἆ", "ἇ", "ᾂ", "ᾃ", "ᾰ", "ᾱ", "ᾲ", "ᾳ", "ᾴ", "ᾶ", "ᾷ", "ⱥ", "𐓘", "𐓙", "𐓚"]
arraa = ["Ā", "Á", "Ǎ", "À", "Â", "Ã", "Ä", "Å", "Ǻ", "Ά", "Ă", "Δ", "Λ", "Д", "Ą"]
arrb = ["b", "ь", "в", "Ъ", "Б", "б", "β", "ƀ", "ƃ", "ɓ", "ᵬ", "ᶀ", "ḃ", "ḅ", "ḇ", "ꞗ", "ḃ"]
arrbb = ["ß", "฿", "Ḃ"]
arrc = ["c", "ç", "ς", "ĉ", "č", "ċ", "ć", "ĉ", "ċ", "ƈ", "ȼ", "¢", "ɕ", "ḉ", "ꞓ", "ꞔ"]
arrcc = ["Č", "Ç", "Ĉ", "Ć", "€", "Ċ", "Č", "¢"]
arrd = ["d", "ď", "đ", "₫", "ð", "δ", "ď"]
arrdd = ["Ď", "Ð", "Ḋ"]
arre = ["e", "ē", "é", "ě", "è", "ê", "ĕ", "ė", "ë", "ę", "з", "ε", "έ", "э", "℮"]
arree = ["E", "Ē", "É", "Ě", "È", "Ę", "Ё", "Σ", "Έ", "Є", "Э", "З", "Ė"]
arrf = ["f", "ƒ", "ḟ"]
arrff = ["F", "₣", "Ƒ", "Ḟ"]
arrg = ["ḡ", "ģ", "ǧ", "ĝ", "ğ", "ġ", "ǥ", "ǵ", "ɠ", "ᶃ", "ꞡ"]
arrgg = ["Ḡ", "Ǵ", "Ǧ", "Ĝ", "Ğ", "Ģ", "Ġ", "Ɠ", "Ǥ", "Ꞡ"]
arrh = ["ĥ", "ħ", "ђ", "н", "ḣ"]
arrhh = ["H", "Ĥ", "Ħ", "Ḣ"]
arri = ["ı", "ī", "í", "ǐ", "ì", "ĭ", "î", "ï", "ί", "į", "ΐ", "ι"]
arrii = ["Ī", "Í", "Ǐ", "Ì", "Î", "Ï", "Ĭ", "Ί", "ı", "İ"]
arrj = ["j"]
arrjj = ["J", "Ĵ"]
arrk = ["ƙ", "κ", "ķ", "ǩ"]
arrkk = ["К", "Ǩ", "Ķ"]
arrl = ["ŀ", "ļ", "ℓ", "ĺ", "ļ", "ľ", "ł", "₺"]
arrll = ["Ŀ", "£", "Ļ", "Ł", "Ĺ", "Ľ"]
arrm = ["m", "₥", "м", "ṁ"]
arrmm = ["M", "Ṁ"]
arrn = ["ń", "ň", "ŉ", "η", "ή", "и", "й", "ñ", "л", "п", "π", "ŋ", "ņ", "ṅ"]
arrnn = ["Ń", "Ň", "И", "Й", "Π", "Л", "Ñ", "Ŋ", "Ņ", "Ṅ"]
arro = ["ō", "ó", "ŏ", "ò", "ô", "õ", "ö", "ő", "σ", "ø", "ǿ", "ȯ"]
arroo = ["Ō", "Ó", "Ǒ", "Ò", "Ô", "Õ", "Ö", "Ό", "Θ", "Ǿ", "Ő", "Ȯ", "Ø", "Ω"]
arrp = ["p", "ρ", "ƥ", "φ", "ṗ"]
arrpp = ["P", "Þ", "₽", "Ṗ"]
arrq = ["q", "ʠ", "ɋ", "q"]
arrqq = ["Q", "Ɋ"]
arrr = ["ř", "ŗ", "г", "ѓ", "ґ", "я", "ṙ"]
arrrr = ["Ř", "Я", "Г", "Ґ", "Ŕ", "Ṙ", "₹"]
arrs = ["ś", "š", "ŝ", "ș", "ş", "ƨ", "ṡ"]
arrss = ["Š", "Ş", "Ș", "§", "$", "Ś", "Ṡ", "Ŝ"]
arrt = ["ț", "ţ", "ť", "ŧ", "т", "τ", "ṫ"]
arrtt = ["Ť", "Ţ", "Ț", "Ŧ", "Ţ", "Ṫ"]
arru = ["ū", "ú", "ǔ", "ù", "û", "ũ", "ů", "ų", "ü", "ǖ", "ǘ", "ǚ", "ǜ", "ύ", "ϋ", "ΰ", "µ", "ц", "џ"]
arruu = ["Ū", "Ǔ", "Ǖ", "Ǘ", "Ǚ", "Ǜ", "Ц", "Û", "Ú", "Ŭ," ,"Ű" ,"Ù" ,"Ů" ,"Ų"]
arrv = ["ν"]
arrvv = ["V", "V", "Ṽ", "Ṿ", "Ꝟ"]
arrw = ["ẃ", "ẁ", "ẅ", "ŵ", "ш", "щ", "ω", "ώ", "ẇ"]
arrww = ["Ẁ", "Ẃ", "Ẅ", "Ŵ", "Ш", "Щ", "₩", "Ẇ"]
arrx = ["x", "ж", "ẋ"]
arrxx = ["X", "Ж", "Ẋ"]
arry = ["y", "ỳ", "ŷ", "ч", "γ", "ẏ", "ÿ", "ý", "У", "Ў"]
arryy = ["Ϋ", "Ẏ", "Ŷ", "Ỳ", "Ύ", "Ψ", "￥", "Ч", "Ý"]
arrz = ["z", "ź", "ż", "ž", "ƶ", "ȥ", "ʐ", "ᵶ", "ᶎ", "ẑ", "ẓ", "ẕ", "ⱬ", "ż", "ζ"]
arrzz = ["Z", "Ź", "Ż", "Ž", "Ƶ", "Ȥ", "Ẓ", "Ẕ", "Ẑ", "Ⱬ", "Ż", "Ʒ", "Ǯ"]
arr1 = ["1", "₁", "¹"]
arr2 = ["2", "₂", "²"]
arr3 = ["3", "₃", "³"]
arr4 = ["4", "₄", "⁴"]
arr5 = ["5", "₅", "⁵"]
arr6 = ["6", "₆", "⁶"]
arr7 = ["7", "₇", "⁷"]
arr8 = ["8", "₈", "⁸"]
arr9 = ["9", "₉", "⁹"]
arr0 = ["0", "₀", "⁰"]
arral = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
arrba = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
suf=""
pshis=""
# 定义内容
what_text = "伪本地化(pseudo-localization, 语言环境名称为 qps-ploc, qps-plocm, qps-ploca, en-XA, en-XB), \n是通过模拟本地化过程, 以有效地调查在本地化中出现的问题\n(如字符无法正常显示, 或因字符串过长而导致语段显示不完整等）。\n在伪本地化过程中, 英文字母会被替换为来自其他语言的重音符号和字符。\n(例如, 字母 a 可以被 αäáàāāǎǎăăåå 中的任何一个替换), 还会添加分隔符等以增加字符串长度。\n例: “Windows Photo Gallery (Windows 照片库)”→“ [1iaT9][ Ẅĭпðøωś Þнôтŏ Ģάŀļєяÿ !!! !] ”\n更多信息: \nhttps://docs.microsoft.com/zh-cn/globalization/methodology/pseudolocalization, \nhttps://zhuanlan.zhihu.com/p/613293858"
about_text = "伪本地化演示程序 " + ver + "\n开发者: " + author +"\n贡献者、使用到的第三方项目详见 GitHub 项目仓库\n(https://github.com/suntrise/Pseudo-localization-Demo)" 
edge = ft.Divider(height=1, thickness=1.5)
divider = ft.Divider(height=9, thickness=1)

# 主程序
def main(page: ft.Page):
    # 伪本地化
    def pslo(e):
        global pshis
        i = 0
        m = 0
        n = 0
        v = ""
        pstr = page.pstype.value
        res = ''
        if str != "" and str != "null":
            if xab.value != "enxb":
                xab.value = "enxa"
                for l in pstr:
                    i += 1
                    if num_pslo.value == "2":
                        al = l.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('l',random.choice(arrl)).replace('L',random.choice(arrll)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('n',random.choice(arrn)).replace('N',random.choice(arrnn)).replace('o',random.choice(arro)).replace('O',random.choice(arroo)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz)).replace('1',random.choice(arr1)).replace('2',random.choice(arr2)).replace('3',random.choice(arr3)).replace('4',random.choice(arr4)).replace('5',random.choice(arr5)).replace('6',random.choice(arr6)).replace('7',random.choice(arr7)).replace('8',random.choice(arr8)).replace('9',random.choice(arr9)).replace('0',random.choice(arr0))
                    elif num_pslo.value == "1":
                        al = l.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('l',random.choice(arrl)).replace('L',random.choice(arrll)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('n',random.choice(arrn)).replace('N',random.choice(arrnn)).replace('o',random.choice(arro)).replace('O',random.choice(arroo)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz)).replace('1','①').replace('2','②').replace('3','③').replace('4','④').replace('5','⑤').replace('6','⑥').replace('7','⑦').replace('8','⑧').replace('9','⑨')
                    else:
                        al = l.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('l',random.choice(arrl)).replace('L',random.choice(arrll)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('n',random.choice(arrn)).replace('N',random.choice(arrnn)).replace('o',random.choice(arro)).replace('O',random.choice(arroo)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz))
                    if l.lower() in "aeiou":
                        al = al * (int(vowel_cs.value)+1)
                    res += al

            if xab.value == "enxb":
                for l in pstr:
                    i += 1
                res = pstr[::-1]
        
            suf = ""
            if suf_way.value == "1":           
                while i > 2 and n < (i/7): 
                    suf = suf+"!"  
                    n += 1
                    if n % 3 == 0 & n != int(i/7+1):
                        suf = suf+" "
                res = "["+ res +" " +suf +"]";  
        
            elif suf_way.value == "2":
                while n<(i/7):               
                    suf = suf+arrba[n%20]+" "
                    n+=1  
                res = "["+ res +" " +suf +"]";          
            n = 0
            suf = ""

            if hash_cb.value == True:
                hash_id = ""
                while m < int(hash_ws.value):
                    hash_id = hash_id + random.choice(arral)               
                    m += 1

                res = "[" + hash_id + "]" +res
                hash_id = ""
                m = 0
          
            page.result.value = res
            pshis += pstr+" → "+res +"\n"
            history.value = pshis
            res = ''
        page.update()  
    
    # 复制文本
    def copy_text(e):
        pyperclip.copy(page.result.value)
        page.snack_bar = ft.SnackBar(ft.Text(f"已复制"))
        page.snack_bar.open = True
        page.update()
    
    # 清除历史记录
    def clear_his(e):
        pshis = ""
        history.value = "无记录"
        page.snack_bar = ft.SnackBar(ft.Text(f"已清空"))
        page.snack_bar.open = True
        page.update()
    
    # Hash ID 检测
    def hash_check(e):
        if hash_cb.value == True:
            hash_ws.disabled = False
        else:
            hash_ws.disabled = True
        page.update()

    # Hash ID 位数检测
    def ws_check(e):
        ws=hash_ws.value
        if str(ws).isdigit() == False:
            hash_ws.value = 5  
        elif int(ws)<3:
            hash_ws.value=3
        elif int(ws)>10:
            hash_ws.value=10 
        page.update()

    # 元音重复次数检测
    def vcs_check(e):
        vcs=vowel_cs.value
        if str(vcs).isdigit() == False:
            vowel_cs.value = 0
        elif int(vcs)<0:
            vowel_cs.value=0
        elif int(vcs)>10:
            vowel_cs.value=10 
        page.update()

    # 明暗切换
    def theme_changed(e):
        if theme.value == "0":
            page.theme_mode = (
            ft.ThemeMode.LIGHT
            )
        if theme.value == "1":
            page.theme_mode = (
            ft.ThemeMode.DARK
            )
        if theme.value == "2":
            page.theme_mode = (
            ft.ThemeMode.SYSTEM
            )
        page.update()

    #配色方案修改
    def sch_changed(e):
        sch=int(scheme.value)
        if sch == 0:
            page.theme=ft.Theme(font_family="Microsoft Yahei",
                            color_scheme_seed=ft.colors.BLUE)
        if sch == 1:
            page.theme=ft.Theme(font_family="Microsoft Yahei",
                            color_scheme_seed=ft.colors.PINK)
        if sch == 2:
            page.theme=ft.Theme(font_family="Microsoft Yahei",
                            color_scheme_seed=ft.colors.GREEN)
        if sch == 3:
            page.theme=ft.Theme(font_family="Microsoft Yahei",
                            color_scheme_seed=ft.colors.BROWN)
        if sch == 4:
            page.theme=ft.Theme(font_family="Microsoft Yahei",
                            color_scheme_seed=ft.colors.DEEP_PURPLE_100)
        page.update()
    
    # 打开网页版
    def open_with_browser(e):
        webbrowser.open_new("https://suntrise.github.io/pseudo/")

    # 打开项目仓库
    def open_project_repo(e):
        webbrowser.open_new("https://github.com/suntrise/Pseudo-localization-Demo")

    # 打开“什么是伪本地化”窗口
    def open_what(e):
        page.dialog = what_dlg
        what_dlg.open = True
        page.update()  
    
    # 关闭“什么是伪本地化”窗口
    def close_what(e):
        what_dlg.open = False
        page.update()

    # 打开“更新日志”窗口
    def open_upd(e):
        page.dialog = upd_dlg
        upd_dlg.open = True
        page.update()  
    
    # 关闭“更新日志”窗口
    def close_upd(e):
        upd_dlg.open = False
        page.update()

    # 检查更新
    def check_for_update(e):
        def close_find_upd_dlg(e):
            find_upd_dlg.open = False
            page.update()
        api = "https://api.github.com/repos/suntrise/Pseudo-localization-Demo/releases" 
        all_info = requests.get(api, verify = False).json()
        custom_ver = all_info[0]['name']
        if custom_ver == ver:
            page.snack_bar = ft.SnackBar(ft.Text(f"你正在使用最新版本"))
            page.snack_bar.open = True
            page.update()
        else:
            assets = all_info[0]['assets']
            download_url = assets[0]['browser_download_url']
            detail = all_info[0]['body']
            publish_date_utc = all_info[0]['published_at']
            upd_content = "当前版本: " + ver + "\n \r新版本: " + custom_ver + "\n \r## 详细信息\n \r" + detail + "\n \r## 发布日期\n \r" + publish_date_utc
            find_upd_dlg = ft.AlertDialog(
                title = ft.Text("发现更新"), on_dismiss=lambda e: print("Dialog dismissed!"),
                content = ft.Markdown(upd_content, selectable=True),
                actions = [
                    ft.FilledButton("更新", icon = ft.icons.UPGRADE, url = download_url),
                    ft.TextButton("取消", icon = ft.icons.CANCEL_OUTLINED, on_click = close_find_upd_dlg)
                ],
            )
            page.dialog = find_upd_dlg
            find_upd_dlg.open = True
            page.update()  

    # “什么是伪本地化”窗口定义
    what_dlg = ft.AlertDialog(
        title = ft.Text("什么是伪本地化?"), on_dismiss=lambda e: print("Dialog dismissed!"),
        content = ft.Text(what_text,selectable = True),
        actions=[
            ft.TextButton("我知道啦", icon = ft.icons.DONE, on_click = close_what)      
        ],
        actions_alignment = ft.MainAxisAlignment.END
    ) 
    
    # “更新日志”窗口定义
    upd_dlg = ft.AlertDialog(
        title = ft.Text("更新日志"), on_dismiss=lambda e: print("Dialog dismissed!"),
        content = ft.Markdown(updmd,selectable=True),
        actions = [
            ft.TextButton("确定",on_click=close_upd)
        ],
        actions_alignment = ft.MainAxisAlignment.END,
        shape = ft.RoundedRectangleBorder(radius=20)
    ) 
         
    # 用户界面
    page.title = title
    page.window_left = 200
    page.window_top = 100
    page.window_height = 600
    page.window_width = 800  
    page.window_min_height = 400
    page.window_min_width = 760
    page.theme = ft.Theme(
         font_family="Microsoft Yahei",
         color_scheme_seed=ft.colors.BLUE
         )
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.appbar = ft.AppBar(
        leading_width = 30,
        title = ft.Text(title),
        center_title = False,
        bgcolor = ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.OPEN_IN_BROWSER),
                            ft.Text("网页版"),
                        ]),
                       on_click = open_with_browser
                    ),
                    ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.COLLECTIONS_BOOKMARK_OUTLINED),
                            ft.Text("项目仓库"),
                        ]),
                       on_click = open_project_repo     
                    ),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.QUESTION_MARK_OUTLINED),
                            ft.Text("什么是伪本地化?"),
                        ]),
                       on_click = open_what
                ),
                ]
            ),
        ],
    ) 
    
    # 主界面区
    xab_text = ft.Text("伪本地化方式:",size=20)
    xab = ft.RadioGroup(value = "enxa", #默认为“en-XA”
    content=ft.Row([
    ft.Radio(value="enxa", label="en-XA (abc→ǻƀĉ)"),
    ft.Radio(value="enxb", label="en-XB (abc→cba)")]))
    XABrow = ft.Row(spacing = 10, controls = [xab_text,xab])
    page.pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size =15, multiline = True, max_lines = 5)
    page.result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 15, multiline = True, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledButton(
        "进行伪本地化!",
        icon = ft.icons.TRANSLATE_OUTLINED,
        tooltip = "将您所填写的内容伪本地化, 每次生成结果都会不一样哦",
        on_click = pslo     
        )
    
    copy_btn = ft.FilledTonalButton(
        "复制",
        icon = ft.icons.COPY,
        tooltip = "将生成内容添加到设备剪切板",
        on_click = copy_text     
        )
    
    what_btn = ft.TextButton(
        "什么是伪本地化", 
        icon = ft.icons.QUESTION_MARK_OUTLINED,
        on_click = open_what
        )    
    row_pslo = ft.Row(spacing = 10, controls = [pslo_btn, copy_btn,what_btn])
    
    # 设置区
    opt_pslo = ft.Row(
            [
                ft.Icon(name=ft.icons.TRANSLATE_OUTLINED),
                ft.Text("伪本地化", size = 22)
            ]
        )
    opt_pslo_detail = ft.Text("(部分选项仅适用于 en-XA)", size=15) 
    suf_way = ft.Dropdown(
            label = "前后缀",
            hint_text = "选择前后缀方案，默认为“不添加前后缀”",
            value = 0, #默认为“不添加前后缀”
            options=[
                ft.dropdown.Option(key = 0, text = "不添加前后缀"),
                ft.dropdown.Option(key = 1, text = "[中括号+感叹号括起来 (微软式伪本地化)!!!]"),
                ft.dropdown.Option(key = 2, text = "[中括号+在语段后添加英文基数词（安卓式伪本地化） one two three]")
           ])  
    hash_cb = ft.Switch(label = "[Abc12]添加伪 Hash ID (资源标识符)(由一定位数的字母+数字所构成的字符串)", value=False,on_change=hash_check)
    hash_ws = ft.TextField(width=150,label="位数（3-10）",value=5,on_blur=ws_check,disabled=True) 
    row_hash = ft.Row(spacing = 10, controls = [hash_cb,hash_ws])
    vowel_tx = ft.Text("重复元音次数（0代表不重复，1代表双写，以此类推）：",size=15)
    vowel_cs = ft.TextField(width=150,label="次数（0-10）",value=0,on_blur=vcs_check) 
    row_vow = ft.Row(spacing = 10, controls = [vowel_tx,vowel_cs])
    num_pslo = ft.Dropdown(
            label = "数字伪本地化",           
            hint_text = "选择数字伪本地化方案，默认为“无”",
            value = 0, #默认为“无”
            options=[
                ft.dropdown.Option(key = 0, text = "无"),
                ft.dropdown.Option(key = 1, text = "使用①-⑨替代1-9"),
                ft.dropdown.Option(key = 2, text = "使用₀-₉或⁰-⁹交叉替换0-9")
            ]) 

    opt_look = ft.Row(
            [
                ft.Icon(name = ft.icons.PALETTE_OUTLINED),
                ft.Text("外观", size = 22)
            ]
        )
    theme = ft.Dropdown(
            label = "亮暗模式",
            hint_text = "亮暗模式",
            value = 2, #默认为“跟随系统”
            options=[
                ft.dropdown.Option(key = 0, text = "亮色"),
                ft.dropdown.Option(key = 1, text = "暗色"),
                ft.dropdown.Option(key = 2, text = "跟随系统")
            ],
            on_change = theme_changed) 
    sch_text = ft.Text("配色", size = 20)
    scheme = ft.RadioGroup(value = 0,content=ft.Row([
        ft.Radio(
        value = 0,
        label = "蓝色（默认）",
        fill_color=ft.colors.BLUE_800,
        ),
        ft.Radio(
        value = 1,
        label = "粉色",
        fill_color=ft.colors.PINK_700,
        ),
        ft.Radio(
        value = 2,
        label = "绿色",
        fill_color=ft.colors.GREEN_700,
        ),
        ft.Radio(
        value = 3,
        label = "巧克力色",
        fill_color=ft.colors.BROWN,
        ),
        ft.Radio(
        value = 4,
        label = "紫色",
        fill_color=ft.colors.DEEP_PURPLE,
        ),])
        ,on_change=sch_changed)
    abt = ft.Row(
            [
                ft.Icon(name = ft.icons.INFO_OUTLINE),
                ft.Text("关于", size = 22)
            ]
        )    
    about = ft.Text(about_text,size=15,selectable=True)

    upd_bar = ft.Row(
        controls=[
            ft.TextButton("项目仓库", icon = ft.icons.WAREHOUSE, url = "https://github.com/suntrise/Pseudo-localization-Demo"),
            ft.TextButton("网页版", icon = ft.icons.OPEN_IN_BROWSER, url = "https://suntrise.github.io/pseudo/"),
            ft.TextButton("更新日志", icon = ft.icons.UPDATE, on_click = open_upd),
            ft.TextButton("检查更新", icon = ft.icons.UPGRADE_OUTLINED, on_click = check_for_update)
        ]
    )

    # 历史记录
    history = ft.Text("无记录",size = 18, selectable = True)
    his_clear = ft.Row(alignment = ft.MainAxisAlignment.END, controls=[
        ft.TextButton("清空",
        icon = ft.icons.DELETE_FOREVER_OUTLINED,
        on_click = clear_his)
    ])

    # 标签
    tab = ft.Tabs(
        selected_index = 0,
        animation_duration = 200,
        indicator_tab_size=True,
        tabs=[
            ft.Tab(
                text = "主界面",
                icon = ft.icons.HOME_OUTLINED,
                content=ft.Container(
                    ft.Column(spacing = 5,scroll = ft.ScrollMode.ALWAYS, controls = [edge, XABrow, page.pstype, page.result, row_pslo])
                ),
            ),
            ft.Tab(
                text = "历史记录",
                icon = ft.icons.HISTORY_OUTLINED,
                content = ft.Column(spacing = 10,scroll = ft.ScrollMode.ALWAYS, controls = [edge, his_clear,history]),
            ),
            ft.Tab(
                text="设置",
                icon=ft.icons.SETTINGS_OUTLINED,
                content=ft.Column(spacing = 10,scroll = ft.ScrollMode.ALWAYS, controls = [edge, opt_pslo, opt_pslo_detail, suf_way, row_hash, num_pslo,row_vow, divider, opt_look, theme, sch_text, scheme, divider, abt, about, upd_bar]), 
            ),
        ]
    )
    page.add(tab)
    page.update()

ft.app(target=main)
