wa_mx = input('app:         ')
if wa_mx == 'cal':
    wop = input('operation:')
    a = int(input('number 1:    '))
    b = int(input('number 2:    '))
    print('-------------------')

    if wop == 'sum':
        c = a + b
        print(f'{a} + {b} = {c} ')
    elif wop == 'min':
        c = a - b
        print(f'{a} - {b} = {c} ')
    elif wop == 'mul':
        c = a * b
        print(f'{a} * {b} = {c} ')
    elif wop == 'div':
        c = a / b
        print(f'{a} / {b} = {c} ')
if wa_mx == 'avg':
    avg = int(input('how much numbers?      '))
    if avg == 2:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        print((av + bv) / avg)
    if avg == 3:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        print((av + bv + cv) / avg)
    if avg == 4:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        print((av + bv + cv + dv) / avg)
    if avg == 5:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        print((av + bv + cv + dv + ev) / avg)
    if avg == 6:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        fv = int(input('number 6:        '))
        print((av + bv + cv + dv + ev + fv) / avg)
    if avg == 7:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        fv = int(input('number 6:        '))
        gv = int(input('number 7:        '))
        print((av + bv + cv + dv + ev + fv + gv) / avg)
    if avg == 8:
        av = int(input('number 1:        '))
        bv = int(input('number 2:        '))
        cv = int(input('number 3:        '))
        dv = int(input('number 4:        '))
        ev = int(input('number 5:        '))
        fv = int(input('number 6:        '))
        gv = int(input('number 7:        '))
        hv = int(input('number 8:        '))
        print((av + bv + cv + dv + ev + fv + gv + hv) / avg)
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
        print((av + bv + cv + dv + ev + fv + gv + hv + iv) / avg)
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
        print((av + bv + cv + dv + ev + fv + gv + hv + iv + jv) / avg)
if wa_mx == 'ver':
    print('version = 1.12')
