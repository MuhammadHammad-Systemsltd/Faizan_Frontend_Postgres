from ._anvil_designer import Landing_PageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Survey import Survey

class Landing_Page(Landing_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings
    
    self.init_components(**properties)
    if anvil.server.call('check_admin'):
      self.login_link.visible = False
      self.logout_link.visible = True
    else:
      self.login_link.visible = True
      self.logout_link.visible = False
  
  def GetStarted_button_click(self, **event_args):
    """This method is called when the Button is Pressed"""
    self.content_panel.clear()
    open_form('Introduction')

  def login_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    if anvil.users.login_with_form(remember_by_default=False, allow_cancel=True, show_signup_option=True):
      open_form('Download_page')

  def logout_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    self.content_panel.clear()
    open_form('Landing_Page')
    self.logout_link.visible = False
    self.login_link.visible = True

  def signup_link_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.signup_with_email()
    anvil.users.si









