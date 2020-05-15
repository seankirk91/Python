Water= 29
Food = "29"
Exercise = 120

Hydration = int(Water)
Nourishment = int(Food)
Activity = int(Exercise)
Healthy = False

print(Healthy)

if Hydration == Nourishment or Nourishment == Activity or Exercise == Water:
    Healthy = True

print(Healthy)
