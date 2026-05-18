import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Tier"), "fieldname": "membership_tier", "fieldtype": "Link",
         "options": "Membership Tier", "width": 150},
        {"label": _("Active"), "fieldname": "active", "fieldtype": "Int", "width": 80},
        {"label": _("Expired"), "fieldname": "expired", "fieldtype": "Int", "width": 80},
        {"label": _("Lapsed"), "fieldname": "lapsed", "fieldtype": "Int", "width": 80},
        {"label": _("Total"), "fieldname": "total", "fieldtype": "Int", "width": 80},
    ]
    tiers = frappe.get_all("Membership Tier", fields=["name"])
    data = []
    for tier in tiers:
        active = frappe.db.count("Member", {"membership_tier": tier.name, "status": "Active"})
        expired = frappe.db.count("Member", {"membership_tier": tier.name, "status": "Expired"})
        lapsed = frappe.db.count("Member", {"membership_tier": tier.name, "status": "Lapsed"})
        data.append({"membership_tier": tier.name, "active": active,
                     "expired": expired, "lapsed": lapsed,
                     "total": active + expired + lapsed})
    return columns, data
