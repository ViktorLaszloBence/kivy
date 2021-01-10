from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView

TermekLista = []

class Termek:
    def __init__(self, nev, marka, mennyiseg):
        self.nev = nev
        self.marka = marka
        self.mennyiseg = mennyiseg

    def print(self): # Kiíratás debug szempontjából.
        return print("[ %s, %s, %s ]" % (self.nev, self.marka, self.mennyiseg))

class MainWindow(Screen):
    termek = ObjectProperty(None)
    marka = ObjectProperty(None)
    mennyiseg = ObjectProperty(None)

    def press_submit(self):
        # A Globális TermekLista változót használod, így kell megjelölni. Ennek köszönhetően nem kell minden osztálynak átadnod.
        # Olyan mint C#-ban a static. Nem a legjobb OOP-s megoldás, de jelenleg teljesen jó.
        global TermekLista
        TermekLista.append(Termek(self.termek.text,self.marka.text,self.mennyiseg.text))

        self.termek.text = ""
        self.marka.text = ""
        self.mennyiseg.text = ""

        # TermekLista hosszának és elemeinek kiíratása.
        print("TermekLista length: %d" % len(TermekLista))
        for t in TermekLista:
            t.print()

class SecondWindow(Screen):
    global TermekLista # Szintén a globális tömböt használd. Ez után nem tudom mit szeretnél vagy hogyan xD
    def build(self):



class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class RV(RecycleView):
    global TermekLista
    def __init__(self):
        super().__init__()
        for termek in TermekLista:
            print("fing")
            self.data = self.termek.text

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()