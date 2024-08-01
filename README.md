# Odoo17
odoo 17 training
    sales_training:
This Odoo module adds a sales training model with the following features:
1. **Unique IDs:** Sets up a sequence for training records.
2. **Sale Order Field:** Adds a "First Name" field to sale orders.
3. **User Group:** Creates a "Training Team" group.
4. **Views:** Provides form and tree views for managing training records.
5. **Menu:** Adds a menu item for accessing the training records.
6. **Wizard:** Includes a wizard for creating new training records.
- **SaleOrder:** Adds a "First Name" field.
- **SalesTrainingModel:** Manages training records with fields like first name, last name, and amount. Includes methods for creating records and state management.
- **TrainingWizard:** A wizard for creating training records.

    purchase_enhancement:
This Odoo module enhances purchase requests with these features:

1. **Purchase Request Model:**
   - Manages purchase requests with fields for name, requester, dates, order lines, total price, and state.
   - Handles state transitions (draft, to approve, approved, rejected, cancelled) and validations.
   - Automatically generates request names using a sequence.
2. **Purchase Request Line Model:** Manages order lines with product, quantity, cost price, and total.
3. **XML Views:**
   - Form and tree views for managing purchase requests.
   - Buttons for submitting, approving, rejecting, and resetting requests.
   - Rejection wizard to provide a rejection reason.
