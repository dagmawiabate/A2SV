class Solution:
  def find_players(self, matches: List[List[int]]) -> List[List[int]]:
    # Initialize dictionaries to track wins and losses for each player
    wins = {}
    losses = {}

    # Iterate through each match
    for winner, loser in matches:
      # Update wins dictionary
      wins[winner] = wins.get(winner, 0) + 1
      # Update losses dictionary
      losses[loser] = losses.get(loser, 0) + 1


    # Initialize lists to store players with zero or one loss
    no_losses = []
    one_loss = []

    # Iterate through all players
    for player in range(1, max(max(wins), max(losses)) + 1):
      # Check if the player has played at least one match
      if player in wins or player in losses:
        # Check if the player has no losses
        if player not in losses:
          no_losses.append(player)
        # Check if the player has exactly one loss
        elif losses[player] == 1:
          one_loss.append(player)

    return [no_losses, one_loss]