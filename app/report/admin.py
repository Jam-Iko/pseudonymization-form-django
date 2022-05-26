from django.contrib import admin
from report.models import ReportConnectionsModel, ReportFilesModel, ReportModel

admin.site.register(ReportConnectionsModel)
admin.site.register(ReportFilesModel)
admin.site.register(ReportModel)