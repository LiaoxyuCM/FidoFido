from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseForbidden,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from secrets import randbelow
from os import getenv
from dotenv import load_dotenv
from .forms import SimpleRegisterForm, PostForm, UsernameChangeForm
from passagesharer.models import Passage


def register_view(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    if request.method == "POST":
        form = SimpleRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successfully to create your account!")
            return redirect("accounts:dashboard")
            # request.session["user_email"] = form.cleaned_data["email"]
            # request.session["registration_data"] = {
            #     "username": form.cleaned_data["username"],
            #     "email": form.cleaned_data["email"],
            #     "password": form.cleaned_data["password1"],
            # }
            # login(request, user)
            #
            # del request.session["user_email"]
            # del request.session["smscode"]
            # del request.session["registration_data"]
            #
            # messages.success(request, "Successfully created your account!")
            # return redirect("accounts:dashboard")
        else:
            messages.error(request, "Failed, please check your form")
    else:
        form = SimpleRegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def register_sms_code_view(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:  # type: ignore
    # if request.method == "GET":
    #     smscode = randbelow(899999) + 100000
    #     request.session["smscode"] = smscode
    #     request.session.set_expiry(60)
    #     sender_mail = getenv("FidoFido_registeration_smtp_sender_email")
    #     password = getenv("FidoFido_registeration_smtp_password")
    #     receiver = ['WuBinBin@happymail.com',]

    load_dotenv(".\\accounts\\.env")
    if "user_email" not in request.session:
        messages.error(request, "Please complete registration first")
        return redirect("accounts:register")

    if request.method == "GET":
        if request.session.get("smscode", ""):
            messages.info(
                request,
                "A verification code has already been sent to your email. Please check your inbox.",
            )
            return render(request, "accounts/sms_verification.html")
        smscode = randbelow(89999999) + 10000000
        request.session["smscode"] = smscode
        request.session.set_expiry(300)

        sender_mail = getenv("FidoFido_registeration_smtp_sender_email")
        password = getenv("FidoFido_registeration_smtp_password")
        receiver = [request.session["user_email"]]

        try:
            mail_content = f"""\
Dear {request.session["registration_data"]["username"]},

Hello.
You are registering.
Your verification code is: {smscode}

This code will expire in 5 minutes.

If you didn't request this code, please ignore this email.

Best regards,
FidoFido
"""

            message = MIMEText(mail_content, "plain", "utf-8")
            message["From"] = formataddr(("FidoFido Verification", sender_mail))
            message["To"] = receiver[0]
            message["Subject"] = Header(
                "Your Verification Code - FidoFido Verification", "utf-8"
            )

            server = smtplib.SMTP_SSL(getenv("smtp_server"), 465)
            server.login(sender_mail, password)
            server.sendmail(sender_mail, receiver, message.as_string())
            server.quit()

            messages.success(request, "Verification code has been sent to your email!")
            return render(request, "accounts/sms_verification.html")

        except Exception as e:
            messages.error(request, f"Failed to send verification code: {str(e)}")
            return redirect("accounts:register")

    elif request.method == "POST":
        user_entered_code = request.POST.get("sms_code")
        stored_code = request.session.get("smscode")

        if str(stored_code) == user_entered_code:
            registration_data = request.session.get("registration_data")
            if registration_data:
                User = get_user_model()
                try:
                    user = User.objects.create_user(
                        username=registration_data["username"],
                        email=registration_data["email"],
                        password=registration_data["password"],
                    )
                    login(request, user)

                    del request.session["user_email"]
                    del request.session["smscode"]
                    del request.session["registration_data"]

                    messages.success(request, "Successfully created your account!")
                    return redirect("accounts:dashboard")

                except Exception as e:
                    messages.error(request, f"Failed to create account: {str(e)}")
                    return redirect("accounts:register")
            else:
                messages.error(request, "Registration data missing")
                return redirect("accounts:register")
        else:
            messages.error(request, "Invalid verification code")
            return render(request, "accounts/sms_verification.html")


def login_with_email_view(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:  # type: ignore
    return HttpResponseForbidden("安全起见，不支持邮箱注册")
    # if request.method == "GET":
    #     return render(request, "accounts/login_with_email.html")
    # if request.method == "POST":
    #     email = request.POST.get("email")
    #     if not email:
    #         messages.error(request, "Please provide your email address.")
    #         return redirect("accounts:login_with_email")
    #
    #     request.session["user_email"] = email
    #     return redirect("accounts:login_sms_code")


def login_sms_code_view(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:  # type: ignore
    # if request.method == "GET":
    #     smscode = randbelow(899999) + 100000
    #     request.session["smscode"] = smscode
    #     request.session.set_expiry(60)
    #     sender_mail = getenv("FidoFido_registeration_smtp_sender_email")
    #     password = getenv("FidoFido_registeration_smtp_password")
    #     receiver = ['WuBinBin@happymail.com',]

    load_dotenv(".\\accounts\\.env")
    if "user_email" not in request.session:
        messages.error(request, "Please complete login first")
        return redirect("accounts:login_with_email")

    if request.method == "GET":
        if request.session.get("smscode", ""):
            messages.info(
                request,
                "A verification code has already been sent to your email. Please check your inbox.",
            )
            return render(request, "accounts/sms_verification.html")
        smscode = randbelow(89999999) + 10000000
        request.session["smscode"] = smscode
        request.session.set_expiry(300)

        sender_mail = getenv("FidoFido_registeration_smtp_sender_email")
        password = getenv("FidoFido_registeration_smtp_password")
        receiver = [
            request.session["user_email"],
        ]

        User = get_user_model()
        try:
            user = User.objects.get(email=request.session["user_email"])

            try:
                mail_content = f"""\
Dear {user.username},

Hello.
You are logging in.
Your verification code is: {smscode}

This code will expire in 5 minutes.

If you didn't request this code, please ignore this email.

Best regards,
FidoFido
"""

                message = MIMEText(mail_content, "plain", "utf-8")
                message["From"] = formataddr(("FidoFido Verification", sender_mail))
                message["To"] = receiver[0]
                message["Subject"] = Header(
                    "Your Verification Code - FidoFido Verification", "utf-8"
                )

                server = smtplib.SMTP_SSL(getenv("smtp_server"), 465)
                server.login(sender_mail, password)
                server.sendmail(sender_mail, receiver, message.as_string())
                server.quit()

                messages.success(
                    request, "Verification code has been sent to your email!"
                )
                return render(request, "accounts/sms_verification.html")

            except Exception as e:
                messages.error(request, f"Failed to send verification code: {str(e)}")
                return redirect("accounts:register")
        except Exception as e:
            messages.error(request, "No account found with this email.")
            return redirect("accounts:login_with_email")

    elif request.method == "POST":
        user_entered_code = request.POST.get("sms_code")
        stored_code = request.session.get("smscode")

        if str(stored_code) == user_entered_code:
            email = request.session.get("user_email")
            if email:
                User = get_user_model()
                try:
                    user = User.objects.get(email=email)
                    login(request, user)

                    del request.session["user_email"]
                    del request.session["smscode"]

                    messages.success(request, "Successfully logged in!")
                    return redirect("accounts:dashboard")
                except User.DoesNotExist:
                    messages.error(request, "No account found with this email.")
                    return redirect("accounts:login_with_email")
        else:
            messages.error(request, "Invalid verification code")
            return render(request, "accounts/sms_verification.html")


def login_view(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("/admin/")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Username or password is wrong, please try again")

    return render(request, "accounts/login.html")


@login_required
def dashboard_view(request: HttpRequest) -> HttpResponse:
    passages = Passage.objects.order_by("-created_at")
    return render(
        request,
        "accounts/dashboard.html",
        context={
            "passages": passages,
            "user": request.user,
            "username": request.user.get_username(),
        },
    )


@login_required
def post_view(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Successfully posting a new passage.")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Failed, please check your form")
    else:
        form = PostForm()

    return render(request, "accounts/post_form.html", {"form": form, "editing": False})


@login_required
def delete_passage_view(
    request: HttpRequest, passage_id: int
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    passage = get_object_or_404(Passage, id=passage_id)
    if passage.author == request.user:
        if request.method == "POST":
            passage.delete()
            messages.success(request, "This passage has deleted")
            return redirect("accounts:dashboard")

        return render(request, "accounts/del_psg_confirm.html", {"passage": passage})
    else:
        return redirect("accounts:dashboard")


@login_required
def edit_passage_view(
    request: HttpRequest, passage_id: int
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    passage: Passage = get_object_or_404(Passage, id=passage_id)
    if passage.author == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=passage)
            if form.is_valid():
                form.save()
                messages.success(request, "Your passage has updated")
                return redirect("accounts:dashboard")
            else:
                messages.error(request, "Failed, please check your form")
        else:
            form = PostForm(instance=passage)

        return render(
            request,
            "accounts/post_form.html",
            {"form": form, "passage": passage, "editing": True},
        )
    else:
        return redirect("accounts:dashboard")


@login_required
def change_username(
    request,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    if request.method == "POST":
        form = UsernameChangeForm(request.POST, user=request.user)
        if form.is_valid():
            new_username = form.cleaned_data["new_username"]

            user = request.user
            user.username = new_username
            user.save()

            messages.success(request, "Updated your username.")
            return redirect("accounts:change_username")
    else:
        form = UsernameChangeForm(user=request.user)

    return render(request, "accounts/change_username.html", {"form": form})


def logout_view(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    logout(request)
    messages.success(request, "Successfully to logout")
    return redirect("accounts:login")


def user_profile_view(request: HttpRequest, userid: int) -> HttpResponse:
    user = get_object_or_404(get_user_model(), id=userid)
    passages = Passage.objects.filter(author=user).order_by("-created_at")
    return render(
        request,
        "accounts/user_profile.html",
        {
            "profile_user": user,
            "passages": passages,
            "is_logged": request.user.is_authenticated,
            "current_user": request.user,
        },
    )

