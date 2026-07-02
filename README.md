# Resume Generator

This project was created by I Tadiwa E Tembo to demonstrate Django skills in web development.

It is a Django-based resume generator that allows users to enter their details, upload a passport photo, and generate a professional PDF resume.

## Features

- Fill out a resume form
- Upload a passport photo
- Save resume information to the database
- Generate a PDF resume from an HTML template
- Save the generated PDF in the media folder
- Download the generated PDF from the success page

## Project Structure

- `project1/` - Django project folder
- `mriic/` - Main app for the resume generator
- `mriic/templates/resume/` - Form, PDF, and success templates

## Requirements

- Python
- Django
- WeasyPrint

## How to Run

1. Open the project folder:
   ```powershell
   cd C:\Users\adiw\Desktop\Resume Generator
   ```

2. Activate the virtual environment:
   ```powershell
   .\m1\Scripts\activate
   ```

3. Start the development server:
   ```powershell
   python project1\manage.py runserver
   ```

4. Open the app in your browser:
   ```text
   http://127.0.0.1:8000/
   ```

## Notes

- Generated PDFs are saved in `project1/media/generated_resumes/`
- Uploaded passport photos are saved in `project1/media/passport_photos/`

## Future Improvements

- Add email sending
- Add more resume templates
- Improve the PDF design further

SCREENSHOTS







THE GENERATED RESUME PDF


