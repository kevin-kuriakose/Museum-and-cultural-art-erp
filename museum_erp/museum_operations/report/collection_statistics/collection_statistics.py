import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Category"), "fieldname": "category", "fieldtype": "Data", "width": 200},
        {"label": _("Value"), "fieldname": "value", "fieldtype": "Data", "width": 200},
        {"label": _("Count"), "fieldname": "count", "fieldtype": "Int", "width": 100},
    ]
    data = []
    for row in frappe.db.sql("SELECT object_type as value, COUNT(*) as count FROM `tabArtifact` WHERE docstatus<2 GROUP BY object_type ORDER BY count DESC", as_dict=True):
        data.append({"category": "By Object Type", "value": row.value or "Unknown", "count": row.count})
    for row in frappe.db.sql("SELECT `condition` as value, COUNT(*) as count FROM `tabArtifact` WHERE docstatus<2 GROUP BY `condition`", as_dict=True):
        data.append({"category": "By Condition", "value": row.value or "Unknown", "count": row.count})
    for row in frappe.db.sql("SELECT acquisition_method as value, COUNT(*) as count FROM `tabArtifact` WHERE docstatus<2 GROUP BY acquisition_method", as_dict=True):
        data.append({"category": "By Acquisition Method", "value": row.value or "Unknown", "count": row.count})
    total = frappe.db.count("Artifact")
    data.insert(0, {"category": "Total Artifacts", "value": "All", "count": total})
    return columns, data
