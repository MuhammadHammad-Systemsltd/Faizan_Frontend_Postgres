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

Values = []
TotalResource = 0
class Survey(SurveyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
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
    global Values, TotalResource
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
    Values = client_details + [coverage, location, project_client, support_lvl, technology, environment,
             existing, ticketing, reporting_lvl, SLA, monitoring_tool, voice_sup, 
             medium, no_portals, ticket_count, feedback]
    TotalResource = 0
    if Values[0] == 'Shared':
        TotalResource += 1
    else:
        TotalResource += 1
    if Values[3] == '24/7':
        TotalResource += 3
    elif Values[3] == '16/5':
        TotalResource += 2
    else:
        TotalResource += 1
 
    if Values[4] == 'Onsite':
        TotalResource += 2
    else:
        TotalResource += 1
 
    if Values[5] == 'Pakistan':
        TotalResource += 1
    elif Values[5] == 'Middle east':
        TotalResource += 1
    elif Values[5] == 'US':
        TotalResource += 2
    else:
        TotalResource += 2
    if Values[6] == 'L3 support':
        TotalResource += 3
    elif Values[6] == 'L2 support':
        TotalResource += 2
    else:
        TotalResource += 1
 
    if Values[7] == 'Infrastructure':
        TotalResource += 2
    else:
        TotalResource += 1
 
    if Values[8] == 'Cloud':
        TotalResource += 1
    elif Values[8] == 'OnPrem':
        TotalResource += 1
    else:
        TotalResource += 1
 
    if Values[9] == 'Yes':
        TotalResource += 1
    else:
        TotalResource += 0
 
    if Values[10] == 'Yes':
        TotalResource += 1
    else:
        TotalResource += 0
 
    if Values[11] == 'No':
        TotalResource += 0
    elif Values[11] == 'Daily':
        TotalResource += 3
    elif Values[11] == 'Weekly':
        TotalResource += 2
    else:
        TotalResource += 1
 
    if Values[12] == '15 mins':
        TotalResource += 3
    elif Values[12] == '30 mins':
        TotalResource += 2
    else:
        TotalResource += 1
 
    if Values[13] == 'Yes':
        TotalResource += 1
    else:
        TotalResource += 0
 
    if Values[14] == 'Yes':
        TotalResource += 1
    else:
        TotalResource += 0
 
    if Values[15] == 'Email':
        TotalResource += 1
    elif Values[15] == 'Calls':
        TotalResource += 2
    else:
        TotalResource += 3
 
    if Values[16] == 'Yes':
        TotalResource += 1
    else:
        TotalResource += 0
 
    if Values[17] == 'High':
        TotalResource += 1
    else:
        TotalResource += 0
    Values.append(str(TotalResource))
    if None not in Values:
      # anvil.server.call('add_responses', age, frequency, methods, rating, comments)
      alert("Thank you for submitting the form!\nWe will get back to you shortly!")
      self.content_panel.clear()
      open_form('Results_Page')
    else:
      alert("Please fill out required fields")

  def submit_button_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

      
      
    


