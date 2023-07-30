from tkinter import *


class FootballTeam:
    """
    This class creates a football team's statistics tracker
    """
    def __init__(self, name):
        self.__name = name
        self.__match_score = 0
        self.__points = 0
        self.__goal_for = 0
        self.__goal_against = 0
        
    def match_result(self, other):
        """
        This function uses the result from the match to determine
        the point which the team recieves
        :param other: the opposing team
        :type other: object
        """
        
        # The teams tied
        if self.__match_score == other.__match_score:
            self.__points += 1
        # The team won
        elif self.__match_score > other.__match_score:
            self.__points += 3
        
        # The team lost
        elif self.__match_score < other.__match_score:
            
            pass
    def add_gf(self, score):
        """
        This function adds up the total goal scored
        :param score: the goals scored in the match
        :type score: int
        """
        self.__goal_for += score
    
    def add_ga(self, score):
        """
        This function adds up the total goal scored
        against
        :param score: the goals the opposing team scored
        in the match
        :type score: int
        """
        self.__goal_against += score
    def teamName(self):
        return self.__name
    def get_points(self):
        return self.__points
    
    def get_gf(self):
        return self.__goal_for
    
    def get_ga(self):
        return self.__goal_against
    
    def get_goal_diff(self):
        return self.__goal_for - self.__goal_against
    
    def update_match_results(self, score):
        """
        Stores the score of the match
        :param score: the goals scored
        :type score: int
        """
        self.__match_score = score
class UserInterface:
    """
    This class represents the GUI of the application
    """
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title("FOOTBALL SCORES")
        self.__teamName = Label(self.__main_window, text="INSERT TEAM NAMES HERE:")
        self.__teamName.grid(row=0, column=0)
        # Insert the team names
        self.__insertTeam1 = Entry(width=25)
        self.__insertTeam2 = Entry(width=25)
        self.__insertTeam3 = Entry(width=25)
        self.__insertTeam4 = Entry(width=25)
        self.__insertTeam1.grid(row=1, column=0)
        self.__insertTeam2.grid(row=2, column=0)
        self.__insertTeam3.grid(row=3, column=0)
        self.__insertTeam4.grid(row=4, column=0)
        # Initiate the main menu
        self.__start_button = Button(self.__main_window, text="START", command=self.popup, width=15)
        self.__start_button.grid(row=2, column=1)
        # Quit the application
        self.__quit_button = Button(self.__main_window, text="QUIT", command=quit, width=15)
        self.__quit_button.grid(row=3, column=1)
        self.__main_window.mainloop()
    def popup(self):
        """
        This popup window represents the main window of the 
        application
        """
        popupWindow = Toplevel(self.__main_window)
        popupWindow.title("MAIN WINDOW")
        # Matchpoint entry
        matchpoint_entry_section = Label(popupWindow, text="MATCH RESULTS")
        matchpoint_entry_section.grid(row=0, column=0)
        # These variables store the team names
        teamA_name = self.__insertTeam1.get()
        teamB_name = self.__insertTeam2.get()
        teamC_name = self.__insertTeam3.get()
        teamD_name = self.__insertTeam4.get()
        # Shows the team names of each match              
        teamA1_label = Label(popupWindow, text=teamA_name)
        teamB1_label = Label(popupWindow, text=teamB_name)
        teamC1_label = Label(popupWindow, text=teamC_name)
        teamD1_label = Label(popupWindow, text=teamD_name)
        teamA2_label = Label(popupWindow, text=teamA_name)
        teamB2_label = Label(popupWindow, text=teamC_name)
        teamC2_label = Label(popupWindow, text=teamB_name)
        teamD2_label = Label(popupWindow, text=teamD_name)
        teamA3_label = Label(popupWindow, text=teamA_name)
        teamB3_label = Label(popupWindow, text=teamD_name)
        teamC3_label = Label(popupWindow, text=teamB_name)
        teamD3_label = Label(popupWindow, text=teamC_name)
        teamA1_label.grid(row=1, column=0)
        teamB1_label.grid(row=1, column=4)
        teamC1_label.grid(row=2, column=0)
        teamD1_label.grid(row=2, column=4)
        teamA2_label.grid(row=4, column=0)
        teamB2_label.grid(row=4, column=4)
        teamC2_label.grid(row=5, column=0)
        teamD2_label.grid(row=5, column=4)
        teamA3_label.grid(row=7, column=0)
        teamB3_label.grid(row=7, column=4)
        teamC3_label.grid(row=8, column=0)
        teamD3_label.grid(row=8, column=4)
        # Enter the score of the match
        score1 = Entry(popupWindow, width=10)
        score2 = Entry(popupWindow, width=10)
        score3 = Entry(popupWindow, width=10)
        score4 = Entry(popupWindow, width=10)
        score5 = Entry(popupWindow, width=10)
        score6 = Entry(popupWindow, width=10)
        score7 = Entry(popupWindow, width=10)
        score8 = Entry(popupWindow, width=10)
        score9 = Entry(popupWindow, width=10)
        score10 = Entry(popupWindow, width=10)
        score11 = Entry(popupWindow, width=10)
        score12 = Entry(popupWindow, width=10)
        score1.grid(row=1, column=1)
        score2.grid(row=1, column=3)
        score3.grid(row=2, column=1)
        score4.grid(row=2, column=3)
        score5.grid(row=4, column=1)
        score6.grid(row=4, column=3)
        score7.grid(row=5, column=1)
        score8.grid(row=5, column=3)
        score9.grid(row=7, column=1)
        score10.grid(row=7, column=3)
        score11.grid(row=8, column=1)
        score12.grid(row=8, column=3)
        # Error message if the score is invalid
        error_message = Label(popupWindow)
        error_message.grid(row=9, column=0)
        
        # Separate the score entry section and the current leaderboard section
        section_separator1 = Label(popupWindow, text="|")
        section_separator2 = Label(popupWindow, text="|")
        section_separator3 = Label(popupWindow, text="|")
        section_separator4 = Label(popupWindow, text="|")
        section_separator5 = Label(popupWindow, text="|")
        section_separator6 = Label(popupWindow, text="|")
        section_separator7 = Label(popupWindow, text="|")
        section_separator8 = Label(popupWindow, text="|")
        section_separator9 = Label(popupWindow, text="|")
        section_separator10 = Label(popupWindow, text="|")
        section_separator1.grid(row=0, column=5)
        section_separator2.grid(row=1, column=5)
        section_separator3.grid(row=2, column=5)
        section_separator4.grid(row=3, column=5)
        section_separator5.grid(row=4, column=5)
        section_separator6.grid(row=5, column=5)
        section_separator7.grid(row=6, column=5)
        section_separator8.grid(row=7, column=5)
        section_separator9.grid(row=8, column=5)
        section_separator10.grid(row=9, column=5)
        # The topic of each column
        topic1 = Label(popupWindow, text="NO.")
        topic2 = Label(popupWindow, text="TEAM")
        topic3 = Label(popupWindow, text="POINTS")
        topic4 = Label(popupWindow, text="GD")
        topic5 = Label(popupWindow, text="GF")
        topic6 = Label(popupWindow, text="GA")
        topic1.grid(row=3, column=6)
        topic2.grid(row=3, column=7)
        topic3.grid(row=3, column=8)
        topic4.grid(row=3, column=9)
        topic5.grid(row=3, column=10)
        topic6.grid(row=3, column=11)
        # The label of the word LEADERBOARD
        leaderboard_label = Label(popupWindow, text="LEADERBOARD")
        leaderboard_label.grid(row=2, column=8)
        # The column of team names
        team1 = Label(popupWindow, text=teamA_name)
        team2 = Label(popupWindow, text=teamB_name)
        team3 = Label(popupWindow, text=teamC_name)
        team4 = Label(popupWindow, text=teamD_name)
        team1.grid(row=4, column=7)
        team2.grid(row=5, column=7)
        team3.grid(row=6, column=7)
        team4.grid(row=7, column=7)
        # The column of points
        point1 = Label(popupWindow, text=0)
        point2 = Label(popupWindow, text=0)
        point3 = Label(popupWindow, text=0)
        point4 = Label(popupWindow, text=0)
        point1.grid(row=4, column=8)
        point2.grid(row=5, column=8) 
        point3.grid(row=6, column=8)
        point4.grid(row=7, column=8)
        # The column of goal differences
        gd1 = Label(popupWindow, text=0)
        gd2 = Label(popupWindow, text=0)
        gd3 = Label(popupWindow, text=0)
        gd4 = Label(popupWindow, text=0)
        gd1.grid(row=4, column=9)
        gd2.grid(row=5, column=9)
        gd3.grid(row=6, column=9)
        gd4.grid(row=7, column=9)
        # The column of goals scored
        gf1 = Label(popupWindow, text=0)
        gf2 = Label(popupWindow, text=0)
        gf3 = Label(popupWindow, text=0)
        gf4 = Label(popupWindow, text=0)
        gf1.grid(row=4, column=10)
        gf2.grid(row=5, column=10)
        gf3.grid(row=6, column=10)
        gf4.grid(row=7, column=10)
        # The column of goals scored against
        ga1 = Label(popupWindow, text=0)
        ga2 = Label(popupWindow, text=0)
        ga3 = Label(popupWindow, text=0)
        ga4 = Label(popupWindow, text=0)
        ga1.grid(row=4, column=11)
        ga2.grid(row=5, column=11)
        ga3.grid(row=6, column=11)
        ga4.grid(row=7, column=11)
        def set_leaderboard(team_list):
            """
            This function determines the order of teams using the 
            statistics of each team
            :param team_list: list of the teams
            :type team_list: list
            :return: list of the teams on the leaderboard in
            the descending order
            :rtype: list
            """
            
            # Rank the leaderboard by points
            leaderboard = sorted(team_list, key=lambda x: x.get_points(), reverse=True)
            for i in range(0, len(leaderboard)):
                
                # If two teams are equal in points  
                if leaderboard[i].get_points() == leaderboard[i-1].get_points():
                    
                    # The team with higher goal difference goes first
                    if leaderboard[i].get_goal_diff() > leaderboard[i-1].get_goal_diff():
                        leaderboard.insert(i-1, leaderboard.pop(i))
                    # If the two teams are equal in goal difference
                    elif leaderboard[i].get_goal_diff() == leaderboard[i-1].get_goal_diff():
                        
                        # The team with the higher amount of goal scored goes first
                        if leaderboard[i].get_gf() > leaderboard[i-1].get_gf():
                            leaderboard.insert(i-1, leaderboard.pop(i))
                        # If the two teams are equal in amount of goal scored
                        elif leaderboard[i].get_gf() == leaderboard[i-1].get_gf():
                            
                            # The team with the lower amount of goal scored against goes first
                            if leaderboard[i].get_ga() < leaderboard[i-1].get_ga():
                                leaderboard.insert(i-1, leaderboard.pop(i))
            return leaderboard
        def update():
            """
            This function uses the result of the matches and determine the leaderboard
            based on points, goal difference, goals scored and goal scored against and 
            display the leaderboard
            """
            try:
                # Goals from each match
                score_1 = int(score1.get()) # Possible ValueError if nothing is entered
                score_2 = int(score2.get())
                score_3 = int(score3.get())
                score_4 = int(score4.get())
                score_5 = int(score5.get())
                score_6 = int(score6.get())
                score_7 = int(score7.get())
                score_8 = int(score8.get())
                score_9 = int(score9.get()) 
                score_10 = int(score10.get())
                score_11 = int(score11.get())
                score_12 = int(score12.get())
                # Matchscore is negative
                if score_1 < 0 or score_2 < 0 or score_3 < 0 or score_4 < 0 \
                    or score_5 < 0 or score_6 < 0 or score_7 < 0 or score_8 < 0 \
                    or score_9 < 0 or score_10 < 0 or score_11 < 0 or score_12 < 0:
                    error_message["text"] = "ERROR: Invalid matchscore"
                else:
                
                    # The teams created by the FootballTeam class
                    teamA = FootballTeam(teamA_name)
                    teamB = FootballTeam(teamB_name)
                    teamC = FootballTeam(teamC_name)
                    teamD = FootballTeam(teamD_name)
                    # Stores the match result entered by the user (GW1)
                    teamA.update_match_results(score_1)
                    teamB.update_match_results(score_2)
                    teamC.update_match_results(score_3)
                    teamD.update_match_results(score_4)
                    # Determine whether the team won, lost or tied (GW1)
                    teamA.match_result(teamB)
                    teamB.match_result(teamA)
                    teamC.match_result(teamD)
                    teamD.match_result(teamC)
                    # Stores the match result entered by the user (GW2)
                    teamA.update_match_results(score_5)
                    teamC.update_match_results(score_6)
                    teamB.update_match_results(score_7)
                    teamD.update_match_results(score_8)
                    # Determine whether the team won, lost or tied (GW2)
                    teamA.match_result(teamC)
                    teamC.match_result(teamA)
                    teamB.match_result(teamD)
                    teamD.match_result(teamB)
                    # Stores the match result entered by the user (GW3)
                    teamA.update_match_results(score_9)
                    teamD.update_match_results(score_10)
                    teamB.update_match_results(score_11)
                    teamC.update_match_results(score_12)
                    teamA.match_result(teamD)
                    teamD.match_result(teamA)
                    teamC.match_result(teamB)
                    teamB.match_result(teamC)
                    # Adds up the goals scored and scored against for each team
                    teamA.add_gf(score_1)
                    teamA.add_gf(score_5)
                    teamA.add_gf(score_9)
                    teamA.add_ga(score_2)
                    teamA.add_ga(score_6)
                    teamA.add_ga(score_10)
                    teamB.add_gf(score_2)
                    teamB.add_gf(score_7)
                    teamB.add_gf(score_11)
                    teamB.add_ga(score_1)
                    teamB.add_ga(score_8)
                    teamB.add_ga(score_12)
                    teamC.add_gf(score_3)
                    teamC.add_gf(score_6)
                    teamC.add_gf(score_12)
                    teamC.add_ga(score_1)
                    teamC.add_ga(score_5)
                    teamC.add_ga(score_9)
                    teamD.add_gf(score_4)
                    teamD.add_gf(score_8)
                    teamD.add_gf(score_10)
                    teamD.add_ga(score_3)
                    teamD.add_ga(score_7)
                    teamD.add_ga(score_9)
                    # List of 4 teams out of order
                    team_list = [teamA, teamB, teamC, teamD]
                    leaderboard = set_leaderboard(team_list)
                    # Displays the final result on the leaderboard
                    team1["text"] = leaderboard[0].teamName()
                    team2["text"] = leaderboard[1].teamName()
                    team3["text"] = leaderboard[2].teamName()
                    team4["text"] = leaderboard[3].teamName()
                    point1["text"] = leaderboard[0].get_points()
                    point2["text"] = leaderboard[1].get_points()
                    point3["text"] = leaderboard[2].get_points()
                    point4["text"] = leaderboard[3].get_points()
                    gd1["text"] = leaderboard[0].get_goal_diff()
                    gd2["text"] = leaderboard[1].get_goal_diff()
                    gd3["text"] = leaderboard[2].get_goal_diff()
                    gd4["text"] = leaderboard[3].get_goal_diff()
                    ga1["text"] = leaderboard[0].get_ga()
                    ga2["text"] = leaderboard[1].get_ga()
                    ga3["text"] = leaderboard[2].get_ga()
                    ga4["text"] = leaderboard[3].get_ga()
                    gf1["text"] = leaderboard[0].get_gf()
                    gf2["text"] = leaderboard[1].get_gf()
                    gf3["text"] = leaderboard[2].get_gf()
                    gf4["text"] = leaderboard[3].get_gf()
            # Matchscore box is blank
            except ValueError:
                
                error_message["text"] = "ERROR: Missing matchscore"
                
        update_table_button = Button(popupWindow, text="UPDATE TABLE",
                                     command=update, width=15)
        update_table_button.grid(row=9, column=2)
        # The numbers besides the team names
        number1_label = Label(popupWindow, text=1)
        number2_label = Label(popupWindow, text=2)
        number3_label = Label(popupWindow, text=3)
        number4_label = Label(popupWindow, text=4)
        number1_label.grid(row=4, column=6)
        number2_label.grid(row=5, column=6)     
        number3_label.grid(row=6, column=6)
        number4_label.grid(row=7, column=6)
        # The goal separators
        goal_separator1 = Label(popupWindow, text="-")
        goal_separator2 = Label(popupWindow, text="-")
        goal_separator3 = Label(popupWindow, text="-")
        goal_separator4 = Label(popupWindow, text="-")
        goal_separator5 = Label(popupWindow, text="-")
        goal_separator6 = Label(popupWindow, text="-")
        goal_separator1.grid(row=1, column=2)
        goal_separator2.grid(row=2, column=2)
        goal_separator3.grid(row=4, column=2)
        goal_separator4.grid(row=5, column=2)
        goal_separator5.grid(row=7, column=2)
        goal_separator6.grid(row=8, column=2)
        def return_menu():
            """
            Closes only the main window of the application without
            quitting the whole application
            """
            popupWindow.destroy()
            popupWindow.update()
        quitButton = Button(popupWindow, text="RETURN", command=return_menu, width=15)
        quitButton.grid(row=9, column=4)
    def quit(self):
        """
        Quits the whole application
        """
        self.__main_window.destroy()
def main():
    UserInterface()
if __name__ == "__main__":
    main()