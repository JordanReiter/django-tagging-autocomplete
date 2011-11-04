from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson as json

from tagging.models import Tag

def list_tags(request):
        tags = serializers.serialize('json', Tag.objects.filter(name__istartswith=request.GET['q']), fields=('name','id'))
	return HttpResponse(tags, mimetype='application/json')