"""
this is almost the same as the best books problem
"""

def team_with_best_average_score(games):
    best = games[0]
    for game in games:
        if game["score"] > best["score"]:
            best = game
    return best["team_name"]

games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers", 
     "score": 30
    },
    {"team_name": "Lions", 
     "score": 27
    },
    {"team_name": "Bears", 
     "score": 20
    },
    {"team_name": "Tigers", 
     "score": 24
    },
    {"team_name": "Bears", 
     "score": 22
    }
]

print(team_with_best_average_score(games))
   
    
    