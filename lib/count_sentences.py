import re
class MyString:
    def __init__(self, value = ""):
        self._value = value

    def value(self):
        return self._value

    def set_value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    value = property(value, set_value)

    def is_sentence(self):
        if self._value.__contains__('.'):
            return True
        else:
            return False
      
    def is_question(self):
        if self._value.__contains__('?'):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value.__contains__('!'):
            return True
        else:
            return False
        
    def count_sentences(self):
        if self.value == '':
            return 0
            
        return len(re.split(r'[!\?\.](?= )', self.value))
