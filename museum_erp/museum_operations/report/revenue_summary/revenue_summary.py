import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Month"), "fieldname": "month", "fieldtype": "Data", "width": 120},
        {"label": _("Ticketing (Rs)"), "fieldname": "ticketing", "fieldtype": "Currency", "width": 130},
        {"label": _("Membership (Rs)"), "fieldname": "membership", "fieldtype": "Currency", "width": 130},
        {"label": _("Donations (Rs)"), "fieldname": "donations", "fieldtype": "Currency", "width": 130},
        {"label": _("Venue Hire (Rs)"), "fieldname": "venue_hire", "fieldtype": "Currency", "width": 130},
        {"label": _("Shop (Rs)"), "fieldname": "shop", "fieldtype": "Currency", "width": 130},
        {"label": _("Total (Rs)"), "fieldname": "total", "fieldtype": "Currency", "width": 130},
    ]
    year = filters.get("year") or frappe.utils.nowdate()[:4]
    ticketing = {r.month: flt(r.amount) for r in frappe.db.sql(
        "SELECT DATE_FORMAT(visit_date,'%%Y-%%m') as month, SUM(total_price) as amount FROM `tabTicket` WHERE docstatus=1 AND YEAR(visit_date)=%s GROUP BY month", year, as_dict=True)}
    donations = {r.month: flt(r.amount) for r in frappe.db.sql(
        "SELECT DATE_FORMAT(donation_date,'%%Y-%%m') as month, SUM(amount) as amount FROM `tabDonation` WHERE docstatus=1 AND YEAR(donation_date)=%s GROUP BY month", year, as_dict=True)}
    memberships = {r.month: flt(r.amount) for r in frappe.db.sql(
        "SELECT DATE_FORMAT(renewal_date,'%%Y-%%m') as month, SUM(amount_paid) as amount FROM `tabMembership Renewal` WHERE docstatus=1 AND YEAR(renewal_date)=%s GROUP BY month", year, as_dict=True)}
    venue = {r.month: flt(r.amount) for r in frappe.db.sql(
        "SELECT DATE_FORMAT(event_date,'%%Y-%%m') as month, SUM(hire_fee) as amount FROM `tabVenue Hire` WHERE docstatus=1 AND YEAR(event_date)=%s GROUP BY month", year, as_dict=True)}
    shop = {r.month: flt(r.amount) for r in frappe.db.sql(
        "SELECT DATE_FORMAT(sale_date,'%%Y-%%m') as month, SUM(total) as amount FROM `tabShop Sale` WHERE docstatus=1 AND YEAR(sale_date)=%s GROUP BY month", year, as_dict=True)}
    months = sorted(set(list(ticketing)+list(donations)+list(memberships)+list(venue)+list(shop)))
    data = []
    for m in months:
        t = ticketing.get(m,0); d = donations.get(m,0)
        mem = memberships.get(m,0); v = venue.get(m,0); s = shop.get(m,0)
        data.append({"month": m, "ticketing": t, "membership": mem,
                     "donations": d, "venue_hire": v, "shop": s,
                     "total": t+mem+d+v+s})
    return columns, data
