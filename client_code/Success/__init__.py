from ._anvil_designer import SuccessTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Success(SuccessTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def Home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    from ..Introduction import Introduction
    open_form(Introduction())
    pass
