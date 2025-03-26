# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountReport(models.Model):
    _inherit = "account.report"

    #  FILTERS =======================================================================================================================================
    # Those fields control the display of menus on the report

    filter_account = fields.Boolean(
        string="Accounts",
        compute=lambda x: x._compute_report_option_filter('filter_account'), readonly=False, store=True,
        depends=['root_report_id', 'section_main_report_ids'],
    )

    def _init_options_account(self, options, previous_options=None):
        if not self.filter_account:
            return
        options['account'] = True
        previous_account_ids = previous_options and previous_options.get('account_ids') or []
        selected_account_ids = [int(partner) for partner in previous_account_ids]
        # search instead of browse so that record rules apply and filter out the ones the user does not have access to
        selected_accounts = selected_account_ids and self.env['account.account'].with_context(active_test=False).search(
            [('id', 'in', selected_account_ids)]) or self.env['res.partner']
        options['selected_account_ids'] = selected_accounts.mapped('name')
        options['account_ids'] = selected_accounts.ids

    @api.model
    def _get_options_account_domain(self, options):
        domain = []
        if options.get('account_ids'):
            account_ids = [int(account) for account in options['account_ids']]
            domain.append(('account_id', 'in', account_ids))
        return domain

    def _get_options_domain(self, options, date_scope):
        self.ensure_one()
        domain = super()._get_options_domain(options, date_scope)
        domain += self._get_options_account_domain(options)
        return domain
