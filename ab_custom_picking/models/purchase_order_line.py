from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    picking_date = fields.Date(string='Fecha albarán', store=True, related="order_id.picking_date")
    partner_ref = fields.Char(string='Albarán', store=True, related="order_id.partner_ref")

