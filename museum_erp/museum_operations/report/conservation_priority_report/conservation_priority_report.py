import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Artifact"), "fieldname": "artifact", "fieldtype": "Link",
         "options": "Artifact", "width": 160},
        {"label": _("Title"), "fieldname": "artifact_title", "fieldtype": "Data", "width": 200},
        {"label": _("Condition"), "fieldname": "condition_rating", "fieldtype": "Data", "width": 100},
        {"label": _("Priority"), "fieldname": "priority", "fieldtype": "Data", "width": 90},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": _("Next Exam"), "fieldname": "next_examination_date", "fieldtype": "Date", "width": 120},
        {"label": _("Examiner"), "fieldname": "examiner_name", "fieldtype": "Data", "width": 150},
    ]
    data = frappe.db.sql("""
        SELECT cr.artifact, a.title as artifact_title,
               cr.condition_rating, cr.priority, cr.status,
               cr.next_examination_date, cr.examiner_name
        FROM `tabConservation Record` cr
        LEFT JOIN `tabArtifact` a ON a.name = cr.artifact
        WHERE cr.docstatus < 2
        ORDER BY FIELD(cr.priority,'Urgent','High','Medium','Low'),
                 FIELD(cr.condition_rating,'Critical','Poor','Fair','Good','Excellent')
    """, as_dict=True)
    return columns, data
