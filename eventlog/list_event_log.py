import win32evtlog

events = win32evtlog.ReadEventLog(hand, flags,0)
events_list = [event for event in events if event.EventID == "27035"]
if event_list:
    print('Event Category:', events_list[0].EventCategory)
