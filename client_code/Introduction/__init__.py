from ._anvil_designer import IntroductionTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EU_page import EU_page
from ..UK_Page import UK_Page


class Introduction(IntroductionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def Region_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def Username_text_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    
    pass

  def next_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    region = self.Region_dropdown.selected_value
    text = self.Username_text.text
    project = self.Project_text.text
    
    if region == "UK" or "Canada" or "USA" or "Europe":
      open_form(UK_Page())
    else:
      print("None")
      
    print(f"This are the values Region {region}, text {text} and Project {project}")
    
