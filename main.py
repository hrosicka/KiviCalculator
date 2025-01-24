from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):

        res_layout = BoxLayout()

        self.result = TextInput(multiline=False, font_size=40, halign='right')
        res_layout.add_widget(self.result)
        res_layout.size_hint_y = 0.2

        button_layout = GridLayout(cols=4)


        numbers = ['7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']

        for number in numbers:
            button = Button(text=number, font_size=30, background_color=(0.8, 0.8, 0.8, 1))
            button.bind(on_press=self.on_button_click)
            button_layout.add_widget(button)

        main_layout = BoxLayout(orientation='vertical')
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
