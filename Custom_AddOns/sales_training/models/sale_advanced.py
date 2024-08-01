from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    text = fields.Char(string="First Name", required=True)
