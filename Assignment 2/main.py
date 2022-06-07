from Footballer import Footballer

# DRIVER CODE FOR PLACEMENT ASSIGNMENT 2
try:
    ronaldo = Footballer(name="Cristiano Ronaldo", nationality="Portugal", age=37, league="EPL",
                         team_name="Manchester United")
    ronaldo.set_team_details(established_year=1954, team_value=100000000, position=6)
    ronaldo.store_details(goals_per_game=1.5, assists_per_game=0.8, tackles_per_game=0.2)
    ronaldo.estimated_salary()
    ronaldo.print_details()

except Exception as e:
    print(f"ERROR: {str(e)}")
