class StandUpBot:
    def __init__(self):
        # Dictionary to store team member details
        self.team_members = {}
        # Dictionary to store scheduled meetings (date: [list of members])
        self.meetings = {}

    def add_team_member(self, name, email):
        """Add a new team member."""
        self.team_members[name] = email

    def schedule_meeting(self, date, participants):
        """Schedule a meeting on a specific date with given participants."""
        if date in self.meetings:
            # Add to existing meeting
            self.meetings[date].extend(participants)
        else:
            # Create a new meeting entry
            self.meetings[date] = participants

    def show_meetings(self):
        """Display all scheduled meetings."""
        for date, participants in self.meetings.items():
            print(f"Meeting on {date} with participants: {', '.join(participants)}")

    def send_reminder(self, date):
        """Simulate sending a meeting reminder."""
        if date in self.meetings:
            participants = self.meetings[date]
            for participant in participants:
                email = self.team_members.get(participant, "Not Found")
                print(f"Sending reminder to {participant} ({email}) for the meeting on {date}.")
        else:
            print("No meeting scheduled on this date.")

# Example usage of the bot
bot = StandUpBot()

# Adding team members
bot.add_team_member("Alice", "alice@example.com")
bot.add_team_member("Bob", "bob@example.com")

# Scheduling a meeting
bot.schedule_meeting("2023-12-13", ["Alice", "Bob"])

# Showing scheduled meetings
bot.show_meetings()

# Sending a reminder for the meeting
bot.send_reminder("2023-12-13")