# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    Antonio Cánovas antonio.canovas@serincloud.com
##############################################################################

{
    "name": "Task tree view for waiters",
    "version": "14.0.1.0.0",
    "category": "Project",
    "author": "www.serincloud.com",
    "maintainer": "Antonio Cánovas",
    "website": "www.serincloud.com",
    "license": "AGPL-3",
    "depends": [
        'project',
        'project_timesheet_time_control',
        'web_widget_open_tab',
    ],
    "data": [
        'views/project_task_views.xml'
    ],
    "installable": True,
}
