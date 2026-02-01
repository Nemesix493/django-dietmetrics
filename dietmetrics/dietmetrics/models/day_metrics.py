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
    date = models.DateField(
        null=False,
        blank=False
    )
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    calories = models.IntegerField(
        null=True,
        blank=True
    )
    activity_expenditure = models.IntegerField(
        null=True,
        blank=True
    )
    weight = models.DecimalField(
        null=True,
        blank=True,
        max_digits=5,
        decimal_places=2
    )

    class Meta: # pylint: disable=too-few-public-methods
        """
        Docstring for Meta class to add constraints.
        """
        constraints = [
            models.UniqueConstraint(
                fields=["dietmetrics_user", "date"],
                name="unique_user_date_metric"
            ),
            models.CheckConstraint(
                condition=models.Q(calories__gt=0),
                name="calories_positive"
            ),
            models.CheckConstraint(
                condition=models.Q(weight__gt=0),
                name="weight_positive"
            ),
            models.CheckConstraint(
                condition=models.Q(activity_expenditure__gte=0),
                name="activity_expenditure_non_negative"
            )
        ]
