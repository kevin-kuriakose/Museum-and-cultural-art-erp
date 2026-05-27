from . import __version__ as app_version

app_name = "museum_erp"
app_title = "MuseumEdge ERP"
app_publisher = "bizaxl"
app_description = "Full-suite ERP for Museums and Cultural Heritage Sites"
app_email = "admin@bizaxl.com"
app_license = "MIT"
app_version = "0.0.1"

required_apps = ["frappe", "erpnext"]

app_include_css = "/assets/museum_erp/css/museum_erp.css"
app_include_js = "/assets/museum_erp/js/museum_erp.js"

doc_events = {}
scheduler_events = {"daily": [], "weekly": []}
after_install = "museum_erp.install.after_install"

override_doctype_class = {
    # Phase 1
    "Artifact": "museum_erp.museum_operations.doctype.artifact.artifact.Artifact",
    "Artifact Location": "museum_erp.museum_operations.doctype.artifact_location.artifact_location.ArtifactLocation",
    "Artifact Provenance": "museum_erp.museum_operations.doctype.artifact_provenance.artifact_provenance.ArtifactProvenance",
    "Acquisition": "museum_erp.museum_operations.doctype.acquisition.acquisition.Acquisition",
    "Acquisition Item": "museum_erp.museum_operations.doctype.acquisition_item.acquisition_item.AcquisitionItem",
    "Deaccession": "museum_erp.museum_operations.doctype.deaccession.deaccession.Deaccession",
    # Phase 2
    "Conservation Record": "museum_erp.museum_operations.doctype.conservation_record.conservation_record.ConservationRecord",
    "Conservation Treatment": "museum_erp.museum_operations.doctype.conservation_treatment.conservation_treatment.ConservationTreatment",
    "Condition Report": "museum_erp.museum_operations.doctype.condition_report.condition_report.ConditionReport",
    "Exhibition": "museum_erp.museum_operations.doctype.exhibition.exhibition.Exhibition",
    "Exhibition Artifact": "museum_erp.museum_operations.doctype.exhibition_artifact.exhibition_artifact.ExhibitionArtifact",
    "Exhibition Label": "museum_erp.museum_operations.doctype.exhibition_label.exhibition_label.ExhibitionLabel",
    "Exhibition Label Language": "museum_erp.museum_operations.doctype.exhibition_label_language.exhibition_label_language.ExhibitionLabelLanguage",
    "Exhibition Tour": "museum_erp.museum_operations.doctype.exhibition_tour.exhibition_tour.ExhibitionTour",
    "Exhibition Curator": "museum_erp.museum_operations.doctype.exhibition_curator.exhibition_curator.ExhibitionCurator",
    "Exhibition Sponsor": "museum_erp.museum_operations.doctype.exhibition_sponsor.exhibition_sponsor.ExhibitionSponsor",
    "Traveling Exhibition": "museum_erp.museum_operations.doctype.traveling_exhibition.traveling_exhibition.TravelingExhibition",
    "Loan": "museum_erp.museum_operations.doctype.loan.loan.Loan",
    "Loan Artifact": "museum_erp.museum_operations.doctype.loan_artifact.loan_artifact.LoanArtifact",
    "Facility Report": "museum_erp.museum_operations.doctype.facility_report.facility_report.FacilityReport",
}

# Phase 3 additions
override_doctype_class.update({
    "Ticket Type": "museum_erp.museum_operations.doctype.ticket_type.ticket_type.TicketType",
    "Ticket": "museum_erp.museum_operations.doctype.ticket.ticket.Ticket",
    "Visitor": "museum_erp.museum_operations.doctype.visitor.visitor.Visitor",
    "Group Booking": "museum_erp.museum_operations.doctype.group_booking.group_booking.GroupBooking",
    "Visitor Feedback": "museum_erp.museum_operations.doctype.visitor_feedback.visitor_feedback.VisitorFeedback",
    "Membership Tier": "museum_erp.museum_operations.doctype.membership_tier.membership_tier.MembershipTier",
    "Membership Tier Benefit": "museum_erp.museum_operations.doctype.membership_tier_benefit.membership_tier_benefit.MembershipTierBenefit",
    "Member": "museum_erp.museum_operations.doctype.member.member.Member",
    "Member Benefit": "museum_erp.museum_operations.doctype.member_benefit.member_benefit.MemberBenefit",
    "Member Payment": "museum_erp.museum_operations.doctype.member_payment.member_payment.MemberPayment",
    "Membership Renewal": "museum_erp.museum_operations.doctype.membership_renewal.membership_renewal.MembershipRenewal",
    "Donor": "museum_erp.museum_operations.doctype.donor.donor.Donor",
    "Donor Gift": "museum_erp.museum_operations.doctype.donor_gift.donor_gift.DonorGift",
    "Donation": "museum_erp.museum_operations.doctype.donation.donation.Donation",
    "Donation Campaign": "museum_erp.museum_operations.doctype.donation_campaign.donation_campaign.DonationCampaign",
})

# Phase 4 additions
override_doctype_class.update({
    "Education Program": "museum_erp.museum_operations.doctype.education_program.education_program.EducationProgram",
    "Program Session": "museum_erp.museum_operations.doctype.program_session.program_session.ProgramSession",
    "School Visit": "museum_erp.museum_operations.doctype.school_visit.school_visit.SchoolVisit",
    "Research Request": "museum_erp.museum_operations.doctype.research_request.research_request.ResearchRequest",
    "Workshop Booking": "museum_erp.museum_operations.doctype.workshop_booking.workshop_booking.WorkshopBooking",
    "Gallery": "museum_erp.museum_operations.doctype.gallery.gallery.Gallery",
    "Storage Room": "museum_erp.museum_operations.doctype.storage_room.storage_room.StorageRoom",
    "Venue Hire": "museum_erp.museum_operations.doctype.venue_hire.venue_hire.VenueHire",
    "Maintenance Request": "museum_erp.museum_operations.doctype.maintenance_request.maintenance_request.MaintenanceRequest",
    "Volunteer": "museum_erp.museum_operations.doctype.volunteer.volunteer.Volunteer",
    "Volunteer Skill": "museum_erp.museum_operations.doctype.volunteer_skill.volunteer_skill.VolunteerSkill",
    "Volunteer Assignment": "museum_erp.museum_operations.doctype.volunteer_assignment.volunteer_assignment.VolunteerAssignment",
    "Volunteer Timesheet": "museum_erp.museum_operations.doctype.volunteer_timesheet.volunteer_timesheet.VolunteerTimesheet",
    "Volunteer Timesheet Entry": "museum_erp.museum_operations.doctype.volunteer_timesheet_entry.volunteer_timesheet_entry.VolunteerTimesheetEntry",
    "Staff Training": "museum_erp.museum_operations.doctype.staff_training.staff_training.StaffTraining",
    "Shop Item": "museum_erp.museum_operations.doctype.shop_item.shop_item.ShopItem",
    "Shop Sale": "museum_erp.museum_operations.doctype.shop_sale.shop_sale.ShopSale",
    "Shop Sale Item": "museum_erp.museum_operations.doctype.shop_sale_item.shop_sale_item.ShopSaleItem",
    "Shop Purchase Order": "museum_erp.museum_operations.doctype.shop_purchase_order.shop_purchase_order.ShopPurchaseOrder",
    "Shop PO Item": "museum_erp.museum_operations.doctype.shop_po_item.shop_po_item.ShopPoItem",
    "Grant": "museum_erp.museum_operations.doctype.grant.grant.Grant",
    "Grant Budget Line": "museum_erp.museum_operations.doctype.grant_budget_line.grant_budget_line.GrantBudgetLine",
    "Grant Utilization Report": "museum_erp.museum_operations.doctype.grant_utilization_report.grant_utilization_report.GrantUtilizationReport",
    "Fundraising Event": "museum_erp.museum_operations.doctype.fundraising_event.fundraising_event.FundraisingEvent",
    "Fundraising Sponsor": "museum_erp.museum_operations.doctype.fundraising_sponsor.fundraising_sponsor.FundraisingSponsor",
    "Board Meeting": "museum_erp.museum_operations.doctype.board_meeting.board_meeting.BoardMeeting",
    "Board Agenda": "museum_erp.museum_operations.doctype.board_agenda.board_agenda.BoardAgenda",
    "Board Attendee": "museum_erp.museum_operations.doctype.board_attendee.board_attendee.BoardAttendee",
    "Policy Document": "museum_erp.museum_operations.doctype.policy_document.policy_document.PolicyDocument",
    "Compliance Tracker": "museum_erp.museum_operations.doctype.compliance_tracker.compliance_tracker.ComplianceTracker",
    "Insurance Policy": "museum_erp.museum_operations.doctype.insurance_policy.insurance_policy.InsurancePolicy",
    "Insurance Artifact": "museum_erp.museum_operations.doctype.insurance_artifact.insurance_artifact.InsuranceArtifact",
})

fixtures = [
    {"doctype": "Workspace", "filters": [["name", "in", ["MuseumEdge"]]]},
    {"doctype": "Notification", "filters": [["document_type", "in", [
        "Artifact", "Conservation Record", "Exhibition", "Member", "Loan",
        "Insurance Policy", "Venue Hire", "Shop Item", "Group Booking", "Donation"
    ]]]},
]
