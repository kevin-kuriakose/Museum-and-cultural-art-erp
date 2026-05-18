import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("Volunteer"), "fieldname": "volunteer", "fieldtype": "Link",
         "options": "Volunteer", "width": 180},
        {"label": _("Role"), "fieldname": "role", "fieldtype": "Data", "width": 150},
        {"label": _("Total Hours"), "fieldname": "total_hours", "fieldtype": "Float", "width": 120},
        {"label": _("Assignments"), "fieldname": "assignments", "fieldtype": "Int", "width": 110},
    ]
    data = frappe.db.sql("""
        SELECT volunteer, role,
               SUM(hours) as total_hours,
               COUNT(name) as assignments
        FROM `tabVolunteer Assignment`
        WHERE docstatus < 2 AND status = 'Completed'
        GROUP BY volunteer, role
        ORDER BY total_hours DESC
    """, as_dict=True)
    return columns, data
