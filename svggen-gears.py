#!/usr/bin/python

import math

def genGear(x, y, n, r1, r2, rr1, rr2, angoff=0 ):
    dang = 2 * math.pi / n
    ddang1 = dang * 0.3
    ddang2 = dang * 0.55

    s = f'M { x + math.cos(ddang1+angoff)*r1 } { y + math.sin(ddang1+angoff)*r1 }'
    for i in range(0, n):
        ang1 = i * dang + ddang1 + angoff
        ang2 = i * dang + ddang2 + angoff
        ang3 = ang1 + dang - ddang2
        ang4 = ang1 + dang - ddang1

        if i != 0:
            # s += f' L { r + math.cos(ang1)*r1 } { r + math.sin(ang1)*r1 }'
            s += f' A { rr1 } { rr1 } 0 0 1 { x + math.cos(ang1)*r1 } { y + math.sin(ang1)*r1 }'
        s += f' L { x + math.cos(ang2)*r2 } { y + math.sin(ang2)*r2 }'

        # s += f' L { x + math.cos(ang3)*r2 } { y + math.sin(ang3)*r2 }'
        s += f' A { rr2 } { rr2 } 0 0 0 { x + math.cos(ang3)*r2 } { y + math.sin(ang3)*r2 }'
        s += f' L { x + math.cos(ang4)*r1 } { y + math.sin(ang4)*r1 }'

    s += f' A { rr1 } { rr1 } 0 0 1 { x + math.cos(ddang1+angoff)*r1 } { y + math.sin(ddang1+angoff)*r1 }'
    print(f' <path d="{s}"/>')
    print(f' <circle cx="{ x }" cy="{ y }" r="{ r2 - 20 }"/>')


print(f'<svg width="{ 500 }" height="{ 400 }" xmlns="http://www.w3.org/2000/svg">')
print('<link xmlns="http://www.w3.org/1999/xhtml" rel="stylesheet" href="style.css" type="text/css" />')

genGear(x=130, y=170, n=12, r1=120, r2=90, rr1=20, rr2=10, angoff=0 )
genGear(x=325, y=210, n=9, r1=100, r2=70, rr1=15, rr2=10, angoff=15/180*math.pi )
genGear(x=380, y=75, n=6, r1=60, r2=38, rr1=15, rr2=10, angoff=0 )


print('</svg>')
