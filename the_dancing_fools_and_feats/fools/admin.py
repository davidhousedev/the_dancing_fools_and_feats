from django.contrib import admin

from .models import DanceEvent, WeeklyEvent, MonthlyEvent, YearlyEvent


@admin.register(DanceEvent)
class DanceEventAdmin(admin.ModelAdmin):
    pass


@admin.register(WeeklyEvent)
class WeeklyDanceEventAdmin(admin.ModelAdmin):
    pass


@admin.register(MonthlyEvent)
class MonthlyDanceEventAdmin(admin.ModelAdmin):
    pass


@admin.register(YearlyEvent)
class YearlyDanceEventAdmin(admin.ModelAdmin):
    pass
