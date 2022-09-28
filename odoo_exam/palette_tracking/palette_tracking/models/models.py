from odoo import models, fields, api

class Palette_tracking(models.Model):
    _name = 'Palette_tracking'

    picking_id = fields.Many2one('stock.picking', required=True)
    partner_id = fields.Many2one('res.partner', default=lambda self: self.env['res.partner'])
    license_plate = fields.Char()
    picking_partner_id = fields.Many2one('res.partner')
    picking_date_done = fields.Datetime()
    palette_count_plus = fields.Integer()
    palette_count_minus = fields.Integer()
    balance = fields.Integer(compute='_compute_balance')

    @api.depends('palette_count_plus', 'palette_count_minus')
    def _compute_balance(self):
        for record in self:
            record.balance = record.palette_count_plus - record.palette_count_minus

    def open_field(self):
        return {
            'name': 'information',
            'view_mode': 'tree',
            'res_model': 'Palette_tracking',
            'type': 'ir.actions.act_window',
            'domain': [('partner_id', '=', self.id)]
        }