# Copyright 2023 IC - Antonio Cánovas
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    sanitary_code_ids = fields.Many2one('sanitary.code', string='Reg. sanitario', store=True, copy=True)
    manufacturer_id = fields.Many2one('res.partner', string='Manufacturer', store=True, copy=True)
