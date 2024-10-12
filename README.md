**Invoice PDF Extractor**<br>
This project is a simple Invoice PDF Extractor built using Streamlit for the frontend and pdfplumber and regex for PDF text extraction. The application extracts specific fields from an invoice in PDF format and displays the extracted data in JSON format. The main goal of this project is to automate the extraction of key information from invoices without any manual selection of fields, making it user-friendly and efficient.

Features
Extracts Vendor Information, Total Amount, VAT, Gross Amount incl. VAT, and Bank Details using regular expressions.
Extracts Invoice No, Customer No, Date, and Invoice Period from table-based data using pdfplumber.
Automatically combines the extracted data and displays it in JSON format.

Libraries Used
Streamlit: For creating a web-based UI to upload the PDF file and display the extracted data.
pdfplumber: To extract tables and raw text from the uploaded PDF file.
re (Regular Expressions): For extracting column-based fields (such as Vendor Information and Amounts) from the raw text.

How It Works
PDF Upload: The user uploads a PDF invoice file via a simple UI.
PDF Text and Table Extraction: The PDF file is processed using pdfplumber. It extracts text from the file and processes tables to find fields like Invoice No, Customer No, Date, and Invoice Period.
Regular Expression Matching: Predefined regular expressions are used to extract fields like Vendor Information, Total Amount, VAT, Gross Amount incl. VAT, and Bank Details directly from the text.
Display JSON Output: The extracted data from both table-based and regex-based methods are combined and displayed in JSON format.

Assumptions Made
Invoice Format: The PDF files provided for extraction follow a specific format, particularly in terms of table structure and textual content. For example, the "Vendor Information" follows a pattern of CPB Software (Germany) GmbH - ... and amounts are in Euro (€). The regex patterns used for extracting column-based data rely on the assumption that the structure will not significantly vary across invoices.
Table Structure: The row-based details like Invoice No, Customer No, etc., are assumed to be present in table format, with field names in the first row and their corresponding values in the second row.
No Field Selection Needed: The requirement to automatically display all fields without the need for the user to manually select them is implemented. This ensures that all necessary fields are extracted without user intervention.

Thought Process
Separation of Column-Based and Row-Based Extraction: The code separates column-based extractions (e.g., amounts and vendor info) from row-based extractions (e.g., invoice numbers). This ensures that the logic for dealing with both types of data remains clear and modular.
Error Handling via Defaults: When a pattern does not match or a table field is not found, the code assigns None values to ensure that the final output still provides all expected fields, even if some data is missing.
Extensibility: The code is designed to be extensible. If new fields need to be added in the future, users can add new regex patterns or modify the field names extracted from the tables.

Instructions to Run

Install Dependencies:
    pip install streamlit pdfplumber

Run the Streamlit App:
    streamlit run app.py

Upload a PDF Invoice: Once the app is running in your browser, upload a PDF invoice to extract and display the relevant details.
