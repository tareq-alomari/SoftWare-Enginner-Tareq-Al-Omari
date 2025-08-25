# SchoolManagement/students/templatetags/app_tags.py

from django import template

register = template.Library()

@register.filter(name='pass_fail')
def check_pass_fail(marks, threshold=50):
    """
    Checks if the marks are above a certain threshold.
    Returns 'Pass' or 'Fail'.
    The threshold defaults to 50.
    """
    if marks >= threshold:
        return "ناجح"
    else:
        return "راسب"