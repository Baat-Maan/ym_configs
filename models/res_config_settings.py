# -*- coding: utf-8 -*-

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    save_jobsite = fields.Boolean(string='Save Jobsite To Beta', config_parameter='ym_configs.save_jobsite')
    jobsite_endpoint = fields.Char(string='Jobsite Beta Endpoint', config_parameter='ym_configs.jobsite_endpoint')

    save_customer = fields.Boolean(string='Save Customer To Beta', config_parameter='ym_configs.save_customer')
    customer_endpoint = fields.Char(string='Customer Beta Endpoint', config_parameter='ym_configs.customer_endpoint')

    save_customer_branch = fields.Boolean(string='Save Customer Branch To Beta',
                                          config_parameter='ym_configs.save_customer_branch')
    customer_branch_endpoint = fields.Char(string='Customer Beta Endpoint',
                                           config_parameter='ym_configs.customer_branch_endpoint')

    save_quotation = fields.Boolean(string='Save Quotation To Beta', config_parameter='ym_configs.save_quotation')
    quotation_endpoint = fields.Char(string='Quotation Beta Endpoint', config_parameter='ym_configs.quotation_endpoint')

    google_maps_api_key = fields.Char(string='Google Maps API Key', config_parameter='ym_configs.google_maps_api_key')

    rapid_sms_api_key = fields.Char(string='RapidSMSApi Key', config_parameter='ym_configs.rapid_sms_api_key')
    rapid_sms_url = fields.Char(string='RapidSMS Api Endpoint', config_parameter='ym_configs.rapid_sms_url')
    rapid_sms_sender = fields.Char(string='RapidSMS Sender', config_parameter='ym_configs.rapid_sms_sender')

    sales_head_contact = fields.Char(string='Sales Team Head', size=10,
                                     config_parameter='ym_configs.sales_head_contact')
    accounts_head_contact = fields.Char(string='Accounts Team Head', size=10,
                                        config_parameter='ym_configs.accounts_head_contact')
    ops_head_contact = fields.Char(string='Ops Team Head', size=10, config_parameter='ym_configs.ops_head_contact')

    sap_api_url = fields.Char(string='SAP API Endpoint', config_parameter='ym_configs.sap_api_url')
    sap_db = fields.Char(string='SAP DB', config_parameter='ym_configs.sap_db')
    sap_username = fields.Char(string='SAP Username', config_parameter='ym_configs.sap_username')
    sap_password = fields.Char(string='SAP Password', config_parameter='ym_configs.sap_password')
    sap_domain = fields.Char(string='SAP Domain', config_parameter='ym_configs.sap_domain')
