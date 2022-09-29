def add_time(start, duration, startDay=None):

  start_hour,start_minute = int(start.split(":")[0]), int(start.split(":")[1].split()[0])
  add_hour,add_minute = int(duration.split(":")[0]), int(duration.split(":")[1])
  days_later = 0
  
  if start[-2:]=="AM":
    if start_hour==12:
      start_hour = 0
  else:
    start_hour+=12
  final_hour = start_hour
  
  if startDay:
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

  final_minute = start_minute + add_minute
  if final_minute>=60:
    final_hour+=1
    final_minute%=60
    if final_hour>=24:
      days_later += 1
      final_hour%=24
      
  days_later += add_hour//24
  final_hour += add_hour % 24
  if final_hour>=24:
    days_later +=1
    final_hour%=24
  
  new_time = "{}:{} {}{}".format(
    final_hour-12 if final_hour>12 else 12 if final_hour==0 else final_hour,
    str(final_minute).zfill(2),
    "AM" if final_hour<12 else "PM",
    ", "+ days[(days.index(startDay.capitalize())+days_later)%7] if startDay else ""
  )
  
  return new_time + " (next day)" if days_later==1 else new_time+" ({} days later)".format(days_later) if days_later>1 else new_time
