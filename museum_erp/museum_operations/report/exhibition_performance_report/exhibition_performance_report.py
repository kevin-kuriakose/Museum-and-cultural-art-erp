import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("Exhibition"), "fieldname": "title", "fieldtype": "Link",
         "options": "Exhibition", "width": 200},
        {"label": _("Type"), "fieldname": "exhibition_type", "fieldtype": "Data", "width": 100},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": _("Expected"), "fieldname": "expected_visitors", "fieldtype": "Int", "width": 100},
        {"label": _("Actual"), "fieldname": "actual_visitors", "fieldtype": "Int", "width": 100},
        {"label": _("Budget (Rs)"), "fieldname": "budget", "fieldtype": "Currency", "width": 120},
        {"label": _("Expenditure (Rs)"), "fieldname": "expenditure", "fieldtype": "Currency", "width": 130},
        {"label": _("Avg Feedback"), "fieldname": "avg_feedback", "fieldtype": "Float", "width": 120},
    ]
    exhibitions = frappe.get_all("Exhibition",
        fields=["name","title","exhibition_type","status","expected_visitors",
                "actual_visitors","budget","expenditure"],
        order_by="start_date desc")
    data = []
    for e in exhibitions:
        avg = frappe.db.sql("""
            SELECT AVG(CAST(overall_rating AS DECIMAL))
            FROM `tabVisitor Feedback`
            WHERE exhibition_visited = %s AND docstatus < 2
        """, e.name)[0][0]
        data.append({**e, "avg_feedback": round(flt(avg), 2) if avg else 0})
    return columns, data
