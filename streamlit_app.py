#Import required libraries
import streamlit as st     # For creating web UI
import pandas as pd        # For reading excel file
import xml.etree.ElementTree as ET   # For parsing and editing TGML

# Set title on browser tab and center-align the layout
st.set_page_config(page_title="Automatic Binding Tool", layout="centered")
 
# Add custom CSS for styling the background and form
st.markdown("""
    <style>
    /* set the full page background color */
    .body {
        background-color: #0070AD;
    }
    /* style the content box */
    main {
         color: pink;
     }

     /* title styling */
    h1 {
        text-align: center;
        color: #114488;
        font-size: 32px;
    }
    p {
       text-align: center;
       margin-bottom: 20px;
       font-size: 14px;
       color: black;
     }
    /* sub title styling*/
    sub {
        text-align: center;
        color: pink;
        margin-bottom: 30px;
        font-size: 16px;
    }
    /* button styling */
    .stButton>button {
        background-color: #1abc9c;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
    }
    /* Hover effect for buttn=on */
    .stButton>button:hover {
        background-color: #16a085;
    }
    block-container {
        background-color: #0070AD !important;
    }
    </style>
""", unsafe_allow_html=True)
 
# Add title and description
st.markdown('<div class="main">', unsafe_allow_html=True)
#title of the app
st.markdown('<h1>TGML Binding Tool</h1>', unsafe_allow_html=True)
# sub text with instreuctions
st.markdown('<p class="sub">Upload TGML & Excel File to Update Bindings</p>', unsafe_allow_html=True)
 
# File uploaders and input
tgml_file = st.file_uploader("TGML File", type="tgml")
excel_file = st.file_uploader("Excel File", type="xlsx")
sheet_name = st.text_input("Sheet Name:", "")
 
# Button and logic
if st.button("Submit and Download") and tgml_file and excel_file and sheet_name:
    try:
        # Parse XML
        tree = ET.parse(tgml_file)
        root = tree.getroot()
 
        # Read Excel
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        label_to_bind = {}
 
        for _, row in df.iterrows():
            nomenclature = str(row.get("Nomenclature", "")).strip()
            for col in ["First Label", "Second Label", "Third Label"]:
                label = str(row.get(col, "")).strip()
                if label:
                    label_to_bind[label] = nomenclature
 
        # Replace in TGML
        in_group = False
        current_text = None
        inside_target_text = False
 
        for elem in root.iter():
            if elem.tag == "Group":
                in_group = True
            elif elem.tag == "Text" and in_group:
                current_text = elem.attrib.get("Name", "").strip()
                inside_target_text = current_text in label_to_bind
            elif elem.tag == "Bind" and in_group and inside_target_text:
                new_bind = label_to_bind.get(current_text)
                elem.set("Name", new_bind)
            elif elem.tag == "Text" and inside_target_text:
                inside_target_text = False
 
        # Save new file
        output_file = "updated_" + tgml_file.name
        tree.write(output_file, encoding="utf-8", xml_declaration=True)
 
        with open(output_file, "rb") as f:
            st.download_button("Download Updated TGML", f, file_name=output_file)
 
        st.success("Binding completed successfully!")
 
    except Exception as e:
        # shows error if something goes wrong
        st.error(f"Error: {e}")
 
st.markdown('</div>', unsafe_allow_html=True)
