from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SalesTrainingModel(models.Model):
    _name = 'sales.training.model'
    _rec_name = 'first_name'

    student_id = fields.Char(string='Student ID')
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    additional_info = fields.Text(string="Additional Information")
    notes = fields.Text(string="Notes")
    amount = fields.Integer(string='Enter Amount')
    change_value = fields.Char(string="Change Value")
    is_boolean = fields.Boolean(compute="_compute_is_boolean", store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', readonly=True, default='draft')

    @api.model_create_multi
    def create(self, vals_list):
        res = super(SalesTrainingModel, self).create(vals_list)
        for record in res:
            record.student_id = self.env['ir.sequence'].next_by_code('sales.training.model') or _('New')
        return res

    @api.depends('amount')
    def _compute_is_boolean(self):
        for rec in self:
            rec.is_boolean = self.env.user.has_group('sales_training.training_team_group') and rec.amount == 100

    @api.onchange('change_value')
    def _onchange_change_value(self):
        for rec in self:
            rec.amount = rec.change_value

    @api.constrains('amount')
    def _check_amount(self):
        for record in self:
            if record.amount > 100:
                raise ValidationError("The amount cannot be more than 100.")

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_reset_to_draft(self):
        self.state = 'draft'
