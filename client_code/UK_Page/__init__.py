from ._anvil_designer import UK_PageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..success import success


class UK_Page(UK_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.check_boxes = [
      self.check_box_1,
      self.check_box_2,
      self.check_box_3,
      self.check_box_4,
    ]
    self.slider_levels = {
      1: "strongly disagree",
      2: "disagree",
      3: "slightly disagree",
      4: "neutral",
      5: "slightly agree",
      6: "agree",
      7: "strongly agree",
    }
    # set the slider to neutral initially
    self.slider_1.level = 4
    self.slider_label.text = self.slider_levels[self.slider_1.level]

  def slider_1_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.slider_label.text = self.slider_levels[self.slider_1.level]

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    Dataleak = self.Dataleak_dropdown.selected_value
    methods = [box.text for box in self.check_boxes if box.checked == True]
    text_service = self.Service_use_text.text
    rating = self.slider_label.text
    comments = self.comment_area.text
    if Dataleak and text_service and methods is not None:
      print(f"Values are {Dataleak}, {text_service}, {methods}, ratings are {rating} and Extra Comments are <{comments}>")
      open_form(success())
      
      

    else:
      alert("Please fill out required fields")

