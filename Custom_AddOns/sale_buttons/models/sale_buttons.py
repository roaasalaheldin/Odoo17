from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    so_type = fields.Selection([
        ('local', 'Local'),
        ('export', 'Export'),
    ], string='so type', default='local')

    state = fields.Selection(selection_add=[
        ('submit_approval', 'Submit for Approval'),
        ('first_approval', 'First Approval'),
        ('second_approval', 'Second Approval'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def action_submit_approval(self):
        self.state = 'submit_approval'

    def action_first_approval(self):
        self.state = 'first_approval'

    def _can_be_confirmed(self):
        self.ensure_one()
        return self.state in {'draft', 'sent', 'second_approval'}

    def action_second_approval(self):
        self.state = 'second_approval'
        if self.state == 'second_approval' and self.so_type == 'local':
            super(SaleOrder, self).action_confirm()



