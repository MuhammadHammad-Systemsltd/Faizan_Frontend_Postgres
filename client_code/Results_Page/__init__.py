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
import random

class Results_Page(Results_PageTemplate):
  def __init__(self, **properties):
    
    from ..Survey import Values
    self.Values = Values
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Label_ProjModel.text, self.Label_Username.text, self.Label_ProjName.text = Values[0], Values[1], Values[2]
    self.Label_ProjCov.text, self.Label_ProjLoc.text = Values[3], Values[4]
    self.Label_ProjClient.text, self.Label_SupLvl.text  = Values[5], Values[6]
    self.Label_ProjTech.text,  self.Label_ProjEnv.text = Values[7], Values[8]
    self.Label_ProjExist.text, self.Label_ProjTick.text = Values[9], Values[10]
    self.label_ProjRep.text, self.label_VoiceSup.text = Values[11], Values[12]
    self.label_ProjSLA.text, self.label_ProjMon.text = Values[13], Values[14]
    self.label_ProjTickCnt.text, self.label_ProjSupMed.text = Values[15], Values[16]
    self.label_ProjnoPortals.text, self.Feedback.text = Values[17], Values[18]
    
    if int(Values[19]) >= 25:
        self.Label_Display_resourcereq.text = "Number of resources required for the project are Minimum 4 or Maximum 5"
    else:
        self.Label_Display_resourcereq.text = "Number of resources required for the project are Minimum 1 or Maximum 2"
    
  # self.slider_label.text = self.slider_levels[self.Reporting_slider.level]

  def Reporting_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    # self.slider_label.text = self.slider_levels[self.Reporting_slider.level]

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(self.Values)
    if None not in self.Values:
      anvil.server.call("save", self.Values)
      alert("Thank you for submitting the form!\nWe will get back to you shortly!")
      self.content_panel.clear()
      open_form('Success')
    else:
      alert("Please fill out required fields")

  def submit_button_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def BackButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    open_form('Survey')
