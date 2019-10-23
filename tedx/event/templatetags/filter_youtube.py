from django_jinja import library
import jinja2
from django import template

register = template.Library()

def youtube(value):
    """
    Filter to rebuild youtube link. Usage: {{ "link" | youtube }}
    """
    return f"https://www.youtube.com/embed/{ value.split('/')[-1] }"



register.filter('youtube', youtube)