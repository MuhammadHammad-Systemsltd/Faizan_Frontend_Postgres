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
  if anvil.users.get_user():
    # print(anvil.users.get_user())
    return True

@anvil.server.callable
def login():
  # open login form
  anvil.users.login_with_form()
  
@anvil.server.callable
@anvil.tables.in_transaction
def save(Values):
  print("called Server success")
  app_tables.serversidedata.add_row(ProjectModel=Values[0], Username=Values[1],
                                    ProjectName=Values[2], ProjCov=Values[3],
                                    ProjectLocation=Values[4], ProjectClient=Values[5],
                                    ProjectSupportLvl=Values[6], ProjectTechnology=Values[7],
                                    ProjEnv=Values[8], ProjExist=Values[9],
                                    ProjTicketing=Values[10], ProjectRep=Values[11],
                                    ProjVoiceSup=Values[12], ProjSLA=Values[13], 
                                    ProjMon=Values[14], ProjTicketCnt=Values[15],
                                    ProjSupMed=Values[16], ProjnoPortals=Values[17], 
                                    Feedback=Values[18], ResourceNo=Values[19],
                                   ResourceMsg=Values[20])
  
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



