from lib.bot import command
from lib.tools import Database

class TracDB(Database):

    def create_structure(self):
        c = self.con.cursor()
        c.execute("""
            CREATE TABLE trac (
                  id INTEGER PRIMARY KEY,
                  ticket INTEGER UNIQUE,
                  summary TEXT,
                  component TEXT,
                  version TEXT,
                  milestone TEXT,
                  type TEXT,
                  owner TEXT,
                  status TEXT,
                  created TIMESTAMP,
                  updated TIMESTAMP,
                  description TEXT,
                  reporter TEXT
            )""")
        self.con.commit()

class Ticket(command):

    regex = r".*?(?:%(cmd)s\s+(\d+)|(t#\d+)).*"
    triggers = [r"(?=t#\d+)"]
    syntax = 'ticket id | t#id'
    example = "Please see t#320"
    doc = " ".join(
        [ "Print an url to the id of the ticket specified"
        ])

    def run(self, bot, data):
        tid = None
        if data.group(1):
            tid = data.group(1)
        elif data.group(2):
            tid = data.group(2)[2:]
        if tid:
            tracker = "http://wiki.neurohack.com/transcendence/trac/ticket/%s" % tid
            bot.say("Ticket #%s: %s" % (tid, tracker))
