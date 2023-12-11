# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sanitary_code_ids = fields.One2many('sanitary.code', 'manufacturer_id', string='Reg. sanitarios',
                                        store=True, copy=False)