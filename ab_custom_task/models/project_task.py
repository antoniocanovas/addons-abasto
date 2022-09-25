# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import api, fields, models, _

class ProjectTask(models.Model):
    _inherit = "project.task"

    def button_task_done(self):
        for record in self:
            state_done = self.env['project.task.type'].search([('is_closed','=',True),('id','in',record.project_id.type_ids.ids)])[0]
            if stage_done:
                record.stage_id = state_done.id
            # else mensaje "no hay etapa de cierre"
