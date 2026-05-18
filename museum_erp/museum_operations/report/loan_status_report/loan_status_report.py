import frappe
from frappe import _
from frappe.utils import today, date_diff

def execute(filters=None):
    columns = [
        {"label": _("Loan"), "fieldname": "name", "fieldtype": "Link",
         "options": "Loan", "width": 140},
        {"label": _("Type"), "fieldname": "loan_type", "fieldtype": "Data", "width": 90},
        {"label": _("Institution"), "fieldname": "borrower_lender_institution", "fieldtype": "Data", "width": 180},
        {"label": _("Start"), "fieldname": "loan_start_date", "fieldtype": "Date", "width": 100},
        {"label": _("End"), "fieldname": "loan_end_date", "fieldtype": "Date", "width": 100},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": _("Days Overdue"), "fieldname": "days_overdue", "fieldtype": "Int", "width": 110},
        {"label": _("Artifacts"), "fieldname": "artifact_count", "fieldtype": "Int", "width": 90},
    ]
    loans = frappe.get_all("Loan",
        fields=["name","loan_type","borrower_lender_institution",
                "loan_start_date","loan_end_date","status"],
        filters={"docstatus": 1, "status": ["in", ["Active","Overdue"]]})
    data = []
    for loan in loans:
        overdue = max(0, date_diff(today(), str(loan.loan_end_date))) if loan.loan_end_date else 0
        count = frappe.db.count("Loan Artifact", {"parent": loan.name})
        data.append({**loan, "days_overdue": overdue, "artifact_count": count})
    return columns, data
