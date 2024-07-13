from odoo import models, fields

class SliderPage(models.Model):
    _name = 'website.slider.page'
    _description = 'Slider Pages'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Image')
    text_ids = fields.Many2many('website.slider.text', string='Slider Texts')
