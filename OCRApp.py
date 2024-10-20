#!/usr/bin/env python
# coding: utf-8
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup        
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Line,RoundedRectangle,Color
from OCR_API import OCR_API
from OCR_TES import OCR_TES
from OCR3 import OCR3

class StrokeButton(Button):
    def press(self):
        self.c=Color(0,0,0,1)
        self.r=RoundedRectangle(radius=[18],size=self.size,pos=self.pos)
        self.canvas.add(self.c)
        self.canvas.add(self.r)
      #  self.canvas.add(Label(text='hel'))   

    def release(self,state):
        if state=='normal':
        	self.color=(0,0,0,1)
        else:
        	self.color=(1,1,1,1)


class SavePopup(Popup):

    def close(self,*instance):
        try:
        	filename = "single" if self.ids.txtbx.text=="" else self.ids.txtbx.text.replace(" ","_")
        	inf = open('{}.txt'.format(filename),'w', encoding='utf8') 
        	inf.write(app.next_page.ids.output.text)
        	inf.close()
        except Exception as e:
           pop = SecPopup(title='Save')
           pop.input_text='[color=000000]Text is not Clear to save\n{}[/color]'.format(e)
           pop.open()
        self.dismiss()


class SecPopup(Popup):
    pass

class MyPopup(Popup):
    def selected(self, instance):
        try:
            app.start_page.ids.txtbx.text=instance[0]
            app.start_page.ids.img.source=instance[0]
        except:pass


class StartPage(FloatLayout):
    
    def pressed_button(self, instance):
        if self.ids.img.source!='':
            app.screen_manager.current='next'
            if instance.text=='Online': 
                a=OCR_API() 
            else:
                a=OCR_TES()
            #a=OCR3() 
            app.text=a.result(self.ids.img.source,instance.text)
            app.next_page.ids.output.text=app.text
        else:
            content = BoxLayout(orientation='vertical', spacing=5) 
            background_color= (77/255,176/255,147/255, 0)
            self.popup = SecPopup()
            self.popup.open()          
        
    def browse_button(self, instance):
        MyPopup().open()
        
    def selected(self, instance):
        self.ids.img.source=instance[0]


class NextPage(FloatLayout):


    def pressed_button(self, instance):
        app.screen_manager.current='start' 

    def selected1(self,instance):
        self.popup = SavePopup(title='Save')
        self.popup.open()


class OCR(App):
    Window.clearcolor = (77/255,176/255,147/255, 0)

    def build(self):
        self.icon="Images/icon-2.png"
        Window.bind(on_dropfile=self._on_file_drop)
        self.text=""
        self.start_page = StartPage()
        self.screen_manager = ScreenManager()
        self.next_page = NextPage()
        screen1 = Screen(name='start')
        screen2 = Screen(name='next')
        screen1.add_widget(self.start_page)
        screen2.add_widget(self.next_page)
        self.screen_manager.add_widget(screen1)
        self.screen_manager.add_widget(screen2)
        return self.screen_manager

    def _on_file_drop(self, window, file_path):
    	file_path = str(file_path)[2:-1].replace('\\\\','\\')
    	self.start_page.ids.img.source = '%s'%file_path
    	self.start_page.ids.txtbx.text = '%s'%file_path

if __name__ == "__main__":
    app = OCR()
    app.run()