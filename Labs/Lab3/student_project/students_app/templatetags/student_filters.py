from django import template
from django.utils.html import mark_safe 

register = template.Library()

@register.filter(name='pass_fail')
def check_pass_fail(marks, threshold=50):
    if marks >= threshold:
        return "ناجح"
    else:
        return "راسب"

@register.filter(name='status_badge')
def format_status_as_badge(status):
    """
    يحول النص 'نعم' أو 'لا' إلى شارة Bootstrap ملونة.
    """
    if status == "نعم":
        badge_html = '<span class="badge bg-success">منتظم</span>'
    elif status == "لا":
        badge_html = '<span class="badge bg-danger">غير منتظم</span>'
    else:
        badge_html = status # إذا كانت القيمة مختلفة، اعرضها كما هي

    return mark_safe(badge_html) # نستخدم mark_safe للسماح بعرض الـ HTML