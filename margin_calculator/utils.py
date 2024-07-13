import frappe

def calculate_margin(doc, method):
    for item in doc.items:
        # Get the customer document
        customer = frappe.get_doc("Customer", doc.customer)
        
        # Check if the custom_client_margin_rate field exists and has a value
        if hasattr(customer, "custom_client_margin_rate") and customer.custom_client_margin_rate:
            try:
                # Convert custom_client_margin_rate to float
                margin_rate = float(customer.custom_client_margin_rate)
                # Retrieve the item valuation rate in the warehouse
                valuation_rate = frappe.db.get_value("Stock Ledger Entry", {
                    "item_code": item.item_code,
                    "warehouse": item.warehouse
                }, "valuation_rate")
                
                if valuation_rate:
                    # Calculate the new rate with margin
                    new_rate = valuation_rate * (1 + margin_rate / 100.0)
                    item.rate = new_rate
                    item.amount = item.qty * item.rate
            except ValueError:
                frappe.throw(f"Invalid custom_client_margin_rate for customer {customer.name}: {customer.custom_client_margin_rate}")
