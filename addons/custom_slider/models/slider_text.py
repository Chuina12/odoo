from odoo import models, fields

class SliderText(models.Model):
    _name = 'website.slider.text'
    _description = 'Texts for website slider'

    name = fields.Char(string='Text', required=True)
    sequence = fields.Integer(default=10)
