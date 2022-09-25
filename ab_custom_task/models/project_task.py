# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import api, fields, models, _
from datetime import datetime, timedelta

class ProjectTask(models.Model):
    _inherit = "project.task"

    is_closed = fields.Boolean(store=True)

    @api.depends('timesheet_ids.date_time', 'timesheet_ids.unit_amount')
    def get_ab_started(self):
        for record in self:
            started = False
            for li in record.timesheet_ids:
                if li.date_time and not li.unit_amount:
                    started = True
        record.ab_started = started
    ab_started = fields.Boolean('Started', store=True, compute=get_ab_started)


    def button_start_work_ab(self):
        for record in self:
            hour_uom = self.env.ref("uom.product_uom_hour")
            self.env['account.analytic.line'].create({'name': record.name,
                                                 'account_id': record.project_id.analytic_account_id.id,
                                                 'task_id': record.id,
                                                 'employee_id': record.user_id.employee_id.id,
                                                 'product_uom_id': hour_uom.id,
                                                 'user_id': record.user_id.id})

    def button_end_work_ab(self):
        for record in self:
            for li in record.timesheet_ids:
                if li.date_time and not li.date_time_end:
                    li.unit_amount = ((datetime.now() - li.date_time).seconds / 3600)

    def button_task_done_ab(self):
        for record in self:
            if not record.timesheet_ids.ids:
                hour_uom = self.env.ref("uom.product_uom_hour")
                self.env['account.analytic.line'].create({'name': record.name,
                                                          'account_id': record.project_id.analytic_account_id.id,
                                                          'task_id': record.id,
                                                          'employee_id': record.user_id.employee_id.id,
                                                          'product_uom_id': hour_uom.id,
                                                          'user_id': record.user_id.id,
                                                          })
            for li in record.timesheet_ids:
                if li.date_time and not li.date_time_end:
                    li.unit_amount = ((datetime.now() - li.date_time).seconds / 3600)

            stage_done = self.env['project.task.type'].search([('is_closed','=',True),('id','in',record.project_id.type_ids.ids)])[0]
            if stage_done.id:
                record.stage_id = stage_done.id
            else:
                raise Warning("No hay etapa de cierre en este proyecto")
