import streamlit as st
import pandas as pd
from io import StringIO
import map_sku_to_warehouse as sku

st.title("Warehouse to SKU Mapping")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Select file type
    doc_type = st.radio("Select document type", ("csv", "excel"))
    
    # If file is uploaded and document type is selected
    if st.button("Generate SKU-Warehouse Mapping"):
        # Convert uploaded file to a DataFrame
        if doc_type == "csv":
            file_as_str = StringIO(uploaded_file.getvalue().decode("utf-8"))
            df = pd.read_csv(file_as_str)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Apply the mapping function
        result_df = sku.map_warehouse_to_sku(uploaded_file, doc_type=doc_type)
        
        if result_df is not None:
            st.success("Mapping successfully generated!")
            st.write(result_df)
            
            # Provide download link for CSV file
            csv = result_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download mapped CSV",
                data=csv,
                file_name="warehouse_sku_mapping.csv",
                mime="text/csv",
            )