import re

for x in [x.strip() for x in input().split(',')]:
    f, s = '', ''
    if len(x) == 20:
        f = x[0:10]
        s = x[10:]
        pat = r'[@]{6,}|[$]{6,}|[#]{6,}|[\^]{6,}'
        f_check = re.findall(pat, f)
        s_check = re.findall(pat, s)

        if f_check and s_check:
            symbol = f_check[0][0]
            isSymbols = f_check[0][0] == s_check[0][0]

            if isSymbols:
                isJackpot = f_check[0].count(symbol) == 10 and s_check[0].count(symbol) == 10
                if isJackpot:
                    print(f'ticket "{x}" - 10{symbol} Jackpot!')
                else:
                    print(f'ticket "{x}" - {min(f_check[0].count(symbol), s_check[0].count(symbol))}{symbol}')
        else:
            print(f'ticket "{x}" - no match')
    else:
        print('invalid ticket')
