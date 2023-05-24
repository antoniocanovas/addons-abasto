# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ingrediente  = fields.Text('Ingredientes', store=True)
    conservante = fields.Text('Conservantes y colorantes', store=True)
    alergeno    = fields.Text('Alérgenos', store=True)
    consumo    = fields.Char('Consumo', store=True)
    conservacion = fields.Char('Conservacion', store=True)
    qr_url = fields.Char('Url QR', store=True)


