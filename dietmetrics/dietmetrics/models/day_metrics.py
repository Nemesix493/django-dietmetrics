"""
DayMetrics model definition.
"""

from django.db import models

from .user_profile import UserDietmetricsProfile


class DayMetric(models.Model):
    """
    Stores daily nutrition and activity metrics for a user.

    Each entry represents one day of tracking including calorie intake
    and energy expenditure from physical activity.
    """

    dietmetrics_user = models.ForeignKey(
        to=UserDietmetricsProfile,
        on_delete=models.CASCADE,
        related_name="daily_metrics",
    )
    date = models.DateField()
    calories = models.IntegerField()
    activity_expenditure = models.IntegerField()
