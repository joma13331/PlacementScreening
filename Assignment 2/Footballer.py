from Sportsperson import Sportsperson
from Team import Team
import logging


# EXAMPLE MULTIPLE INHERITANCE
class Footballer(Sportsperson, Team):
    """
    Class Name: Footballer
    Description: This class is used to instantiate a footballer, store relevant
                 details and perform required actions.
    """

    # CLASS VARIABLES
    base_salary = 1000000

    def __init__(self, name, nationality, age, team_name, league):
        """
        Method Name: __init__
        Description: This method is the constructor for Footballer class. It
                     initializes class variables which are important for any
                     footballer.
        params: name - Name of the footballer
                nationality - Country to which the foolballer belongs to
                age - Age of the footballer
                team_name - Name of footballer's team
                league - league to which the team belongs to
        """

        # Calling Constructors of Base Classes
        Sportsperson.__init__(self, name=name, nationality=nationality, age=age)
        Team.__init__(self, team_name=team_name, league=league)

        # Setting up Logging Feature
        self.football_logger = logging.getLogger("football_logger")
        self.football_logger.setLevel(logging.INFO)
        football_logger_handler = logging.FileHandler("Football.txt")
        formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        football_logger_handler.setFormatter(formatter)
        self.football_logger.addHandler(football_logger_handler)

    # INHERITED ABSTRACT METHOD IMPLEMENTED
    def store_details(self, goals_per_game, assists_per_game, tackles_per_game):
        """
        Method Name: store_details
        Description: This method is used to store those details about a footballer
                     which are important to recognize how important/good that
                     footballer is
        params: goals_per_game- what is the goals per game of the player for his/her
                career
                assists_per_game - what is the assists per game of the player for
                his/her career
                tackles_per_game - what is the tackles per game of the player for
                his/her career
        return: None
        """
        try:
            self.goals_per_game = goals_per_game
            self.assists_per_game = assists_per_game
            self.tackles_per_game = tackles_per_game
            self.football_logger.info(f"Information about game play of {self.name} obtained")
        except Exception as e:
            self.football_logger.error(f"ERROR: {str(e)}")
            print(f"ERROR: {str(e)}")

    # EXAMPLE DECORATOR
    @staticmethod
    def salary_individual(nationality, age, goals_per_game, assists_per_game,
                          tackles_per_game):
        """
        Method Name: salary_individual
        Description: This method is used to calculate how much the footballer should
                     earn based on his/her own performance
        params: nationality - country to which the footballer belongs to
                age - age of the footballer
                goals_per_game- what is the goals per game of the player for his/her
                career
                assists_per_game - what is the assists per game of the player for
                his/her career
                tackles_per_game - what is the tackles per game of the player for
                his/her career
        returns: salary_multiplier - Salary multiplier due to the players own effort
        """
        try:
            multiplier = 1
            good_country = ['England', 'Germany', 'Spain', 'Italy']

            if nationality in good_country:
                multiplier *= 1.5

            if 25 <= age <= 32:
                multiplier *= 1.5

            salary_multiplier = multiplier * goals_per_game * assists_per_game * tackles_per_game * 0.1

            return salary_multiplier

        except Exception as e:
            print(f"ERROR: {str(e)}")
            raise e

    # EXAMPLE DECORATOR
    @staticmethod
    def salary_team(league, established_year, team_value, position):
        """
        Method Name: salary_team
        Description: This method is used to calculate how much the footballer should
                     earn based on his/her team's performance
        params: league - league to which the team belongs to
                established_year - year in which the team was established
                team_value - estimated worth of the team
                position - position of the team in the league
        returns: salary_multiplier - Salary multiplier due to the players own effort
        """
        try:
            multiplier = 1

            good_league = ["EPL", "La Liga", "Bundesliga", "Seria A"]

            if league in good_league:
                multiplier *= 1.5

            salary_multiplier = multiplier * (2022 - established_year) / 10 * (20 - position) * team_value * 0.000001

            return salary_multiplier

        except Exception as e:
            print(f"ERROR: {str(e)}")
            raise e

    # INHERITED ABSTRACT METHOD IMPLEMENTED
    def estimated_salary(self):
        """
        Method Name: estimated_salary
        Description: This method used two static methods to estimate what the salary
                     of the footballer should be.
        return: None
        """
        try:
            salary_individual_multiplier = self.salary_team(self.league, self.established_year, self.team_value,
                                                            self.position)
            self.football_logger.info(f"Individual Salary Multiplier:{salary_individual_multiplier}")

            salary_team_multiplier = self.salary_individual(self.nationality, self.age,
                                                            self.goals_per_game, self.assists_per_game,
                                                            self.tackles_per_game)
            self.football_logger.info(f"Individual Team Multiplier:{salary_team_multiplier}")

            self.salary = int(Footballer.base_salary * salary_individual_multiplier * salary_team_multiplier)
            self.football_logger.info(f"Individual:{self.salary}")

        except Exception as e:
            self.football_logger.error(f"ERROR: {str(e)}")
            print(f"ERROR: {str(e)}")

    # INHERITED ABSTRACT METHOD IMPLEMENTED
    def print_details(self):
        """
        Method Name: print_details
        Description: This method prints all the relevant details about the
                     footballer.
        return None
        """
        try:
            print(f"""
    Name of the footballer: {self.name}
    Team:{self.team_name}
    Goals scored per game: {self.goals_per_game}
    Assists per game: {self.assists_per_game}
    Tackles per game: {self.tackles_per_game}
    Estimated salary {int(self.salary)}\n
    """)
            self.football_logger.info(f"Details about {self.name} displayed")
        except Exception as e:
            self.football_logger.error(f"ERROR: {str(e)}")
            print(f"ERROR: {str(e)}")
