## Írjunk ki adott számú (24db) csillagot - erre írjunk egy metódust

def jelek(jel:str="*",hanyszor:int=24):
    print(jel*hanyszor)

def nyugta_kiiras(szo:str="NYUGTA", hossz:int=24, jel:str="*"):
    #print(f"*        {szoveg}        *") masik megoldas
    szo = szo.upper()
    hossz= hossz-2
    #print(f"*{szo:^22}*")
    print(f"{jel}{szo:^{hossz}}{jel}")
    
def lec(szo:str="szoveg", hossz:int=24, jel:str="*"):
    jelek(jel,hossz)
    nyugta_kiiras(szo,hossz,jel)
    jelek(jel,hossz)

def tetel_kiir(tetel:str="tetel",ar:float=0,hossz:int=24):
    hossz= hossz-len(tetel)
    print(f"{tetel}{ar:>{hossz-3}} Ft")