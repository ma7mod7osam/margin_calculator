app_name = "margin_calculator"
app_title = "Margin Calculator"
app_publisher = "Mahmood"
app_description = "App to calculate and apply margins on quotations, sales orders, and sales invoices"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ma7mod7osam@gmail.com"
app_license = "MIT"

doc_events = {
    "Quotation": {
        "before_insert": 
"margin_calculator.utils.calculate_margin"
    },
    "Sales Order": {
        "before_insert": 
"margin_calculator.utils.calculate_margin"
    },
    "Sales Invoice": {
        "before_insert": 
"margin_calculator.utils.calculate_margin"
    }
}

