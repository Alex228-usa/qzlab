from odoo import models, fields, api


class Ninja(models.Model):
    _name = 'module_ninja.teacher'
    _description = 'our ninja way'

    name = fields.Char(string='Name', required=True)
    salary = fields.Float(string='Salary', digits=(8, 2),
                          required=True, default=0.0)

    shinobi_ids = fields.One2many('module_ninja.subject', 'ninja _id', string='Subjects')
    academia_id = fields.Many2one('module_ninja.academia', string='Academia')

    total_num_of_shinobi = fields.Integer(string='Total number of shinobi for academia',
                                           compute='_total_shinobi')

                teacher.avg_students = 0
