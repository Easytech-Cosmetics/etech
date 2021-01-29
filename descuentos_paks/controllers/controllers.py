# -*- coding: utf-8 -*-
# from odoo import http


# class DescuentosPaquetes(http.Controller):
#     @http.route('/descuentos_paquetes/descuentos_paquetes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/descuentos_paquetes/descuentos_paquetes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('descuentos_paquetes.listing', {
#             'root': '/descuentos_paquetes/descuentos_paquetes',
#             'objects': http.request.env['descuentos_paquetes.descuentos_paquetes'].search([]),
#         })

#     @http.route('/descuentos_paquetes/descuentos_paquetes/objects/<model("descuentos_paquetes.descuentos_paquetes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('descuentos_paquetes.object', {
#             'object': obj
#         })
