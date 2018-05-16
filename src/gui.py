import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class Gui(BaseWidget):

    def __init__(self):
         super(Gui, self).__init__('CureApp')

         #Definition of the forms fields
         self.search = ControlText('Clinical Signs : ')
         self.button = ControlButton('Search')

#Execute the application
if __name__ == "__main__":  
    pyforms.start_app( Gui )
    PYFORMS_STYLESHEET_LINUX = './src/style.css'