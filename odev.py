from math import sin 
import math
def hesaplama(tç,hmax,xm):
    if(kütle==250):
      Vo=6
    else:
      if(kütle==400 or kütle==650):
        Vo=8
    tç=(Vo*sin(açı))/10
    hmax=(Vo*sin(açı)*20)
    hmax=(Vo*sin(açı)*Vo*sin(açı))/20
    xm=(Vo*sin(açı)*20)
    xm=(Vo*Vo*sin(2*açı))/20    
açı=float(input('lütfen yerle yaptığı açıyı yazınız.'))
açı=sin(math.radians(açı))
kütle=float(input('lütfen kütle bilgisini giriniz.'))

print('tç=',tç) 
print('hmax=',hmax)
print('xm=',xm)