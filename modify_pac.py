# -*- encoding: utf-8 -*-
'''
@File    :   modify_pac.py
@Time    :   2023/04/21 23:01:45
@Author  :   xoyojo 
@Version :   1.0
@Contact :   sduw.lj@gmail.com
@License :   
@Desc    :   None
'''

# here put the import lib

def modify_pac():
    with open('gfwlist_1080.pac', 'r') as f:
        content = f.read()

    content = content.replace(
        "var proxy = 'SOCKS5 127.0.0.1:1080';",
        '''var proxy1 = 'SOCKS5 127.0.0.1:40000';
var proxy2 = 'SOCKS5 127.0.0.1:1080';'''
    )
    content = content.replace(
        '''[],
        []''', 
        '''[],
        [
            "openai.com",
            "bing.com",
            "discord.com",
            "discord.gg",
            "discordapp.com",
        ]'''
    )     

    content = content.replace(
        "return i % 2 == 0 ? 'DIRECT' : proxy;", 
        '''if (index == 0)
                    return i % 2 == 0 ? 'DIRECT' : proxy1;
                else
                    return i % 2 == 0 ? 'DIRECT' : proxy2;''')

                

    with open('gfwlist_auto.pac', 'w') as f:
        f.write(content)


if __name__ == '__main__':
    modify_pac()