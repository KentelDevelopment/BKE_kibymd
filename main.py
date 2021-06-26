#Kentel Technologies
#Author : Efe Akaröz


from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen 
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextFieldRect,MDTextFieldRound
from kivymd.uix.label import MDLabel
from kivymd.toast import toast

class BKE(MDApp):
	def build(self):
		screen = Screen()
		self.theme_cls.primary_palette = "Purple"

		my_toolbar = MDToolbar(title="Beden Kitle İndeksi",pos_hint={'top':1})


		#Inputs:
		labelKG = MDLabel(text="Kütleniz(KG)",pos_hint={'center_x':0.8,'center_y':0.8})
		self.inputKG = MDTextFieldRect(size_hint_x=None,width=600,size_hint_y=None,height=50,pos_hint={'center_x':0.5,'center_y':0.75})

		labelCM = MDLabel(text="Boyunuz(CM)",pos_hint={'center_x':0.8,'center_y':0.6})
		self.inputCM = MDTextFieldRect(size_hint_x=None,width=600,pos_hint={'center_x':0.5,'center_y':0.55},size_hint_y=None,height=50)




		submitbtn = MDRaisedButton(text="Hesapla" , pos_hint={'center_x':0.5,'center_y':0.1},on_release=self.calculate)

		screen.add_widget(my_toolbar)
		screen.add_widget(submitbtn)
		screen.add_widget(labelKG)
		screen.add_widget(self.inputKG)
		screen.add_widget(labelCM)
		screen.add_widget(self.inputCM)
		return screen 

	def calculate(self,obj):
		kgofhuman = int(self.inputKG.text)
		cmofhuman = self.inputCM.text 
		mofhuman = int(cmofhuman)/100
		msquare = mofhuman*mofhuman

		result = kgofhuman/msquare
		print(result)
		if result <= 18.5:
			#Düşük kilo
			self.theme_cls.primary_palette="Red"
			toast("Düşük kilo")

		if result>18.5 and result<25:
			#Normal
			toast("Normal Kilo")
			self.theme_cls.primary_palette="Green"
		
		if result>=25 and result<30:
			#Fazla Kilolu
			toast("Fazla Kilolu")
			self.theme_cls.primary_palette="Yellow"
		
		if result>= 30 and result<40:
			#Obez
			toast("Obez")
			self.theme_cls.primary_palette="Orange"

		if result >= 40:
			#Aşırı obez
			toast("Aşırı Obez")
			self.theme_cls.primary_palette = "Red"
BKE().run()
