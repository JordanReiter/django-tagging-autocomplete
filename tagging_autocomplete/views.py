from django.http import HttpResponse
from django.utils import simplejson as json

from tagging.models import Tag

def list_tags(request):
        tags = json.dumps(list(Tag.objects.filter(name__istartswith=request.GET['q']).values('name').distinct()))
	return HttpResponse(tags, mimetype='application/json')