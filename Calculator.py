try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button
    from kivy.uix.textinput import TextInput
    import math
except ModuleNotFoundError:
    print("Error: Kivy module not found. Please install it using 'pip install kivy'.")
    exit()

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/', '^']
        self.last_was_operator = False
        self.last_button = None
        
        layout = BoxLayout(orientation='vertical')
        
        self.display = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout.add_widget(self.display)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+'],
            ['sin', 'cos', 'tan', 'log']
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        
        return layout
    
    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.display.text = ""
        elif text == "=":
            try:
                expression = self.display.text.replace('^', '**')
                self.display.text = str(eval(expression))
            except:
                self.display.text = "Error"
        elif text in ['sin', 'cos', 'tan', 'log']:
            try:
                expression = f"math.{text}({self.display.text})"
                self.display.text = str(eval(expression))
            except:
                self.display.text = "Error"
        else:
            self.display.text += text

if __name__ == '__main__':
    CalculatorApp().run()
