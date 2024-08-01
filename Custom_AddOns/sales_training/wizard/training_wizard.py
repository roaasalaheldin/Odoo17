from odoo import models, fields, api


class TrainingWizard(models.TransientModel):
    _name = 'training.wizard'
    _description = 'Training Wizard'

    name = fields.Char(string="Name", required=True)
    salary = fields.Float(string="Salary", required=True)

    def action_confirm(self):
        training = self.env['sales.training.model']
        for train in self:
            training.create({
                'first_name': train.name,
                'amount': train.salary,
            })
