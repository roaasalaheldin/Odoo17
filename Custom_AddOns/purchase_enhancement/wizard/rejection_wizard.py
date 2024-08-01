from odoo import models, fields, api


class PurchaseRequestRejectWizard(models.TransientModel):
    _name = 'purchase.wizard'
    _description = 'Purchase Request Reject Wizard'

    purchase_request_id = fields.Many2one('purchase.request', string='Purchase Request')
    rejection_reason = fields.Text(string='Rejection Reason', required=True)

    def action_confirm(self):
        self.ensure_one()

        self.purchase_request_id.update({
            'state': 'reject',
            'rejection_reason': self.rejection_reason,
        })
        return {'type': 'ir.actions.act_window_close'}