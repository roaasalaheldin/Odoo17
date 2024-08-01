from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    dimension = fields.Char(string='Dimension')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dimension = fields.Char(string='Dimension', related='product_id.dimension', store=True)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                moves = self.env['stock.move'].search([('sale_line_id', '=', line.id)])
                moves.write({'dimension': line.dimension})


class StockMove(models.Model):
    _inherit = 'stock.move'

    dimension = fields.Char(string='Dimension', store=True, readonly=False)


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    dimension = fields.Char(string='Dimension')


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        res = super(AccountMove, self).create(vals)
        if res.move_type in ['out_invoice', 'out_refund']:  # Ensure it's a customer invoice or refund
            for line in res.invoice_line_ids:
                sale_line = line.sale_line_ids[:1]
                if sale_line:
                    stock_move = self.env['stock.move'].search([('sale_line_id', '=', sale_line.id)], limit=1)
                    line.dimension = stock_move.dimension
        return res
