from django.core.files.base import ContentFile
from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.text import slugify

from .forms import ResumeForm
from .models import Resume


def generate_pdf(html_string, request):
    try:
        from weasyprint import HTML
    except Exception as exc:
        raise RuntimeError(
            "WeasyPrint is not available. Install it with 'pip install weasyprint' and ensure its native libraries are installed."
        ) from exc

    return HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf()


def create_resume(request):
    form = ResumeForm()
    error_message = None

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                resume = form.save()
                photo_url = request.build_absolute_uri(resume.passport_photo.url) if resume.passport_photo else ''
                html_string = render_to_string(
                    'resume/resume_pdf.html',
                    {
                        'resume': resume,
                        'photo_url': photo_url,
                    },
                )
                pdf_bytes = generate_pdf(html_string, request)
                filename = f"{slugify(resume.name) or 'resume'}_Resume.pdf"
                resume.generated_pdf.save(filename, ContentFile(pdf_bytes), save=True)
                return redirect('resume_success', resume_id=resume.id)
            except RuntimeError as exc:
                error_message = str(exc)
                form = ResumeForm(request.POST, request.FILES)
        else:
            error_message = 'Please correct the highlighted errors in the form.'

    return render(request, 'resume/create_resume.html', {'form': form, 'error_message': error_message})


def resume_success(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return render(request, 'resume/resume_success.html', {'resume': resume})


def download_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)

    if not resume.generated_pdf:
        return redirect('create_resume')

    return FileResponse(
        resume.generated_pdf.open('rb'),
        as_attachment=True,
        filename=f'{resume.name}_Resume.pdf',
    )


def index(request):
    return render(request, 'mriic/home.html')
