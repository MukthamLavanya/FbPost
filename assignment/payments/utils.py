def validate_user_id(user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponse("Invalid UserId")
