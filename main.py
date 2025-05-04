from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex

class CalculatorApp(App):
    def build(self):
        # Main layout for the calculator (vertical box layout)
        self.main_layout = BoxLayout(orientation='vertical')

        # Text input for displaying the result and user input
        self.result_input = TextInput(
            multiline=False,
            readonly=True,
            font_size=40,
            halign='right',
            size_hint_y=None,
            height=80,
            background_color=get_color_from_hex("#333333"), # Dark background for better contrast
            foreground_color=(1, 1, 1, 1) # White text color
        )
        self.main_layout.add_widget(self.result_input)

        # Define the buttons for the calculator
        buttons = [
            {'text': 'C', 'on_press': self.clear_result, 'bg_color': "#FF6F00", 'text_color': "#FFFFFF"}, # Clear button (orange)
            {'text': '<-', 'on_press': self.backspace, 'bg_color': "#FF6F00", 'text_color': "#FFFFFF"}, # Backspace button (orange)
            {'text': '', 'disabled': True, 'on_press': lambda x: None}, # Empty disabled button for layout
            {'text': '/', 'on_press': self.on_button_click, 'bg_color': "#A0A0A0", 'text_color': "#FFFFFF"}, # Operator button
            {'text': '7', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '8', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '9', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '*', 'on_press': self.on_button_click, 'bg_color': "#A0A0A0", 'text_color': "#FFFFFF"}, # Operator button
            {'text': '4', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '5', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '6', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '-', 'on_press': self.on_button_click, 'bg_color': "#A0A0A0", 'text_color': "#FFFFFF"}, # Operator button
            {'text': '1', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '2', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '3', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Number button
            {'text': '+', 'on_press': self.on_button_click, 'bg_color': "#A0A0A0", 'text_color': "#FFFFFF"}, # Operator button
            {'text': '0', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF", 'colspan': 2}, # Zero button spans two columns
            {'text': '.', 'on_press': self.on_button_click, 'bg_color': "#777777", 'text_color': "#FFFFFF"}, # Decimal point button
            {'text': '=', 'on_press': self.evaluate, 'bg_color': "#008080", 'text_color': "#FFFFFF"}, # Equals button (teal)
        ]

        # Layout for the buttons (4 columns grid)
        button_layout = GridLayout(cols=4, spacing=5, padding=5)

        # Manually add buttons to handle the colspan for the '0' button
        index_zero = [i for i, info in enumerate(buttons) if info.get('text') == '0'][0]
        for i, button_info in enumerate(buttons):
            button = Button(text=button_info['text'], font_size=30)
            button.bind(on_press=button_info['on_press'])
            button.background_color = get_color_from_hex(button_info.get('bg_color', "#F0F0F0"))
            button.color = get_color_from_hex(button_info.get('text_color', "#000000"))
            if button_info.get('disabled'):
                button.disabled = True

            button_layout.add_widget(button)

            # Handle colspan for the '0' button by adding an empty widget
            if i == index_zero:
                button_layout.add_widget(BoxLayout()) # Add an empty layout to take up the extra space

        self.main_layout.add_widget(button_layout)
        return self.main_layout

    def on_button_click(self, instance):
        """Appends the text of the clicked button to the result input."""
        self.result_input.text += instance.text

    def clear_result(self, instance):
        """Clears the content of the result input."""
        self.result_input.text = ''

    def backspace(self, instance):
        """Removes the last character from the result input."""
        self.result_input.text = self.result_input.text[:-1]

    def evaluate(self, instance):
        """Evaluates the expression in the result input."""
        try:
            self.result_input.text = str(eval(self.result_input.text))
        except Exception:
            self.result_input.text = 'Error'

if __name__ == '__main__':
    CalculatorApp().run()