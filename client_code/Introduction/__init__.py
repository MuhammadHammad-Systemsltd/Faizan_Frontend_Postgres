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
  def IntroNext_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    model = self.ProjectModel_dropdown.selected_value
    client = self.Clientname_text.text
    project = self.ProjectName_text.text
    
    if model and client and project:
      alert("Welcome " + client)
      open_form(Survey())
    else:
      alert("Please fill out all the fields!")
      
    print(f"This are the values Project Model: {model}\nClient Name: {client}\nProject Name {project}")
    
