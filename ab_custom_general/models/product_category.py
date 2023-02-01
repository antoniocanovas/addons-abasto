# Copyright 2022 Serincloud
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    company_id = fields.Many2one('res.company', string='Company', store=True)
