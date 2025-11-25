from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings

from .models import Suggestion


def autocomplete(request):
    query = request.GET.get("q", "")

    if not query:
        return JsonResponse({"results": []})

    trie = settings.TRIE
    results = trie.search_prefix(query)

    return JsonResponse({"results": results})


def autosuggest(request):
    query = request.GET.get("q", "")

    if not query:
        return JsonResponse({"results": []})

    # Contains-based results from DB
    results = Suggestion.objects.filter(text__icontains=query).values_list("text", flat=True)[:15]

    return JsonResponse({"results": list(results)})

