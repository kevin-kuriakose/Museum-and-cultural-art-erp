import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("School"), "fieldname": "school_name", "fieldtype": "Data", "width": 200},
        {"label": _("Grade"), "fieldname": "grade_level", "fieldtype": "Data", "width": 100},
        {"label": _("Students"), "fieldname": "student_count", "fieldtype": "Int", "width": 90},
        {"label": _("Visit Date"), "fieldname": "visit_date", "fieldtype": "Date", "width": 110},
        {"label": _("Program"), "fieldname": "program_booked", "fieldtype": "Link",
         "options": "Education Program", "width": 180},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 90},
    ]
    data = frappe.get_all("School Visit",
        fields=["name","school_name","grade_level","student_count",
                "visit_date","program_booked","status"],
        order_by="visit_date desc")
    return columns, data
