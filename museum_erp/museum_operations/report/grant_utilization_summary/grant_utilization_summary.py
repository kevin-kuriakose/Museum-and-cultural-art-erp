import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("Grant"), "fieldname": "grant_title", "fieldtype": "Link",
         "options": "Grant", "width": 220},
        {"label": _("Granting Body"), "fieldname": "granting_body", "fieldtype": "Data", "width": 180},
        {"label": _("Amount (Rs)"), "fieldname": "amount", "fieldtype": "Currency", "width": 130},
        {"label": _("Spent (Rs)"), "fieldname": "total_spent", "fieldtype": "Currency", "width": 130},
        {"label": _("Balance (Rs)"), "fieldname": "balance", "fieldtype": "Currency", "width": 130},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": _("End Date"), "fieldname": "end_date", "fieldtype": "Date", "width": 110},
    ]
    grants = frappe.get_all("Grant",
        fields=["name","grant_title","granting_body","amount","status","end_date"])
    data = []
    for g in grants:
        spent = frappe.db.sql("""
            SELECT SUM(total_spent) FROM `tabGrant Utilization Report`
            WHERE grant = %s AND docstatus < 2
        """, g.name)[0][0] or 0
        data.append({**g, "total_spent": flt(spent),
                     "balance": flt(g.amount) - flt(spent)})
    return columns, data
