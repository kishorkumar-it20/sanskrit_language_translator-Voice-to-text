from kivy.core.text import LabelBase
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
# Window.fullscreen = "auto"
import speech_recognition as sr
import audio
import lib
from googletrans import Translator
import pyttsx3 as tts
import io
import tel_lib
import word_lib
import final_lib
tlu = "మామ రామ రామ"

translator = Translator()
# create the recognizer
r = sr.Recognizer()
class MainWindow(Screen):
    m = 0
    def release(self):

        SecondWindow.start(self)

class SecondWindow(Screen):
    global tlu
    #result = "Start"
    def start(self):
        global tlu

        r = sr.Recognizer()

        # define the microphone
        mic = sr.Microphone(device_index=0)

        print("Start speaking")

        # record your speech
        with mic as source:
            audio = r.listen(source)



        # speech recognition
        result = r.recognize_google(audio, language="te-IN")
        print(result)
        tlu = result
        a = result.encode("utf-8")
        # export the result
        # with io.open('Lang.txt', mode='w', encoding ="utf-8") as file:
        #     file.write(str(a))






class ThirdWindow(Screen):
    #a = SecondWindow.result


    global tlu
    # proper(self)
    def proper(self):
        global tlu
        # self.ids.field1.text = "Start to speak..."
        # f = io.open("Lang.txt", mode="r", encoding="utf-8")

        # a = f.readlines()
        # print(a)
        # # a = c.decode('utf-8')
        # for i in a:
        #     b = i
        print(tlu)




        self.ids.field1.text  = tlu

    LabelBase.register(name="TELU", fn_regular="NotoSerifTelugu-Bold.ttf")

    def translate(self):
        #self.ids.but.text = "Translated"
        #self.ids.wsd.text = "Translation sucessful!!"
        # f = open("Lang.txt", 'r')
        # c = f.readlines()
        #
        # for i in c:
        #     d = c[0]
        d = self.ids.field1.text
        print(d)
        rm = audio.lib(d)
        self.ids.field2.text = rm
    def back(self):
        self.ids.but.text = "Translate"
        self.ids.wsd.text = " "

    LabelBase.register(name="SANSKK", fn_regular="NotoSans-Bold.ttf")
    def eng_speak(self):
        tts.text_to_speech(self.ids.field1.text)

    def san_speak(self):
        self.abc = self.ids.field2.text
        sansglish = word_lib.words_change(self.abc)
        print(sansglish)
        tts.text_to_speech(sansglish)






class WindowManager(ScreenManager):
    pass


kv1 = Builder.load_file('Speech_to_text.kv')
class MyApp(App):
    def build(self):
        return kv1

if __name__ == "__main__":
    MyApp().run()