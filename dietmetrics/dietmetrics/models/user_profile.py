"""
Docstring for dietmetrics.models
"""

from django.db import models
from django.contrib.auth import get_user_model

from ..conf import DietmetricsSettings

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

    # Settings fields

    maintenance_period_days = models.IntegerField(
        null=True,
        blank=True
    )

    @property
    def maintenance_period(self) -> int:
        """
        Return the user's maintenance period in days.

        This value indicates the number of days over which maintenance calories
        are calculated or averaged.
        """
        return (
            self.maintenance_period_days
            if self.maintenance_period_days is not None
            else DietmetricsSettings.MAINTENANCE_PERIOD_DAYS
        )

    @property
    def maintenance_calories(self) -> int:
        """
        Return the user's daily maintenance calorie level.

        This value represents the estimated or configured number of calories
        required to maintain the current body weight.
        """
        return 0

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta class to add constraints.
        """
        constraints = [
            models.CheckConstraint(
                condition=models.Q(maintenance_period_days__gt=0),
                name="maintenance_period_positive"
            )
        ]
