# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None
from io import BytesIO

from odoo import models, fields, api, _, SUPERUSER_ID
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    ingrediente  = fields.Text('Ingredientes', store=True)
    conservante = fields.Text('Conservantes y colorantes', store=True)
    alergeno    = fields.Text('Alérgenos', store=True)
    consumo    = fields.Char('Consumo', store=True)
    conservacion = fields.Char('Conservacion', store=True)
    qr_url = fields.Char('Url QR', store=True)

    @api.depends('qr_url', 'write_date')
    def generate_qr(self):
        if qrcode and base64:
#            if not self.sequence:
#                prefix = str(self.env['ir.config_parameter'].sudo().get_param(
#                    'customer_product_qr.config.customer_prefix'))
#                if not prefix:
#                    raise UserError(
#                        _('Set A Customer Prefix In General Settings'))
#                self.sequence = prefix + self.env['ir.sequence'].next_by_code(
#                    'res.partner') or '/'
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.qr_url)
            qr.make(fit=True)

            img = qr.make_image()
            temp = BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            self.qr_image = qr_image
#            return self.env.ref(
#                'customer_product_qrcode.print_qr').report_action(self, data={
#                'data': self.id, 'type': 'cust'})
        else:
            raise UserError(
                _('Necessary Requirements To Run This Operation Is Not Satisfied'))
    qr_image = fields.Binary('QR Image', store=True)
