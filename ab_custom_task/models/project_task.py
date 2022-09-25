# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import api, fields, models, _

class ProjectTask(models.Model):
    _inherit = "project.task"

    is_closed = fields.Boolean(store=True)

    def button_task_done(self):
        for record in self:
            state_done = self.env['project.task.type'].search([('is_closed','=',True),('id','in',record.project_id.type_ids.ids)])[0]
            if stage_done:
                record.stage_id = state_done.id
            # else mensaje "no hay etapa de cierre"

    def button_task_user_timesheet(self):
        for record in self:
            self.env['account.analytic.line'].create({'name': record.name,
                                                 'account_id': record.project_id.analytic_account_id.id,
                                                 'task_id': record.id,
                                                 'set_start_stop': True,
                                                 'employee_id': record.user_id.employee_id.id,
                                                 'user_id': record.user_id.id})
