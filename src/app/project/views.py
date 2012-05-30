from utils.decorators import as_html


@as_html('project/index.html')
def index(request):
    return {}
