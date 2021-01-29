
from odoo import fields, models,api

class paquetes(models.Model):
	_inherit = 'product.packaging'

	Descuento = fields.Integer(string = "Descuento Pack", store=True)






