# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    printed_lot = fields.Many2one('stock.production.lot', string='Lote', store=True)
    printed_expiration = fields.Date('Caducidad', store=True)




