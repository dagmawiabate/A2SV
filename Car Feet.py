def carFleet(target, position, speed):
  # Combine positions and speeds into tuples and sort them by position in descending order
  cars = sorted(zip(position, speed), reverse=True)

  # Function to caculate time taken by a car to reach target
  def time_to_reach(pos, spd):
    return (target - pos) / spd

  fleets = 0
  prev_time = -1

  # Iterate through the cars
  for pos, spd in cars:
    time = time_to_reach(pos, spd)

    # If the current car takes longer time than the previous car, it won't catch up
    if time > prev_time:
      fleets += 1
      prev_time = time

  return fleets