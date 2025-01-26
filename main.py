from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout

class CalculatorApp(MDApp):
    def build(self):

        res_layout = MDBoxLayout(orientation='horizontal', padding=10)
        self.result = MDTextField(multiline=False, font_size=40, halign='right', size_hint_x=0.8)
        res_layout.add_widget(self.result)
        res_layout.size_hint_y = 0.2

        button_layout = MDGridLayout(cols=4, padding=10)

        numbers = ['7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']

        for number in numbers:
            button = Button(
                text=number, 
                font_size=30
                )
            button.bind(on_press=self.on_button_click)
            button_layout.add_widget(button)

        main_layout = MDBoxLayout(orientation='vertical')
        main_layout.add_widget(res_layout)
        main_layout.add_widget(button_layout)

        return main_layout

    def on_button_click(self, instance):
        number = instance.text
        if number == '=':
            try:
                result = eval(self.result.text)
                self.result.text = str(result)
            except Exception:
                self.result.text = 'Error'
        else:
            self.result.text += number

if __name__ == '__main__':
    CalculatorApp().run()
