# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api, _

class SanitaryCode(models.Model):
    _name = 'sanitary.code'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sanitary Codes'

    name = fields.Char(string="Name", store=True, required=True, copy=False)
    product_tmpl_ids = fields.One2many('product.template', 'sanitary_code_id', string='Products', store=True, copy=False)
    manufacturer_id = fields.Many2one('res.partner', string='Manufacturer', store=True, required=True, copy=True)
    active = fields.Boolean('Active', store=True, copy=False, default=True)