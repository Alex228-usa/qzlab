from odoo import models, fields, api


class Shinobi(models.Model):
    _name = 'module_ninja.shinobi'
    _description = 'shinobi way'

    name = fields.Char(string='Name', required=True)
    academia_id = fields.Many2one('module_ninja.academia', string='Academia')
    subject_ids = fields.Many2many('module_ninja.subject', string='Subject')
