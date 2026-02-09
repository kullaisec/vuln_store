from services.auth_service import authenticate

def login_user(request):
    username = request.form.get("username")
    password = request.form.get("password")
    return authenticate(username, password)
