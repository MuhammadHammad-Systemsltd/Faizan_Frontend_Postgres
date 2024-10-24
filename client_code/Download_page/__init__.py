from ._anvil_designer import Download_pageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Download_page(Download_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def Download_btn(self, **event_args):
    """This method is called when the button is clicked"""
    csv_file = app_tables.serversidedata.search().to_csv()
    anvil.media.download(csv_file)