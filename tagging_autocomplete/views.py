from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson as json

from tagging.models import Tag

def list_tags(request):
	try:
		tags = Tag.objects.filter(name__istartswith=request.GET['q']).values_list('name', flat=True)
	except MultiValueDictKeyError:
		tags = []
	
	return HttpResponse(json.dumps(tags), mimetype='application/json')