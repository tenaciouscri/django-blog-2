from .models import Category


def menu_links(request):
    '''
    This will show the categories in the dropdown menu in all pages.
    '''
    links = Category.objects.all()
    return {"links": links}
