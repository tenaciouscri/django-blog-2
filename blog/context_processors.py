from .models import Category


def menu_links(request):
    """
    This will show the categories in the dropdown menu in all pages.
    """
    categories = Category.objects.all()
    return {"categories": categories}
