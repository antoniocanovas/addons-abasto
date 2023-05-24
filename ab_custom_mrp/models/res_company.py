# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    reg_sanitario = fields.Char('Registro sanitario', store=True)
    aut_sanitaria = fields.Char('Autorización sanitaria', store=True)
