from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def get_list_price_taxed(self):
        for record in self:
            price, taxes = record.list_price, 0
            for tax in record.taxes_id:
                if tax.amount_type == 'percent':
                    taxes += tax.amount / 100 * price
            record['list_price_taxed'] = price + taxes

    list_price_taxed = fields.Monetary('List price with tax',
                                       readonly=False,
                                       compute='get_list_price_taxed')
