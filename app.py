import cv2 as cv
import re 
from pathlib import Path
import os
from dotenv import load_dotenv
import datetime as dt 
import streamlit as st
import pytesseract as pyt

timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
VCARD_FILE = 'contact.vcf'

def config():
    load_dotenv()

def config():
    load_dotenv()

def read_business_card(input_path):
    # Set the path to the Tesseract executable
    tesseract_path = os.getenv("TESSERACT_PATH")
    pyt.pytesseract.tesseract_cmd = tesseract_path

    img = cv.imread(cv.samples.findFile(input_path))
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    try:
        # Uncomment and customize the configuration if needed
        # custom_config = r'--oem 3 --psm 6'

        # Perform OCR on the input image to extract text
        card_text = pyt.image_to_string(img_rgb)  #, config=custom_config)
        return card_text
    except Exception as e:
        st.write('Error during OCR:')
        st.write(e)
        return None


def extract_data(card_text):
    """
    Extract contact information from the text of a business card.

    Args:
    - card_text (str): Text extracted from a business card.

    Returns:
    - tuple: A tuple containing extracted information - phone numbers, emails, name, title, website.
    """

    # Define a regular expression pattern for websites
    url_pattern = re.compile(r'\b(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?\b')

    # Define a regular expression pattern for international phone numbers with seven or more digits
    phone_pattern = re.compile(r'\b(?:\+[\d\s-]+|\(\+\d+\)|\d{1,4}[-.\s]?)\d{1,9}[-.\s]?\d{1,9}[-.\s]?\d{1,9}[-.\s]?\d{1,9}\b')

    # Define a regular expression pattern for email addresses
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Extract websites, phone numbers, and emails from the card text
    websites = [site for site in re.findall(url_pattern, card_text) if 'www' in site]
    phone_numbers = [number for number in re.findall(phone_pattern, card_text) if len(number) > 7]
    emails = re.findall(email_pattern, card_text)

    # Extract name and title using a custom pattern
    name_parsing = r"^[\w'\-.][^0-9-!¡?+?¿/\\+=@#$%^&*(){}|~<>;:[\]]{2,}"
    name_title = re.findall(name_parsing, card_text)
    text_list = [word for line in name_title for word in line.split("\n") if len(word) > 3]

    # Assign extracted name and title
    name = text_list[0] if text_list else None
    title = text_list[1] if len(text_list) > 1 else None

    return phone_numbers, emails, name, title, websites

def create_vcf_file(name, phone_numbers, email, organization, website, filename=VCARD_FILE):
    """
    Create a VCF (Virtual Contact File) with the provided information.

    Args:
    - first_name (str): First name of the contact.
    - last_name (str): Last name of the contact.
    - phone_number (str): Phone number of the contact.
    - email (str): Email address of the contact.
    - organization (str): Organization of the contact.
    - filename (str, optional): Name of the output VCF file. Defaults to 'contact.vcf'.
    """

    vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
ORG:{organization}
TEL:{phone_numbers[0]}
EMAIL:{email[0]}
URL:{website[0]}
END:VCARD
"""
    with open(filename, 'r+') as vcf_file:
        vcf_file.write(vcf_content)

st.title("Business Card Reader")

UPLOAD_FOLDER = 'temp'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

uploaded_file = st.file_uploader("Upload a business card image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_name = f"uploaded_card_{timestamp}.png"
    file_path = os.path.join(UPLOAD_FOLDER, file_name)

    try:
        with open(file_path, "wb+") as f:
            f.write(uploaded_file.read())

        st.image(file_path, caption="Uploaded Image", use_column_width=True)

        if file_path is not None:
            card_text = read_business_card(file_path)

            if card_text is not None:
                phone_numbers, emails, name, title, websites = extract_data(card_text)
                create_vcf_file(name, phone_numbers, emails, title, websites, filename=f'contact.vcf')
            
            
            download_button = st.download_button(label="Download vCard", 
                                                 key="vcard", 
                                                 file_name=VCARD_FILE, 
                                                 data=os.path.abspath(VCARD_FILE))

            if download_button:
                # If the download button is clicked, do any additional actions here (if needed)
                st.success("vCard Downloaded!")

    except Exception as e:
        st.write('Error during file processing:')
        st.write(e)
    
    

    