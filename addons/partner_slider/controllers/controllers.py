# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerSlider(http.Controller):
#     @http.route('/partner_slider/partner_slider', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_slider/partner_slider/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_slider.listing', {
#             'root': '/partner_slider/partner_slider',
#             'objects': http.request.env['partner_slider.partner_slider'].search([]),
#         })

#     @http.route('/partner_slider/partner_slider/objects/<model("partner_slider.partner_slider"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_slider.object', {
#             'object': obj
#         })

