
def moon_phase(phase):
  if phase == "New Moon":
    return("🌑")
  
  elif phase == "Waxing Crescent":
    return("🌒")
  
  elif phase == "First Quarter":
    return("🌓")
  
  elif phase == "Waxing Gibbous":
    return("🌔")

  elif phase == "Full Moon":
    return("🌕")
  
  elif phase == "Waning Gibbous":
    return("🌖")
  
  elif phase == "Last Quarter":
    return("🌗")

  elif phase == "Waning Crescent":
    return("🌘")
  else:
    return("Invalid moom phase")

answer = moon_phase("New Moon")

print(answer)


import random

print(random.__file__)  # Te dice dónde está el código fuente
