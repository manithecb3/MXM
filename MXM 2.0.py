import time
import os
wa_mx = input('app:         ')
print('-------------------')
if wa_mx == 'cal':
    wop = input('operation:')
    a = int(input('number 1:    '))
    b = int(input('number 2:    '))
    print('-------------------')
    if wop == 'sum':
        c = a + b
        print(f'{a} + {b} = {c} ')
        time.sleep(10)
    elif wop == 'min':
        c = a - b
        print(f'{a} - {b} = {c} ')
        time.sleep(10)
    elif wop == 'mul':
        c = a * b
        print(f'{a} * {b} = {c} ')
        time.sleep(10)
    elif wop == 'div':
        c = a / b
        print(f'{a} / {b} = {c} ')
        time.sleep(10)
if wa_mx == 'avg':
    avg = int(input('how much numbers?      '))
    print('-------------------')
    if avg == 2:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        print('-------------------')
        print((av + bv) / avg)
        time.sleep(10)
    if avg == 3:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        print('-------------------')
        print((av + bv + cv) / avg)
        time.sleep(10)
    if avg == 4:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        print('-------------------')
        print((av + bv + cv + dv) / avg)
        time.sleep(10)
    if avg == 5:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        print('-------------------')
        print((av + bv + cv + dv + ev) / avg)
        time.sleep(10)
    if avg == 6:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        fv = int(input('number 6:        '))
        print('-------------------')
        print((av + bv + cv + dv + ev + fv) / avg)
        time.sleep(10)
    if avg == 7:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        fv = int(input('number 6:        '))
        gv = int(input('number 7:        '))
        print('-------------------')
        print((av + bv + cv + dv + ev + fv + gv) / avg)
        time.sleep(10)
    if avg == 8:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        fv = int(input('number 6:        '))
        gv = int(input('number 7:        '))
        hv = int(input('number 8:        '))
        print('-------------------')
        print((av + bv + cv + dv + ev + fv + gv + hv) / avg)
        time.sleep(10)
    if avg == 9:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        fv = int(input('number 6:        '))
        gv = int(input('number 7:        '))
        hv = int(input('number 8:        '))
        iv = int(input('number 9:        '))
        print('-------------------')
        print((av + bv + cv + dv + ev + fv + gv + hv + iv) / avg)
        time.sleep(10)
    if avg == 10:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        fv = int(input('number 6:        '))
        gv = int(input('number 7:        '))
        hv = int(input('number 8:        '))
        iv = int(input('number 9:        '))
        jv = int(input('number 10:       '))
        print('-------------------')
        print((av + bv + cv + dv + ev + fv + gv + hv + iv + jv) / avg)
        time.sleep(10)
if wa_mx == 'oreware':
    print('loading ...')
    time.sleep(2)
    print('-------------------')
    owc = input('oreware command:       ')
    print('-------------------')
    if owc == 'oreware version':
        print('loading ...')
        time.sleep(0.5)
        print('-------------------')
        print('version 1.1')
        time.sleep(10)
    if owc == 'connect to developer':
        print('loading ...')
        time.sleep(0.5)
        print('-------------------')
        print('gmail: mani.karbasi.2013@gmail.com')
        time.sleep(1)
        print('outlook: mani.karbasi@outlook.com')
        time.sleep(10)
    if owc == 'file launcher':
        print('loading ...')
        time.sleep(0.5)
        print('-------------------')
        flu = input('what mxm based file?       ')
        if flu == 'blueberry rain':
            response = os.startfile(r"C:\Users\MANDEGAR\PycharmProjects\MXM project\cool stuff\bbmxm.pptx")
            print(response)
if wa_mx == 'vasemaker':
    import webbrowser
    import time

    print('loading...')
    print('-------------------')
    time.sleep(1)
    WL = input('what web site?      ')
    print('-------------------')
    print('loading...')
    print('-------------------')
    time.sleep(1)
    if WL == 'rickroll':
        webbrowser.open('youtube.com/watch/xvFZjo5PgG0')
        print('done!')
    else:
        webbrowser.open(WL)
        print('done!')
if wa_mx == 'ver':
    print('version = 1.2')
    time.sleep(10)
