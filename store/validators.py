from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_kb = 500

    if file.size > max_size_kb:
        raise ValidationError(f'File size cannot be greater that {max_size_kb}KB!')