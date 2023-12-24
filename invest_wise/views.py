from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import InvestmentOpportunityForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Country, Industry, InvestmentOpportunity
from .models import (
    UserProfile,
    InvestmentOpportunity,
    Prediction,
    UserActivityLog,
    Feedback,
)
from .forms import UserProfileForm, InvestmentOpportunityForm, FeedbackForm


def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, "user_profile.html", {"user_profile": user_profile})


@login_required
def create_investment_opportunity(request):
    if request.method == "POST":
        form = InvestmentOpportunityForm(request.POST)
        if form.is_valid():
            investment_opportunity = form.save(commit=False)
            investment_opportunity.added_by = request.user
            investment_opportunity.save()
            log_user_activity(request.user, "Created an investment opportunity")
            return redirect(
                "investment_opportunity_detail", pk=investment_opportunity.pk
            )
    else:
        form = InvestmentOpportunityForm()
    return render(request, "create_investment_opportunity.html", {"form": form})


def investment_opportunity_detail(request, pk):
    investment_opportunity = get_object_or_404(InvestmentOpportunity, pk=pk)
    return render(
        request,
        "investment_opportunity_detail.html",
        {"investment_opportunity": investment_opportunity},
    )


@login_required
def give_feedback(request, pk):
    investment_opportunity = get_object_or_404(InvestmentOpportunity, pk=pk)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.investment_opportunity = investment_opportunity
            feedback.save()
            log_user_activity(
                request.user, "Provided feedback on an investment opportunity"
            )
            return redirect("investment_opportunity_detail", pk=pk)
    else:
        form = FeedbackForm()
    return render(
        request,
        "give_feedback.html",
        {"form": form, "investment_opportunity": investment_opportunity},
    )


def log_user_activity(user, activity_type):
    UserActivityLog.objects.create(user=user, activity_type=activity_type)


def country_list(request):
    countries = Country.objects.all()
    return render(request, "country_list.html", {"countries": countries})


def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, "country_detail.html", {"country": country})


def industry_list(request):
    industries = Industry.objects.all()
    return render(request, "industry_list.html", {"industries": industries})


def industry_detail(request, pk):
    industry = get_object_or_404(Industry, pk=pk)
    return render(request, "industry_detail.html", {"industry": industry})


def investment_opportunity_list(request):
    opportunities = InvestmentOpportunity.objects.all()
    return render(
        request, "investment_opportunity_list.html", {"opportunities": opportunities}
    )


def investment_opportunity_detail(request, pk):
    opportunity = get_object_or_404(InvestmentOpportunity, pk=pk)
    return render(
        request, "investment_opportunity_detail.html", {"opportunity": opportunity}
    )


def create_investment_opportunity(request):
    if request.method == "POST":
        form = InvestmentOpportunityForm(request.POST)
        if form.is_valid():
            investment_opportunity = form.save(commit=False)
            investment_opportunity.added_by = request.user
            investment_opportunity.save()
            return redirect(
                "investment_opportunity_detail", pk=investment_opportunity.pk
            )
    else:
        form = InvestmentOpportunityForm()
    return render(request, "create_investment_opportunity.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserProfileForm


# User Authentication Views
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("user_dashboard")
    else:
        form = UserCreationForm()
    return render(request, "registration/register_user.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("user_dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login_user.html", {"form": form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect("home")


class CustomPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy("password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "registration/password_reset_complete.html"


# User Profile Views
@login_required
def view_profile(request):
    return render(request, "user_profile.html", {"user_profile": request.user.profile})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("view_profile")
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, "edit_profile.html", {"form": form})


# Dashboard View
@login_required
def user_dashboard(request):
    # Add logic to retrieve personalized information and predictions
    return render(request, "user_dashboard.html")


# Investment Opportunities View
def investment_opportunity_list(request):
    opportunities = InvestmentOpportunity.objects.all()
    return render(
        request, "investment_opportunity_list.html", {"opportunities": opportunities}
    )


def investment_opportunity_detail(request, pk):
    opportunity = get_object_or_404(InvestmentOpportunity, pk=pk)
    return render(
        request, "investment_opportunity_detail.html", {"opportunity": opportunity}
    )


# Business Types View
def business_types_list(request):
    business_types = BusinessType.objects.all()
    return render(
        request, "business_types_list.html", {"business_types": business_types}
    )


def business_type_detail(request, pk):
    business_type = get_object_or_404(BusinessType, pk=pk)
    return render(
        request, "business_type_detail.html", {"business_type": business_type}
    )


# Prediction History View
@login_required
def prediction_history(request):
    predictions = Prediction.objects.filter(user=request.user)
    return render(request, "prediction_history.html", {"predictions": predictions})


# Neural Network Model Configuration View
@login_required
def neural_network_config(request):
    # Add logic for configuring and managing neural network parameters
    return render(request, "neural_network_config.html")


# Data Visualization View
@login_required
def data_visualization(request):
    # Add logic for rendering and displaying interactive data visualizations using D3.js
    return render(request, "data_visualization.html")


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Feedback,
    Notification,
    DataSource,
    RiskAssessment,
    UserActivityLog,
    ModelTrainingLog,
    AuthenticationToken,
    PrivacySetting,
)
from .forms import (
    FeedbackForm,
    NotificationForm,
    DataSourceForm,
    RiskAssessmentForm,
    AuthenticationTokenForm,
    PrivacySettingForm,
)


# Feedback Submission View
@login_required
def submit_feedback(request, pk):
    prediction = get_object_or_404(Prediction, pk=pk)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.prediction = prediction
            feedback.save()
            return redirect("prediction_detail", pk=pk)
    else:
        form = FeedbackForm()
    return render(
        request, "submit_feedback.html", {"form": form, "prediction": prediction}
    )


# Notification View
@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, "user_notifications.html", {"notifications": notifications})


# Data Source Integration View
@login_required
def data_source_list(request):
    data_sources = DataSource.objects.all()
    return render(request, "data_source_list.html", {"data_sources": data_sources})


@login_required
def data_source_detail(request, pk):
    data_source = get_object_or_404(DataSource, pk=pk)
    return render(request, "data_source_detail.html", {"data_source": data_source})


# Risk Assessment View
@login_required
def calculate_risk(request, pk):
    investment_opportunity = get_object_or_404(InvestmentOpportunity, pk=pk)
    if request.method == "POST":
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            risk_assessment = form.save(commit=False)
            risk_assessment.investment_opportunity = investment_opportunity
            risk_assessment.save()
            return redirect("investment_opportunity_detail", pk=pk)
    else:
        form = RiskAssessmentForm()
    return render(
        request,
        "calculate_risk.html",
        {"form": form, "investment_opportunity": investment_opportunity},
    )


# User Activity Log View
@login_required
def user_activity_log(request):
    user_activity_logs = UserActivityLog.objects.filter(user=request.user)
    return render(
        request, "user_activity_log.html", {"user_activity_logs": user_activity_logs}
    )


# Model Training Log View
@login_required
def model_training_logs(request):
    model_training_logs = ModelTrainingLog.objects.all()
    return render(
        request,
        "model_training_logs.html",
        {"model_training_logs": model_training_logs},
    )


# Authentication Token View
@login_required
def generate_token(request):
    if request.method == "POST":
        form = AuthenticationTokenForm(request.POST)
        if form.is_valid():
            token = form.save(commit=False)
            token.user = request.user
            token.save()
            return redirect("user_dashboard")
    else:
        form = AuthenticationTokenForm()
    return render(request, "generate_token.html", {"form": form})


@login_required
def revoke_token(request, pk):
    token = get_object_or_404(AuthenticationToken, pk=pk)
    token.delete()
    return redirect("user_dashboard")


# Privacy Settings View
@login_required
def privacy_settings(request):
    if request.method == "POST":
        form = PrivacySettingForm(
            request.POST, instance=request.user.profile.privacy_setting
        )
        if form.is_valid():
            form.save()
            return redirect("view_profile")
    else:
        form = PrivacySettingForm(instance=request.user.profile.privacy_setting)
    return render(request, "privacy_settings.html", {"form": form})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import *
from .forms import *


# API Endpoint Views
def api_endpoint(request):
    # Add logic to handle API requests and responses
    # For example, you can use Django REST framework for building APIs
    # https://www.django-rest-framework.org/
    return render(request, "api_endpoint.html")


# Admin Dashboard Views
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    user_count = User.objects.count()
    country_count = Country.objects.count()
    industry_count = Industry.objects.count()
    investment_opportunity_count = InvestmentOpportunity.objects.count()
    notification_count = Notification.objects.count()
    feedback_count = Feedback.objects.count()

    context = {
        "user_count": user_count,
        "country_count": country_count,
        "industry_count": industry_count,
        "investment_opportunity_count": investment_opportunity_count,
        "notification_count": notification_count,
        "feedback_count": feedback_count,
    }

    return render(request, "admin_dashboard.html", context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def manage_users(request):
    users = User.objects.all()
    return render(request, "manage_users.html", {"users": users})


@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("manage_users")
    else:
        from .forms import UserEditForm

        form = UserEditForm(instance=user)
    return render(request, "edit_user.html", {"form": form, "user": user})


from django.conf import settings


def my_view(request):
    print(settings.MY_CUSTOM_SETTING)
