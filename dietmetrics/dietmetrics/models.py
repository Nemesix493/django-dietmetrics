
"""
Models for the dietmetrics application.

This module defines the core data models used to store user diet profiles
and daily nutrition and activity metrics.
"""

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserDietmetricsProfile(models.Model):
    """
    Stores diet-related profile information for a user.

    This model is linked one-to-one with the Django user model and contains
    nutrition-related metadata such as maintenance calories.
    """

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="dietmetrics_profile",
    )

    @property
    def maintenance_calories(self) -> int:
        """
        Return the user's daily maintenance calorie level.

        This value represents the estimated or configured number of calories
        required to maintain the current body weight.
        """
        return 0


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
