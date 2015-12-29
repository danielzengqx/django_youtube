from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from models import Document
from forms import DocumentForm
from django.core.urlresolvers import reverse


# Create your views here.

def home(request):
        # Handle file upload
    output = dict()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        for key, value in request.POST.iteritems():
            print key + ":" + value
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            comments = list()
            comments.append(request.POST['comment'])
            documents = Document.objects.all()

            output = dict(zip(comments, documents))
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('yearbook:home'))

    else:
        form = DocumentForm() # A empty, unbound form
        # form = ''

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render_to_response(
        'yearbook.html',
        {'documents': documents, 'form': form, 'img_title':output},
        context_instance=RequestContext(request)
    )

	# return HttpResponse(response)
	# return render(request, template, context)


