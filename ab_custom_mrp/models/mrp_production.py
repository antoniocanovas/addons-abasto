# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MrpBom(models.Model):
    _inherit = "mrp.production"

#    timesheet_ids = fields.One2many('account.analytic.line', 'mrp_id', string='Timesheets')
    group_id = fields.Many2one('mrp.bom.group', string='Tipo de trabajo')
#    bom_easy_id = fields.Many2one('mrp.bom', string='Receta')
    printed_expiration = fields.Date('Caducidad', store=True)
    # Nuevo campo para cambar fechas de SM de elaboraciones documentadas de forma tardía:
    elaboration_date = fields.Datetime('Fecha elaboración', store=True, copy=False)

    @api.onchange('elaboration_date')
    def _update_mrp_stock_move_date(self):
        for record in self:
            stockmoves = self.env['stock.move'].search([('production_id','=',record.id)])
            raise UserError(stockmoves)
            for sm in stockmoves:
                sm['date'] = record.elaboration_date

