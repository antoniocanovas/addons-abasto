from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    picking_date = fields.Date(string='Fecha albarán')

