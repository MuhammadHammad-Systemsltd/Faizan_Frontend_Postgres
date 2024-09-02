from ._anvil_designer import IntroductionTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Survey import Survey


class Introduction(IntroductionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def ProjectModel_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def Clientname_text_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    
    pass

  def IntroNext_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    model = self.ProjectModel_dropdown.selected_value
    client = self.Clientname_text.text
    project = self.ProjectName_text.text
    
    if model is not None:
      open_form(Survey())
    else:
      print("Model Value Found = None")
      
    print(f"This are the values Project Model: {model}\nClient Name: {client}\nProject Name {project}")
    
