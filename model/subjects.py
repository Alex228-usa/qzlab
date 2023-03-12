from odoo import models, fields


class Subject(models.Model):
    _name = 'module_ninja.subject'
    _description = 'academia subjects'

    name = fields.Char(string='Name', required=True)
    shinobi_ids = fields.Many2many('module_ninja.shinobi', string='Shinobi')
    ninja_id = fields.Many2one('module_ninja.teacher', string='Ninja')
