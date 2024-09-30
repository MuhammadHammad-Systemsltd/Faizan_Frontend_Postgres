from ._anvil_designer import SurveyTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Success import Success
from ..Results_Page import Results_Page
import random

class Survey(SurveyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.Values = []
    self.slider_levels = {1: 'No',
                          2: 'Daily',
                          3: 'Weekly',
                          4: 'Monthly'}
    #set the slider to neutral initially
    self.Reporting_slider.level = 4
    # self.slider_label.text = self.slider_levels[self.Reporting_slider.level]


  def Reporting_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    # self.slider_label.text = self.slider_levels[self.Reporting_slider.level]

  def submit_button_click(self, **event_args):
    from ..Introduction import User_details
    """This method is called when the button is clicked"""
    ## Page 1 or Section 1 Project Details
    coverage = self.coverage_dropdown.selected_value
    location = self.location_dropdown.selected_value
    project_client = self.client_dropdown.selected_value\
    ## Page 2 or Section 2 Technical Details
    support_lvl = self.support_level_dropdown.selected_value
    technology = self.project_tech_dropdown.selected_value
    environment = self.project_env_dropdown.selected_value
    # Project Yes n no
    existing = self.projectex_RY.get_group_value()
    ticketing = self.projecttick_RY.get_group_value()
    # Project Reporting slider
    reporting_lvl = self.slider_levels[self.Reporting_slider.level]
    # Support Requirments
    voice_sup = self.voice_sup_dropdown.selected_value
    SLA = self.sla_dropdown.selected_value
    monitoring_tool = self.monitoring_tool_dropdown.selected_value
    ticket_count = self.ticket_count_dropdown.selected_value
    medium = self.sup_medium_dropdown.selected_value
    no_portals = self.number_portals_dropdown.selected_value
    
    # Additional Comments
    feedback = self.feedback_area.text
    print(coverage)
    client_details = User_details
    # Create a random ID for the CLient
    print(random.randint(1, 10000))
    Values = client_details + [coverage, location, project_client,support_lvl, technology, environment,
             existing, ticketing, reporting_lvl, voice_sup, SLA, monitoring_tool,
             ticket_count, medium, no_portals, feedback]
    if None not in Values:
      # anvil.server.call('add_responses', age, frequency, methods, rating, comments)
      alert("Thank you for submitting the form!\nWe will get back to you shortly!")
      get_open_form().content_panel.clear()
      get_open_form().content_panel.add_component(Results_Page(), full_width_row=True)
    else:
      alert("Please fill out required fields")

  def submit_button_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

      
      
    


