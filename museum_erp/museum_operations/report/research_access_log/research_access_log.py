import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Request"), "fieldname": "name", "fieldtype": "Link",
         "options": "Research Request", "width": 140},
        {"label": _("Researcher"), "fieldname": "researcher_name", "fieldtype": "Data", "width": 180},
        {"label": _("Institution"), "fieldname": "institution", "fieldtype": "Data", "width": 180},
        {"label": _("Topic"), "fieldname": "research_topic", "fieldtype": "Data", "width": 200},
        {"label": _("Access Type"), "fieldname": "access_type", "fieldtype": "Data", "width": 110},
        {"label": _("Status"), "fieldname": "approval_status", "fieldtype": "Data", "width": 100},
        {"label": _("Start"), "fieldname": "start_date", "fieldtype": "Date", "width": 100},
    ]
    data = frappe.get_all("Research Request",
        fields=["name","researcher_name","institution","research_topic",
                "access_type","approval_status","start_date"],
        order_by="start_date desc")
    return columns, data
