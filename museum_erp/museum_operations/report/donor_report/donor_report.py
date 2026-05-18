import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("Donor"), "fieldname": "name", "fieldtype": "Link",
         "options": "Donor", "width": 200},
        {"label": _("Type"), "fieldname": "donor_type", "fieldtype": "Data", "width": 120},
        {"label": _("Level"), "fieldname": "giving_level", "fieldtype": "Data", "width": 120},
        {"label": _("Cumulative (Rs)"), "fieldname": "cumulative_giving", "fieldtype": "Currency", "width": 140},
        {"label": _("Last Gift"), "fieldname": "last_gift_date", "fieldtype": "Date", "width": 110},
        {"label": _("80G Eligible"), "fieldname": "is_80g_eligible", "fieldtype": "Check", "width": 100},
    ]
    data = frappe.get_all("Donor",
        fields=["name","donor_type","giving_level","cumulative_giving",
                "last_gift_date","is_80g_eligible"],
        order_by="cumulative_giving desc")
    return columns, data
