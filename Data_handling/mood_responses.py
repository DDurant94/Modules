import re
import random as r

def mood_response(mood):
  regex_sad = r"sad|bad|upset"
  sad_responses = ["Lets turn that frown upside down with some laughter.","Tomorrow is a new day with new possibilities!","All things are healed with time."]
  sad = re.search(regex_sad,mood.lower())

  regex_happy = r"happy|good|joy|great"
  happy_responses = ["Best things in life are associated with happiness. Live in this moment to remember it forever!","Let's keep this going for the rest of the week.", "I love to hear that! Always do what makes you happy in the end!"]
  happy = re.search(regex_happy,mood.lower())

  regex_excited = r"excited|ecstatic"
  excited_responses = ["I am happy to hear that! Remember that being patient for these kind of things are key.","I am excited for you and this adventure you are on.", "I can't wait for you to experience this and come back and tell me all about it."]
  excited = re.search(regex_excited,mood.lower())

  regex_normal = r"normal|ok|okay|alright"
  normal_responses = ["What can you think of to make your mood happy or excited?","I hope that changes soon.","We should always be happy for what we are given in life."]
  normal = re.search(regex_normal,mood.lower())
  
  if sad:
    return f"{r.choice(sad_responses)}\n"
  elif happy:
    return f"{r.choice(happy_responses)}\n"
  elif excited:
    return f"{r.choice(excited_responses)}\n"
  elif normal:
    return f"{r.choice(normal_responses)}\n"
  else:
    return "I am sorry, but I don't have a response for your input."
