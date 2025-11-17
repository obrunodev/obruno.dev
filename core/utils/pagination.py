from django.core.paginator import Paginator


def paginate(request, object_context):
    paginator = Paginator(object_context, 10)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
