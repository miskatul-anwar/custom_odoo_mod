from odoo import models, fields, api

class Customer(models.Model):
    _name = 'customer.management'
    _description = 'Customer Management'
    _rec_name = 'name'

    name = fields.Char(string='Customer Name', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    paid = fields.Float(string='Paid Amount', default=0.0)
    due = fields.Float(string='Due Amount', default=0.0, required=True)
    # Add frequency tracking for dashboard
    visit_count = fields.Integer(string='Visit Count', default=1)

    @api.model
    def create(self, vals):
        """Override create to handle initial due amount"""
        record = super(Customer, self).create(vals)
        # If due is 0 upon creation, don't create the record
        if record.due == 0:
            record.unlink()
            return False
        return record

    def write(self, vals):
        """Override write to auto-delete when due becomes 0 and increment visit count"""
        # Increment visit count when paid amount is updated
        if 'paid' in vals and vals['paid'] > 0:
            vals['visit_count'] = self.visit_count + 1

        result = super(Customer, self).write(vals)
        # Check if any record has due = 0 after update
        for record in self:
            if record.due == 0:
                record.unlink()
        return result

    @api.onchange('paid', 'due')
    def _onchange_payment(self):
        """Optional: Add validation or calculation logic here"""
        pass

    @api.model
    def get_dashboard_data(self):
        """Get data for dashboard"""
        # Get all customers
        all_customers = self.search([])

        # Best customers (most frequent visitors)
        best_customers = all_customers.sorted(key='visit_count', reverse=True)[:3]

        # Worst customers (highest due amounts)
        worst_customers = all_customers.sorted(key='due', reverse=True)[:3]

        # Total earnings
        total_earnings = sum(all_customers.mapped('paid'))

        return {
            'best_customers': best_customers,
            'worst_customers': worst_customers,
            'total_earnings': total_earnings,
        }
