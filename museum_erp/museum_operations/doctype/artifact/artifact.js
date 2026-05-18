frappe.ui.form.on("Artifact", {
    refresh(frm) {
        if (!frm.is_new()) {
            const color = frm.doc.condition === "Critical" ? "red" :
                          frm.doc.condition === "Poor" ? "orange" :
                          frm.doc.condition === "Fair" ? "yellow" : "green";
            frm.dashboard.add_indicator(
                __("Condition: {0}", [frm.doc.condition || "Unknown"]), color);
        }
        if (!frm.is_new() && frm.doc.status === "Active") {
            frm.add_custom_button(__("Add Location Record"), () => {
                frappe.new_doc("Artifact Location", {artifact: frm.doc.name});
            });
            frm.add_custom_button(__("Conservation Record"), () => {
                frappe.new_doc("Conservation Record", {artifact: frm.doc.name});
            });
        }
    }
});
