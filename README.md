# Business Card Reader

## Overview
The Business Card Reader is an innovative application that leverages generative AI, computer vision, and optical character recognition (OCR) technologies to extract, organize, and manage contact information from business cards. The application provides an interactive and user-friendly interface for users to upload business card images and retrieve detailed contact information effortlessly.

## Features
- **OCR Processing:** Utilizes Tesseract OCR for accurate extraction of text from business card images.
- **Comprehensive Data Extraction:** Extracts diverse data, including phone numbers, emails, names, titles, and websites from business cards.
- **VCF File Generation:** Creates Virtual Contact Files (VCF) for easy integration with contact management systems.
- **Streamlit Interface:** Interactive web interface created with Streamlit for a seamless user experience.
- **Secure Environment Variables:** Sensible information, such as the Tesseract path, is securely handled using `python-dotenv`.
- **Versatile Development Stack:** Built with Python, OpenCV, and other cutting-edge technologies.

## Getting Started
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/xuzmocode4-325/business-card-reader.gits
2. **Install Dependencies**
   pip install -r requirements.txt
3. **Set the Environment Variables**
   TESSERACT_PATH=/path/to/tesseract
   You may need to specify t
4.**Run the Application**
   streamlit run app.py

## Future Improvements
Machine Learning Integration: Enhance OCR accuracy through machine learning techniques.
User Customization: Provide additional customization options for a more personalized user experience.
Contributions
Contributions are welcome! If you find issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgements 
Special thanks to [Brandon Jacobson](https://youtu.be/_p6e5R9kb8Y?si=ktQTicNLekC_gqCo)
