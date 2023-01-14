from django.contrib import admin
from app1.models import DemandStatistics, GeographyStatistics, SkillsStatistics


admin.site.register(DemandStatistics)
admin.site.register(GeographyStatistics)
admin.site.register(SkillsStatistics)
