import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config
import time

class Calculator(BoxLayout):
    """The widget that contains a screen and a button pad.  Initializes with entry_state and current_operation
        fields.  entry_state ("accepting_first_operand", "accepting_second_operand", or "result") determines how input
        is treated.

        accepting_first_operand: Digits entered are concatenated to those onscreen. Screen is cleared and entry_state
        switches to "accepting_second_operand" when operation button is pressed. Operation is stored in
        current_operation field (possible values: "+", "-", "x", and "/").

        accepting_second_operand: When a digit is entered, screen is cleared. Subsequent digits entered are
        concatenated to those onscreen. If the "=" button is pressed: two operands are performed upon, screen
        is cleared, result is displayed onscreen, and entry_state changes to "result".

        result: If a digit button is pressed: screen clears, entry_state changes to "accepting_first_operand", and
        digit is added to screen. If an operation button is pressed: operation is stored in current_operation,
        entry_state is changed to "accepting_second_operand", and the displayed result is treated as the first of two
        operands. """

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.entry_state = 'accepting_first_operand'
        self.current_operation = ''
        self.first_operand = 0
        self.second_operand = 0

    def clear_operands_and_operation(self):
        self.set_first_operand("")
        self.set_second_operand("")
        self.set_current_operation("")

    def get_entry_state(self):
        return self.entry_state

    def set_entry_state(self, new_entry_state):
        self.entry_state = new_entry_state

    def get_current_operation(self):
        return self.current_operation

    def set_current_operation(self, new_current_operation):
        self.current_operation = new_current_operation

    def get_first_operand(self):
        return self.first_operand

    def set_first_operand(self, new_first_operand):
        self.first_operand = new_first_operand

    def get_second_operand(self):
        return self.second_operand

    def set_second_operand(self, new_second_operand):
        self.second_operand = new_second_operand



    def get_screen_text(self):
        return self.ids["screen"].text

    def number_decimal_points_on_screen(self):
        return self.get_screen_text().count(".")

    def find_decimal_point_on_screen(self):
        return self.get_screen_text().find(".")

    def has_number_on_screen(self):
        screen_text = self.ids['screen'].text
        found_decimal = self.find_decimal_point_on_screen()
        return screen_text.isdigit() or (screen_text[1:].isdigit() and screen_text[0] == '-') or \
                  (self.number_decimal_points_on_screen() == 1 and ((screen_text[0] == '-' and \
                    (screen_text[1:found_decimal] + screen_text[found_decimal + 1:]).isdigit()) \
                        or (screen_text[0:found_decimal] + screen_text[found_decimal+1:]).isdigit()))


    def set_screen_text(self, new_text):
        self.ids['screen'].text = new_text

    def clear_screen_text(self):
        self.ids['screen'].text = ''


    def add_to_screen(self, to_be_added):
        current_screen_text = self.get_screen_text()
        self.set_screen_text(current_screen_text + to_be_added)

    def switch_displayed_number_parity(self):
        if self.has_number_on_screen():
            self.set_screen_text('%g'%(float(self.get_screen_text()) * -1))

    def operate_on_operands(self, first_operand, second_operand, operation):
        if operation == "+":
            return '%g'%(float(first_operand) + float(second_operand))
        if operation == "-":
            return '%g'%(float(first_operand) - float(second_operand))
        if operation == "x":
            return '%g'%(float(first_operand) * float(second_operand))
        if operation == "/":
            return '%g'%(float(first_operand) / float(second_operand))


    def enter_button(self, button_entry):
        if len(button_entry) == 1:
            if button_entry.isdigit():
                if self.get_entry_state() == "accepting_first_operand" or self.get_entry_state() == \
                        "accepting_second_operand":
                    self.add_to_screen(button_entry)

                elif self.get_entry_state() == "result":
                    self.clear_screen_text()
                    self.set_entry_state("accepting_first_operand")
                    self.add_to_screen(button_entry)

            elif button_entry in "+-x/":
                if self.get_entry_state() == "accepting_first_operand":
                    self.set_first_operand(self.get_screen_text())
                    self.clear_screen_text()
                    self.set_current_operation(button_entry)
                    self.set_entry_state("accepting_second_operand")

                if self.get_entry_state() == "result":
                    self.set_first_operand(self.get_screen_text())
                    self.set_current_operation(button_entry)
                    self.clear_screen_text()
                    self.set_entry_state("accepting_second_operand")

            elif button_entry == "=":
                if self.get_entry_state() == "accepting_second_operand":
                    if self.has_number_on_screen():
                        self.set_second_operand(self.get_screen_text())
                        result = self.operate_on_operands(self.get_first_operand(), self.get_second_operand(), \
                            self.get_current_operation())
                        self.clear_operands_and_operation()
                        self.set_screen_text(str(result))
                        self.set_entry_state("result")

            elif button_entry == ".":
                if self.get_entry_state() == "accepting_first_operand" or self.get_entry_state() == \
                    "accepting_second_operand":
#<<<<<<< HEAD:calculator.py

                    if self.has_number_on_screen() and self.number_decimal_points_on_screen() < 1:


#=======
                    if self.has_number_on_screen() and self.number_decimal_points_on_screen() < 1:
#>>>>>>> main-py-file-rename:main.py
                        self.add_to_screen(".")
                    elif self.get_screen_text() == "":
                        self.add_to_screen("0.")
                elif self.get_entry_state() == "result":
                    self.clear_screen_text()
                    self.clear_operands_and_operation()
                    self.set_entry_state("accepting_first_operand")
                    self.add_to_screen("0.")



            elif button_entry == 'C':
                #############
                #self.set_screen_text(str(self.has_number_on_screen()))
                #time.sleep(3)
                self.clear_screen_text()
                self.set_entry_state("accepting_first_operand")
                self.clear_operands_and_operation()

        elif len(button_entry) == 3:
            if button_entry == '+/-':
                if self.get_entry_state() == "result":
                    self.clear_screen_text()
                    self.clear_operands_and_operation()
                    self.set_entry_state("accepting_first_operand")
                else:
                    self.switch_displayed_number_parity()


class CalculatorApp(App):
    """The main app."""
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()

