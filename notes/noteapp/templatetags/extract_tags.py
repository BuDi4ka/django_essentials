from django import template
from django.utils.html import format_html
from django.shortcuts import get_object_or_404
from ..models import Note

register = template.Library()

@register.filter
def extract_tags(note):
    """
    Extract tags from a Note object and return them as a formatted string.
    Usage: {{ note|extract_tags }}
    """
    if not note or not hasattr(note, 'tags'):
        return ''
    
    tags = note.tags.all()
    result = ''
    
    for tag in tags:
        result += format_html('<span class="badge bg-primary me-1">{}</span>', tag.name)
    
    return format_html(result)

@register.simple_tag
def get_note_tags(note_id):
    """
    Get all tags for a note by its ID.
    Usage: {% get_note_tags note_id %}
    """
    try:
        note = get_object_or_404(Note, pk=note_id)
        tags = note.tags.all()
        result = ''
        
        for tag in tags:
            result += format_html('<span class="badge bg-primary me-1">{}</span>', tag.name)
        
        return format_html(result)
    except Exception:
        return '' 