from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    picking_date = fields.Date(string='Picking Date', related='purchase_id.picking_date')
