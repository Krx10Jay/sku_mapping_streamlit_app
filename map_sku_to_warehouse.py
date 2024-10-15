import streamlit as st
import pandas as pd


def map_warehouse_to_sku(path: str, doc_type: str = "csv", ):#output_path: str = "new_csv.csv"):
    """
    Links each individual warehouse id to all SKU ids available in the file.
    
    Parameters:
        path (str): Path to the input CSV or Excel file.
        doc_type (str): Type of the document - "csv" or "excel".
        output_path (str): Path to save the output CSV file. Default is 'new_csv.csv'.
    
    Returns:
        pd.DataFrame: DataFrame with each warehouse id mapped to all SKU ids.
    """
    
    # Load the file based on the document type
    if doc_type == "csv":
        df = pd.read_csv(path)
    elif doc_type == "excel":
        df = pd.read_excel(path)
    else:
        st.error("Document type not supported. Please use 'csv' or 'excel'.")
        #return None
        print("doc_type not supported. Please use 'csv' or 'excel'.")
        return None
    
    # Identify the sku and warehouse columns
    sku_col = None
    warehouse_col = None
    
    for col in df.columns:
        if "sku" in col.lower():
            sku_col = col
        if "warehouse" in col.lower():
            warehouse_col = col
    
    # Ensure both columns are found
    if not sku_col or not warehouse_col:
        st.error("Could not find appropriate columns for SKU or Warehouse ID.")
        print("Could not find appropriate columns for SKU or Warehouse ID.")
        return None
    
    # Drop NaN values
    sku_ids = df[sku_col].dropna().unique()  # Get unique SKU ids
    warehouse_ids = df[warehouse_col].dropna().unique()  # Get unique Warehouse ids
    
    # Create a new DataFrame mapping each warehouse to all SKU ids
    expanded_df = pd.DataFrame([(warehouse, sku) for warehouse in warehouse_ids for sku in sku_ids], 
                               columns=['warehouse id', 'sku id'])
    
    # Save the new DataFrame to CSV
    # expanded_df.to_csv(output_path, index=False)
    # expanded_df.head()
    # print(f"File saved as {output_path}")
    
    return expanded_df
