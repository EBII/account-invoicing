# -*- coding: utf-8 -*-
# © 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.addons.sale.tests.test_sale_common import TestSale
import datetime


class TestSaleTimesheetDescription(TestSale):

    def test_sale_timesheet_description_1111(self):
        """ Test invoice description  """
        self.SaleConfigSetting = self.env['sale.config.settings']
        inv_obj = self.env['account.invoice']
        # intial sale order
        prod_ts = self.env.ref('product.product_product_2')
        sale_order_vals = {
            'partner_id': self.partner.id,
            'partner_invoice_id': self.partner.id,
            'partner_shipping_id': self.partner.id,
            'pricelist_id': self.env.ref('product.list0').id,
            'timesheet_invoice_description': '1111',
            'order_line': [(0, 0, {
                'name': prod_ts.name,
                'product_id': prod_ts.id,
                'product_uom_qty': 5,
                'product_uom': prod_ts.uom_id.id,
                'price_unit': prod_ts.list_price})],
        }
        sale_order = self.env['sale.order'].create(sale_order_vals)
        sale_order.action_confirm()
        # let's log some timesheets
        self.env['account.analytic.line'].create({
            'name': 'Test description 1234567890',
            'account_id': sale_order.project_id.id,
            'unit_amount': 10.5,
            'user_id': self.manager.id,
            'is_timesheet': True,
        })
        invoice_id = sale_order.with_context(
            timesheet_description=True
        ).action_invoice_create()
        invoice = inv_obj.browse(invoice_id)

        description = invoice.invoice_line_ids[0].name
        date = datetime.date.today()
        self.assertIn('Support Contract (on timesheet)\n'+str(date) + ' - ' +
                      '10.5 Hour(s) - Test description 1234567890' +
                      ' - Andrew Manager',
                      description)

        self.default_timesheet_invoice_description = (
            self.SaleConfigSetting.create({}))

        self.default_timesheet_invoice_description.execute()

    #
    # def test_sale_timesheet_description_1011(self):
    #     """ Test invoice description  """
    #     self.SaleConfigSetting = self.env['sale.config.settings']
    #     inv_obj = self.env['account.invoice']
    #     # intial sale order
    #     prod_ts = self.env.ref('product.product_product_2')
    #     sale_order_vals = {
    #         'partner_id': self.partner.id,
    #         'partner_invoice_id': self.partner.id,
    #         'partner_shipping_id': self.partner.id,
    #         'pricelist_id': self.env.ref('product.list0').id,
    #         'timesheet_invoice_description': '1011',
    #         'order_line': [(0, 0, {
    #             'name': prod_ts.name,
    #             'product_id': prod_ts.id,
    #             'product_uom_qty': 5,
    #             'product_uom': prod_ts.uom_id.id,
    #             'price_unit': prod_ts.list_price})],
    #     }
    #     sale_order = self.env['sale.order'].create(sale_order_vals)
    #     sale_order.action_confirm()
    #     # let's log some timesheets
    #     self.env['account.analytic.line'].create({
    #         'name': 'Test description 1234567890',
    #         'account_id': sale_order.project_id.id,
    #         'unit_amount': 11.5,
    #         'user_id': self.manager.id,
    #         'is_timesheet': True,
    #     })
    #     invoice_id = sale_order.with_context(
    #         timesheet_description=True
    #     ).action_invoice_create()
    #     invoice = inv_obj.browse(invoice_id)
    #
    #     description = invoice.invoice_line_ids[0].name
    #     date = datetime.date.today()
    #     self.assertIn('Support Contract (on timesheet)\n'+
    #     '- 11.5 Hour(s) - Test description 1234567890 - Andrew Manager',
    #       description)
    #
    #     self.default_timesheet_invoice_description = (
    #         self.SaleConfigSetting.create({}))
    #
    #     self.default_timesheet_invoice_description.execute()
    #
    # def test_sale_timesheet_description_0111(self):
    #         """ Test invoice description  """
    #         self.SaleConfigSetting = self.env['sale.config.settings']
    #         inv_obj = self.env['account.invoice']
    #         # intial sale order
    #         prod_ts = self.env.ref('product.product_product_2')
    #         sale_order_vals = {
    #             'partner_id': self.partner.id,
    #             'partner_invoice_id': self.partner.id,
    #             'partner_shipping_id': self.partner.id,
    #             'pricelist_id': self.env.ref('product.list0').id,
    #             'timesheet_invoice_description': '0111',
    #             'order_line': [(0, 0, {
    #                 'name': prod_ts.name,
    #                 'product_id': prod_ts.id,
    #                 'product_uom_qty': 5,
    #                 'product_uom': prod_ts.uom_id.id,
    #                 'price_unit': prod_ts.list_price})],
    #         }
    #         sale_order = self.env['sale.order'].create(sale_order_vals)
    #         sale_order.action_confirm()
    #         # let's log some timesheets
    #         self.env['account.analytic.line'].create({
    #             'name': 'Test description 1234567890',
    #             'account_id': sale_order.project_id.id,
    #             'unit_amount': 8.5,
    #             'user_id': self.manager.id,
    #             'is_timesheet': True,
    #         })
    #         invoice_id = sale_order.with_context(
    #             timesheet_description=True
    #         ).action_invoice_create()
    #         invoice = inv_obj.browse(invoice_id)
    #
    #         description = invoice.invoice_line_ids[0].name
    #         date = datetime.date.today()
    #         self.assertIn('Support Contract (on timesheet)\n'
    #          + str(date) +
    #          + ' - 8.5 Hour(s) - Test description 1234567890',
    #           description)
    #
    #         self.default_timesheet_invoice_description = (
    #             self.SaleConfigSetting.create({}))
    #
    #         self.default_timesheet_invoice_description.execute()
