from .models import Faculty
from modeltranslation.translator import TranslationOptions, register

@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('faculty_name', 'description')
