"""
Configuration management for the Dietmetrics Django app.

This module exposes a settings proxy object that reads configuration values
from the Django project settings, falling back to default values when not defined.
"""

from django.conf import settings


class DietmetricsSettings: # pylint: disable=too-few-public-methods
    """
    Proxy object for Dietmetrics settings.

    Reads values from Django settings using the `DIETMETRICS_` prefix and falls
    back to internal defaults if not defined.
    """

    DEFAULTS = {
        "MAINTENANCE_PERIOD_DAYS": 14,
    }

    def __getattr__(self, name):
        if name not in self.DEFAULTS:
            raise AttributeError(name)

        return getattr(
            settings,
            f"DIETMETRICS_{name}",
            self.DEFAULTS[name],
        )


dietmetrics_settings = DietmetricsSettings()
