import streamlit as st
import pdfplumber
import re
import json

# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to extract row-based details from a table
def extract_row_based_details(table_data):
    extracted_data = {}
    selected_fields = ["Invoice No", "Customer No", "Date", "Invoice Period"]
    
    for table in table_data:
        if len(table) >= 2:  # Ensure at least 2 rows exist
            field_names = table[0]  # First row contains field names
            values = table[1]  # Second row contains values
            
            # Map the field names to their values
            for field, value in zip(field_names, values):
                if field and field.strip() in selected_fields:
                    extracted_data[field.strip()] = value.strip() if value else None
    return extracted_data

# Function to extract column-based details from text using regex
def extract_column_based_details(text):
    extracted_data = {
        "Vendor Information": None,
        "Total Amount": None,
        "VAT": None,
        "Gross Amount incl. VAT": None,
        "Bank Details": None,
    }

    patterns = {
        "Vendor Information": r"CPB Software \(Germany\) GmbH - .+",
        "Total Amount": r"Total\s+([\d,]+\s?€)",
        "VAT": r"VAT\s+\d+\s*%\s+([\d,]+\s?€)",
        "Gross Amount incl. VAT": r"Gross Amount incl\. VAT\s+([\d,]+\s?€)",
        "Bank Details": r"IBAN\s+(.*?)(?=\| BIC)"
    }

    for key, pattern in patterns.items():
        matches = re.findall(pattern, text, re.MULTILINE)
        if matches:
            extracted_value = matches[0] if isinstance(matches[0], str) else ' to '.join(matches[0])
            extracted_data[key] = extracted_value.strip()
    
    return extracted_data

# Function to extract table data from PDF using pdfplumber for row-based fields
def extract_table_from_pdf(file):
    table_data = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if table:
                    table_data.append(table)
    return table_data

# Function to create JSON template
def create_json_template(extracted_data):
    json_template = {}
    for key, value in extracted_data.items():
        json_template[key] = {
            "rule": f"Extract the '{key}' from the invoice."
        }
    return json_template

def main():
    st.title("Invoice Extractor")
    st.write("Upload a PDF file to extract details.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        st.write("Extracting data...")

        # Extract the text and table data
        text = extract_text_from_pdf(uploaded_file)
        table_data = extract_table_from_pdf(uploaded_file)
        
        # Extract column-based details using regex
        column_data = extract_column_based_details(text)
        
        # Extract row-based details from the table
        row_data = extract_row_based_details(table_data)
        
        # Combine both extraction results
        combined_data = {**column_data, **row_data}

        # Create JSON template
        st.write("Extracted Data in JSON Format:")
        st.json(combined_data)

if __name__ == "__main__":
    main()
