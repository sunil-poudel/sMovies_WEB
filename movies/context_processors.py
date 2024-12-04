from .forms import SearchForm

def search_results(request):
    return {'search_form':SearchForm}