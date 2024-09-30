from ._anvil_designer import Results_PageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Success import Success
from ..Survey import Survey
import random

class Results_Page(Results_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Label_ProjCov = Values[0]
    self.Label_ProjLoc = Values[1]
    self.Label_ProjClient = Values[2]
    # self.slider_label.text = self.slider_levels[self.Reporting_slider.level]

  def Reporting_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    # self.slider_label.text = self.slider_levels[self.Reporting_slider.level]

  def submit_button_click(self, **event_args):
    Values = Survey.Values
    """This method is called when the button is clicked"""
    print(Values)
    if None not in Values:
      # anvil.server.call('add_responses', age, frequency, methods, rating, comments)
      anvil.server.call("save", Values)
      alert("Thank you for submitting the form!\nWe will get back to you shortly!")
      get_open_form().content_panel.clear()
      get_open_form().content_panel.add_component(Success(), full_width_row=True)
    else:
      alert("Please fill out required fields")

  def submit_button_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass
