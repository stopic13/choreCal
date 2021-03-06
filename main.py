import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

dict = {}
import icalendar
from datetime import datetime, timedelta
from random import shuffle

HOST_ADDR = "username@gmail.com"
HOST_PW = "LOL"

# input: my master calendar
filepath = "Chores 17S.ics"
#g = open(filepath,'rb')
#gcal = icalendar.Calendar.from_ical(g.read())
i = 0

name = ""
# for each name


class Chore:
    def __init__(self, name, description, frequency, time_of_day=None, days=None):
        self.name = name
        self.description = description
        self.frequency = frequency
        if time_of_day == None:
            self.start_date = datetime(2018, 4, 5, 8)
            print(self.start_date)
        self.end_date = datetime(2018,4, 29, 8)



dishes = Chore("dishes", "do the dishes", 7)
chores = [dishes]

class ChoreCalendar:
    def __init__(self, chores, resident_file):
        self.chores = chores
        self.residents = self.parse_emails(resident_file)

    def read_template(self, filename):
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    def send_email(self):
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(HOST_ADDR, HOST_PW)
        for name, email in self.residents.items():
            message_template = self.read_template('message.txt')
            msg = MIMEMultipart()
            message = message_template.substitute(PERSON_NAME=name.title())
            msg['From'] = HOST_ADDR
            msg['To'] = email
            msg['Subject'] = ""
            msg.attach(MIMEText(message, 'plain'))
            s.send_message(msg)
            del msg

    def parse_emails(self, resident_file):
        users_emails = {}
        with open(resident_file) as f:
            for line in f:
                line_split_by_comma = line.split(',')
                name = line_split_by_comma[0].strip()
                email = line_split_by_comma[1].strip()
                users_emails[name] = email
        return users_emails


    def make_main_cal(self):
        cal = icalendar.Calendar()
        chore_freq = {}
        for resident in self.residents:
            chore_freq[resident] = 0

        for chore in self.chores:
            i = 0
            total_days = (chore.end_date - chore.start_date).days
            print(total_days)

            while i < total_days:
                event = icalendar.Event()
                event['summary'] = "CHORE: " + str(chore.name) + " " + str(chore.description)
                event['dtstart'] =  chore.start_date + timedelta(days=i)
                cal.add_component(event)

                i += 1

        f = open("main_cal.ics", 'wb')

        f.write(cal.to_ical())

            #print(chore)



            #  print (resident)

            # 	make a new calendar

    def make_individual_cals(self):
        for resident in self.residents:
            print (resident)
            # 	make a new calendar
            cal = icalendar.Calendar()

            #for each event
            for component in gcal.walk('vevent'):
                summary = component.get('summary')
                if ":" in summary:

                    chore,name = summary.split(":")
                    chore.strip()
                    name.strip()

                    #if name in event name
                    if resident in name:

                        #add to calendar
                        event = icalendar.Event()
                        event['summary'] = "CHORE: " + str(chore)
                        event['dtstart'] = component.get('dtstart')

                        #print resident, name
                        if resident in dict:
                            dict[resident] += 1
                        else:
                            dict[resident] = 1
                        print (resident, chore)

                        cal.add_component(event)

            filename = resident + ".ics"
            f = open(filename, 'wb')

            f.write(cal.to_ical())
            f.close()

        g.close()
        for key in dict:
            print (dict[key], key)

cal = ChoreCalendar(chores, "users.csv")
cal.make_main_cal()
