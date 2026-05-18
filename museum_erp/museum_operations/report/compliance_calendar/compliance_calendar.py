import frappe
from frappe import _
from frappe.utils import today, date_diff

def execute(filters=None):
    columns = [
        {"label": _("Obligation"), "fieldname": "obligation_type", "fieldtype": "Data", "width": 220},
        {"label": _("Due Date"), "fieldname": "due_date", "fieldtype": "Date", "width": 110},
        {"label": _("Days Left"), "fieldname": "days_left", "fieldtype": "Int", "width": 90},
        {"label": _("Responsible"), "fieldname": "responsible_person", "fieldtype": "Link",
         "options": "User", "width": 150},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]
    items = frappe.get_all("Compliance Tracker",
        fields=["name","obligation_type","due_date","responsible_person","status"],
        filters={"status": ["in", ["Pending","Overdue"]]},
        order_by="due_date asc")
    data = []
    for item in items:
        days = date_diff(str(item.due_date), today()) if item.due_date else 0
        data.append({**item, "days_left": days})
    return columns, data
