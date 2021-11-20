def get_path_upload_avatar(instans, file):
    return f'avatar/{instans.id}/{file}'


def validate_size_image(file_obj):
    megabytelimit = 2
    if file_obj.size > megabytelimit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabytelimit}MB")
    
