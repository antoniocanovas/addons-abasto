from odoo import _, api, fields, models
import datetime

import logging
_logger = logging.getLogger(__name__)


class PurchaseBillUnion(models.Model):
    _inherit = 'purchase.bill.union'

    picking_date = fields.Date('Picking date', related='purchase_order_id.picking_date')

    def name_get(self):
        result = []
        for doc in self:
            name = doc.name or ''
            if doc.reference:
                name += ' - ' + doc.reference
            if doc.picking_date:
                date_inv_dt = datetime.datetime.strftime(doc.picking_date, '%d/%m/%Y')
                name += ': ' + str(date_inv_dt)

            result.append((doc.id, name))
        return result