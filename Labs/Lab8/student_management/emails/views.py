from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.timezone import now

def send_welcome_email(username, recipient_email):
    """
    تجهيز وإرسال بريد إلكتروني ترحيبي للمستخدم الجديد.
    """
    subject = f"مرحباً بك في منصتنا يا {username}!"
    from_email = 'qutabh2@gmail.com' # **هام: يجب أن يتطابق مع EMAIL_HOST_USER**
    
    context = {
        'username': username,
        'year': now().year,
    }
    
    html_message = render_to_string('emails/welcome_email.html', context)
    
    try:
        email_message = EmailMessage(subject, html_message, from_email, [recipient_email])
        email_message.content_subtype = 'html'  # تحديد أن المحتوى هو HTML
        sent_count = email_message.send()
        return sent_count > 0 # ترجع True إذا تم الإرسال بنجاح
    except Exception as e:
        # في المشاريع الحقيقية، يجب تسجيل الخطأ هنا
        print(f"Error sending email: {e}")
        return False