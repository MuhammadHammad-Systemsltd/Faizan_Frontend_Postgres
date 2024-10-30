import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def check_admin():
   if anvil.users.get_user() == "hammad@hammad.asd":
      print(anvil.users.get_user())
      return True

@anvil.server.callable
@anvil.tables.in_transaction
def save(Values):
  print("called Server success")
  app_tables.serversidedata.add_row(ProjectModel=Values[0], Username=Values[1], ProjectName=Values[2])
@anvil.server.callable
def get_total_responses():
  return len(app_tables.responses.search())

@anvil.server.callable
def get_tables():
  ages = app_tables.age.search()
  frequency = app_tables.frequency.search()
  methods = app_tables.method.search()
  ratings = app_tables.ratings.search()
  return [ages, frequency, methods, ratings]



