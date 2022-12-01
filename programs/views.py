import io
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import FileResponse
from django.views.generic import ListView, DetailView
from reportlab.pdfgen import canvas

from .models import Program
# Create your views here.


class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'program_list'
    paginate_by = 4
    number_in_page = Program.objects.all().count()


class ProgramDetailView(DetailView):
    model = Program
    template_name: str = 'program_detail.html'

    def generate_pdf(request):
        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(100, 100, 'Hello world')

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='programs.pdf')
