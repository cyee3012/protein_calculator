mass = raw_input("Welcome to protein calculator! Would you like to us kgs or lbs?")

if mass == "kgs":
  print("OK! So you want to use the metric system. In that case, please tell me how much you weigh in " + mass + "?")
elif mass == "lbs":
  print("OK! So you want to use the imperial system. In that case, please tell me how much you weigh in " + mass + "?")

weight = raw_input()

if mass == "kgs":
  protein_low = float(weight) * 1.2
  protein_low = str(protein_low)
  protein_height = float(weight) * 1.7
  protein_height = str(protein_height)
elif mass == "lbs":
  protein_low = float(weight) * 0.5
  protein_low = str(protein_low)
  protein_height = float(weight) * 0.8
  protein_height = str(protein_height)

print("I see...so you weigh " + weight + mass + ". That means you should try to eat around " + protein_low + "-" + protein_height + "g of protein a day to gain muscle!")
