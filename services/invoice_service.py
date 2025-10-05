# services/invoice_service.py

from database.models import Invoice
from database.db_utils import get_session

# 🧾 Create a new invoice
def create_invoice(user_id, invoice_data):
    """
    Save a new invoice to the database.

    Args:
        user_id (int): ID of the logged-in user.
        invoice_data (dict): Extracted invoice data like amount, date, vendor, etc.

    Returns:
        Invoice: The created invoice object.
    """
    session = get_session()
    try:
        new_invoice = Invoice(
            user_id=user_id,
            invoice_number=invoice_data.get("invoice_number"),
            vendor=invoice_data.get("vendor"),
            date=invoice_data.get("date"),
            total_amount=invoice_data.get("total_amount"),
            currency=invoice_data.get("currency"),
            description=invoice_data.get("description"),
            pdf_path=invoice_data.get("pdf_path")
        )
        session.add(new_invoice)
        session.commit()
        return new_invoice
    except Exception as e:
        session.rollback()
        print(f"❌ Error creating invoice: {e}")
        return None
    finally:
        session.close()


# 📜 Fetch all invoices for a specific user
def get_user_invoices(user_id):
    """
    Retrieve all invoices belonging to a user.
    """
    session = get_session()
    try:
        invoices = session.query(Invoice).filter_by(user_id=user_id).order_by(Invoice.date.desc()).all()
        return invoices
    except Exception as e:
        print(f"❌ Error fetching invoices: {e}")
        return []
    finally:
        session.close()


# 🔍 Get a single invoice by ID
def get_invoice_by_id(invoice_id):
    """
    Retrieve one invoice by its ID.
    """
    session = get_session()
    try:
        return session.query(Invoice).filter_by(id=invoice_id).first()
    except Exception as e:
        print(f"❌ Error fetching invoice by ID: {e}")
        return None
    finally:
        session.close()


# 🗑️ Delete an invoice
def delete_invoice(invoice_id):
    """
    Delete an invoice from the database.
    """
    session = get_session()
    try:
        invoice = session.query(Invoice).filter_by(id=invoice_id).first()
        if invoice:
            session.delete(invoice)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        print(f"❌ Error deleting invoice: {e}")
        return False
    finally:
        session.close()
