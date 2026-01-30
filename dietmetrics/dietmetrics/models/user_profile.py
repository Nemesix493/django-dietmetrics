"""
Docstring for dietmetrics.models
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
