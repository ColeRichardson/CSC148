class Tournament:
    """A sports tournament.

    === Attributes ===
    teams:
        The names of the teams in this tournament.
    team_stats:
        The history of each team in this tournament. Each key is a team name,
        and each value stores the number of games played and the number won.

    === Sample usage ===
    >>> t = Tournament(['a', 'b', 'c'])
    >>> t.record_game('a', 'b', 10, 4)
    >>> t.record_game('a', 'c', 5, 1)
    >>> t.record_game('b', 'c', 2, 0)
    >>> t.best_percentage()
    'a'
    """
    # Attribute types
    teams: List[str]
    team_stats: Dict[str, List[int]]

    def __init__(self, teams: List[str]) -> None:
        """Initialize a new Tournament among the given teams.
        """
        self.team_stats = {}                       # Line 1
        self.teams = []                            # Line 2
        for team_name in teams:                    # Line 3
            self.teams.append(team_name)           # Line 4
            self.team_stats[team_name] = [0, 0]    # Line 5

    def record_game(self, team1: str, team2: str,
                    score1: int, score2: int) -> None:
        """Record the fact that <team1> played <team2> with the given scores.

        <team1> scored <score1> and <team2> scored <score2> in this game.

        Precondition: team1 and team2 are both in this tournament.
        """

        # YOUR CODE HERE
        pass
    
    def best_percentage(self) -> str:
        """Return the team name with the highest percentage of games won.

        If no team has won a game, return the empty string.
        Otherwise if there is a tie for best percentage, return the name of any
        of the tied teams.
        """

        # YOUR CODE HERE
        pass
