from odoo import models, fields, api


class Academia(models.Model):
    _name = 'modele_ninja.academia'
    _description = 'ninja academia'

    name = fields.Char(string='Name', required=True)

    shinobi_ids = fields.One2many('module_ninja.shinobi', 'academia_id', string='Shinoni')
    ninja_ids = fields.One2many('module_ninja.ninja', 'academia_id', string='Ninja')

    avg_ninja_salary = fields.Float(compute='_avg_salary', string='avg salary among ninja for academia',
                                      digits=(8,2), default=0.0, store=True)

    @api.depends('ninja_ids.salary')
    def _avg_salary(self):
        for academia in self:
            ninja = academia.ninja_ids
            if ninja:
                salary = [teach.salary for teach in ninja]
                academia.avg_ninja_salary = sum(salary) / len(salary)
