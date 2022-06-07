import logging

# BASE CLASS 2
class Team:
    """
    Class Name: Team
    Description: This class will hold details about a sporting team. This class is
               intended to be inherited by any sportsperson class
    """

    def __init__(self, team_name, league):
        """
        Method Name: __init__
        Description: This method is the constructor for Team class. It
                     initializes class variables which are important for any
                     sportsperson
        params: team_name - Name of the team
                league - league to which the team belongs to
        """
        self.team_name = team_name
        self.league = league

        self.team_logger = logging.getLogger("team_logger")
        self.team_logger.setLevel(logging.INFO)
        team_logger_handler = logging.FileHandler("Team.txt")
        formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        team_logger_handler.setFormatter(formatter)
        self.team_logger.addHandler(team_logger_handler)

    def set_team_details(self, established_year, team_value, position):
        """
        Method Name: set_team_details
        Description: This method is used to store the details about a team in the
                   instance variables.
        params: established_year - year in which the team was established
              team_value - estimated worth of the team
              position - position of the team in the league
        return None
        """
        try:

            self.established_year = established_year
            self.team_value = team_value
            self.position = position

            self.team_logger.info(f" Details about {self.team_name} stored")

        except Exception as e:
            self.team_logger.error(f"ERROR: {str(e)}")
            print(f"ERROR: {str(e)}")
