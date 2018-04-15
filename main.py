
def parse(resident_file):
    users_emails = {}
    with open(resident_file) as f:
        for line in f:
            line_split_by_comma = line.split(',')
            name = line_split_by_comma[0].strip()
            email = line_split_by_comma[1].strip()
            users_emails[name] = email
    return users_emails

dict = {}
import icalendar

# input: my master calendar
filepath = "Chores 17S.ics"
g = open(filepath,'rb')
gcal = icalendar.Calendar.from_ical(g.read())
i = 0

name = ""
# for each name
for resident in residents:
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
