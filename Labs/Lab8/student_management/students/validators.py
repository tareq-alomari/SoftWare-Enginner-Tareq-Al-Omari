from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import magic

# Validator 1 : letter
f_name_validator = RegexValidator(
    regex=r'^[A-Z][a-zA-Z]*$',
    message="الاسم الأول يجب أن يبدأ بحرف Capital ويحتوي على أحرف فقط."
)

# Validator 2 :  type of  image
def validate_image_mimetype(file):
    """
    Validates that the uploaded file is a real image (PNG, JPG, JPEG).
    """
    accept = ['image/png', 'image/jpeg', 'image/jpg']
    file_mime_type = magic.from_buffer(file.read(2048), mime=True)
    if file_mime_type not in accept:
        raise ValidationError("نوع الملف غير مدعوم. يرجى رفع صورة بصيغة png, jpg, أو jpeg.")
