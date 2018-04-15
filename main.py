
dict = {}
import icalendar

# input: my master calendar
filepath = "Chores 17S.ics"
g = open(filepath,'rb')
gcal = icalendar.Calendar.from_ical(g.read())
i = 0

name = ""
# for each name


class Chore:
    def __init__(self, name, description, frequency, days=None):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.days = days

dishes = Chore("dishes", "do the dishes", 7)


class ChoreCalendar:
    def __init__(self, chores, resident_file):
        self.residents = self.parse(resident_file)




    def make_main_cal(self):
        cal = icalendar.Calendar()

        for resident in self.residents:
            print
            resident
            # 	make a new calendar

    def make_individual_cals(self):
        for resident in self.residents:
            print resident
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
                        print resident, chore

                        cal.add_component(event)

            filename = resident + ".ics"
            f = open(filename, 'wb')

            f.write(cal.to_ical())
            f.close()

        g.close()
        for key in dict:
            print  dict[key], key
