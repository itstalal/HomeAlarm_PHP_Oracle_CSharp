from gpiozero import LED
from time import sleep
 
class SevenSeg:
 
    def __init__(self, psa:int, psb:int, psc:int, psd:int, pse:int, psf:int, psg:int, pd:int, AC_CC:bool):
        self.__sa = LED(psa)
        self.__sb = LED(psb)
        self.__sc = LED(psc)
        self.__sd = LED(psd)
        self.__se = LED(pse)
        self.__sf = LED(psf)
        self.__sg = LED(psg)
        self.__pd = LED(pd)
        self.__AC_CC = AC_CC
 
    def show0(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()
 
    def show1(self):
        if self.__AC_CC:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
 
    def show2(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.on()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.off()
 
    def show3(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
 
    def show4(self):
        if self.__AC_CC:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()
 
    def show5(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.off()
            self.__sc.on()
            self.__sd.on()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.off()
            self.__sd.off()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()
 
    def show6(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.off()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
 
    def show7(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
 
    def show8(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
 
    def show9(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()
 
    def showA(self):
        if self.__AC_CC:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
    
    def showH(self):
        if self.__AC_CC:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.off() 
            
            
    def showL(self):
        if self.__AC_CC:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
        else:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()                    
   
 
 
    def cout_up(self):
        self.show0()
        sleep(1)
        self.show1()
        sleep(1)
        self.show2()
        sleep(1)
        self.show3()
        sleep(1)
        self.show4()
        sleep(1)
        self.show5()
        sleep(1)
        self.show6()
        sleep(1)
        self.show7()
        sleep(1)
        self.show8()
        sleep(1)
        self.show9()
        sleep(1)
        self.showA()
 
 
 
    def cout_down(self):
        self.show9()
        sleep(1)
        self.show8()
        sleep(1)
        self.show7()
        sleep(1)
        self.show6()
        sleep(1)
        self.show5()
        sleep(1)
        self.show4()
        sleep(1)
        self.show3()
        sleep(1)
        self.show2()
        sleep(1)
        self.show1()
        sleep(1)
        self.show0()
        sleep(1)
 
 
    def Flash0(self):
        self.__sa.blink()
        self.__sb.blink()
        self.__sc.blink()
        self.__sd.blink()
        self.__se.blink()
        self.__sf.blink()
        self.__sg.blink()
 
    def Flash1(self):
        self.__sb.blink()
        self.__sc.blink()
 
    def Flash2(self):
        self.__sa.blink()
        self.__sb.blink()
        self.__sd.blink()
        self.__se.blink()
        self.__sg.blink()
 
    def Flash3(self):
        self.__sa.blink()
        self.__sb.blink()
        self.__sc.blink()
        self.__sd.blink()
        self.__sg.blink()
 
    def Flash4(self):
        self.__sb.blink()
        self.__sc.blink()
        self.__sf.blink()
        self.__sg.blink()
 
    def Flash5(self):
        self.__sa.blink()
        self.__sc.blink()
        self.__sd.blink()
        self.__sf.blink()
        self.__sg.blink()
 
    def Flash6(self):
        self.__sa.blink()
        self.__sc.blink()
        self.__sd.blink()
        self.__se.blink()
        self.__sf.blink()
        self.__sg.blink()
 
    def Flash7(self):
        self.__sa.blink()
        self.__sb.blink()
        self.__sc.blink()
 
    def Flash8(self):
        self.__sa.blink()
        self.__sb.blink()
        self.__sc.blink()
        self.__sd.blink()
        self.__se.blink()
        self.__sf.blink()
        self.__sg.blink()
 
    def Flash9(self):
        self.__sa.blink()
        self.__sb.blink()
        self.__sc.blink()
        self.__sf.blink()
        self.__sg.blink()
       
