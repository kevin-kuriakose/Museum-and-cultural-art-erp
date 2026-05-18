import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("Venue"), "fieldname": "venue_name", "fieldtype": "Data", "width": 160},
        {"label": _("Bookings"), "fieldname": "bookings", "fieldtype": "Int", "width": 100},
        {"label": _("Revenue (Rs)"), "fieldname": "revenue", "fieldtype": "Currency", "width": 130},
        {"label": _("Confirmed"), "fieldname": "confirmed", "fieldtype": "Int", "width": 100},
        {"label": _("Cancelled"), "fieldname": "cancelled", "fieldtype": "Int", "width": 100},
    ]
    data = frappe.db.sql("""
        SELECT venue_name,
               COUNT(name) as bookings,
               SUM(hire_fee) as revenue,
               SUM(CASE WHEN status='Confirmed' THEN 1 ELSE 0 END) as confirmed,
               SUM(CASE WHEN status='Cancelled' THEN 1 ELSE 0 END) as cancelled
        FROM `tabVenue Hire`
        WHERE docstatus < 2
        GROUP BY venue_name
        ORDER BY bookings DESC
    """, as_dict=True)
    return columns, data
