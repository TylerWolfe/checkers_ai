import json

class Logger:
    def __init__(self, log_file="game_log.txt"):
        self.log_file = log_file

    def log_move(self, move):
        with open(self.log_file, "a") as f:
            f.write(f"{move}\n")

    def save_stats(self, stats_file="stats.json"):
        stats = {"games_played": 10, "wins": 5, "losses": 5}
        with open(stats_file, "w") as f:
            json.dump(stats, f)

    def load_stats(self, stats_file="stats.json"):
        try:
            with open(stats_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"games_played": 0, "wins": 0, "losses": 0}