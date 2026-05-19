import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Date"), "fieldname": "visit_date", "fieldtype": "Date", "width": 120},
        {"label": _("Exhibition"), "fieldname": "exhibition", "fieldtype": "Link",
         "options": "Exhibition", "width": 180},
        {"label": _("Ticket Type"), "fieldname": "ticket_type", "fieldtype": "Data", "width": 150},
        {"label": _("Tickets"), "fieldname": "total_tickets", "fieldtype": "Int", "width": 100},
        {"label": _("Visitors"), "fieldname": "total_visitors", "fieldtype": "Int", "width": 100},
        {"label": _("Revenue (Rs)"), "fieldname": "revenue", "fieldtype": "Currency", "width": 130},
    ]
    data = frappe.db.sql("""
        SELECT
            t.visit_date,
            t.exhibition,
            t.ticket_type,
            COUNT(t.name) as total_tickets,
            SUM(t.quantity) as total_visitors,
            SUM(t.total_price) as revenue
        FROM `tabTicket` t
        WHERE t.docstatus < 2
        {date_filter}
        GROUP BY t.visit_date, t.exhibition, t.ticket_type
        ORDER BY t.visit_date DESC
    """.format(
        date_filter="AND t.visit_date BETWEEN %(from_date)s AND %(to_date)s"
        if filters.get("from_date") and filters.get("to_date") else ""
    ), filters, as_dict=True)
    return columns, data
