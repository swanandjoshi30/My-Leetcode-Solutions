class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """
        Args:
            day (int): The day of the month (1-31).
            month (int): The month (1-12).
            year (int): The year.

        Returns:
            str: The day of the week in full string format (e.g., 'Monday').
        """
        # Create a datetime object for the given date
        res = datetime.datetime(year, month, day)
        # Format and return the day of the week
        return res.strftime("%A")
