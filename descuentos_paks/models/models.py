
from odoo import fields, models,api,exceptions


class Partner(models.Model):
	_inherit = 'sale.order.line'

	
	Pruebas = fields.Many2one(
		comodel_name = 'product.packaging',
		string='Paquetes',
		domain="[('product_id','=',product_id)]" #filtrado del campo selección.. segundo campo no literal #
		)

	cantidad = fields.Float('Cantidad_paquete', related='Pruebas.qty',compute = '_ModCantidad',store=True)
	Descuento_paquete = fields.Integer('Descuento %', related='Pruebas.Descuento', store=True)
	
	@api.onchange('cantidad')
	def _ModCantidad(self):
		self.product_uom_qty = self.cantidad
		self.discount = self.Descuento_paquete #igualamos el cmapo descuento estandar al nuestro y ocultamos el estandar... la logica la ejecuta el campo estandar oculto
		

	#nota: no perder la indentación.... dejará de aplicar la función.
	@api.onchange('product_uom_qty')
	def _Error_cantidad(self):
		if self.cantidad != 0:
			if self.product_uom_qty % self.cantidad != 0:
				raise exceptions.UserError('La cantidad debe ser múltiplo, revise empaquetado')



	



# class descuentos_paquetes(models.Model):
#     _name = 'descuentos_paquetes.descuentos_paquetes'
#     _description = 'descuentos_paquetes.descuentos_paquetes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
