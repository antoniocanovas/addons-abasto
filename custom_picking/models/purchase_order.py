from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    picking_date = fields.Date(string='Picking Date')

    @api.depends('name', 'partner_ref', 'picking_date')
    def name_get(self):
        
        result = []
        for po in self:
            name = po.name
            if po.partner_ref:
                name += ' (' + po.partner_ref + ')'
            #if self.env.context.get('show_total_amount') and po.amount_total:
            #    name += ': ' + formatLang(self.env, po.amount_total, currency_obj=po.currency_id)
            if po.picking_date:
                name += str(po.picking_date)
            result.append((po.id, name))
        return result