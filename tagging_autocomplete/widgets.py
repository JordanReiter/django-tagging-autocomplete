from django.forms.widgets import Input
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe

class TagAutocomplete(Input):
	input_type = 'text'
	
	def render(self, name, value, attrs=None):
		list_view = reverse('tagging_autocomplete-list')
		html = super(TagAutocomplete, self).render(name, value, attrs)
		js = u"""
			<script type="text/javascript">
			$(document).ready(function (){
				function split(term) {
					term = term.replace(/,\s*(\S+)\s*(,\s*|$)/g,'\n$1\n');
					term = term.replace(/>[,\s]*/g,'>\n');
					term = term.trim();
					return term.split('\n')
				}
				function extractLast(term) {
					return split(term).pop();
				}

				$('#%(id)s').autocomplete({
					minLength: 0,
					source: function(request, response) {
						$.getJSON("%(lookup)s", {
							q: extractLast(request.term)
						}, response);
					},
					focus: function() {
						// prevent value inserted on focus
						return false;
					},
					select: function(event, ui) {
						var terms = split( this.value );
						// remove the current input
						terms.pop();
						// add the selected item
						terms.push( ui.item.name );
						// add placeholder to get the comma-and-space at the end
						terms.push("");
						this.value = terms.join(", ");
						return false;
					}
				})
				.data( "autocomplete" )._renderItem = function( ul, item ) {
					return $( "<li></li>" )
						.data( "item.autocomplete", item )
						.append( "<a>" + item.name + "</a>" )
						.appendTo( ul );
				};
			});
			</script>
		""" % { 'id':attrs['id'], 'lookup': list_view}
		return mark_safe("\n".join([html, js]))
	
	class Media:
		js_base_url = getattr(settings, 'TAGGING_AUTOCOMPLETE_JS_BASE_URL','%s/jquery-autocomplete' % settings.MEDIA_URL)
		css = {
		    'all': ('%s/jquery.autocomplete.css' % js_base_url,)
		}
		js = (
			'%s/lib/jquery.js' % js_base_url,
			'%s/jquery.autocomplete.js' % js_base_url,
			)