from django.urls import path
from .views import *

urlpatterns = [
    # Country URLs
    path("countries/", country_list, name="country_list"),
    path("countries/<int:pk>/", country_detail, name="country_detail"),
    # Industry URLs
    path("industries/", industry_list, name="industry_list"),
    path("industries/<int:pk>/", industry_detail, name="industry_detail"),
    # Investment Opportunity URLs
    path(
        "investment-opportunities/",
        investment_opportunity_list,
        name="investment_opportunity_list",
    ),
    path(
        "investment-opportunities/<int:pk>/",
        investment_opportunity_detail,
        name="investment_opportunity_detail",
    ),
    path(
        "investment-opportunities/create/",
        create_investment_opportunity,
        name="create_investment_opportunity",
    ),
    # Add more URLs as needed
]
from django.urls import path
from .views import *

urlpatterns = [
    # User Authentication URLs
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path("password-reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # User Profile URLs
    path("profile/", view_profile, name="view_profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),
    # Dashboard URL
    path("dashboard/", user_dashboard, name="user_dashboard"),
    # Investment Opportunities URLs
    path(
        "investment-opportunities/",
        investment_opportunity_list,
        name="investment_opportunity_list",
    ),
    path(
        "investment-opportunities/<int:pk>/",
        investment_opportunity_detail,
        name="investment_opportunity_detail",
    ),
    # Business Types URLs
    path("business-types/", business_types_list, name="business_types_list"),
    path("business-types/<int:pk>/", business_type_detail, name="business_type_detail"),
    # Prediction History URL
    path("prediction-history/", prediction_history, name="prediction_history"),
    # Neural Network Model Configuration URLs
    path("neural-network-config/", neural_network_config, name="neural_network_config"),
    # User Authentication URLs
    path("register/", register_user, name="register_user"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
    path("password-reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password-reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # User Profile URLs
    path("profile/", view_profile, name="view_profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),
    # Dashboard URL
    path("dashboard/", user_dashboard, name="user_dashboard"),
    # Investment Opportunities URLs
    path(
        "investment-opportunities/",
        investment_opportunity_list,
        name="investment_opportunity_list",
    ),
    path(
        "investment-opportunities/<int:pk>/",
        investment_opportunity_detail,
        name="investment_opportunity_detail",
    ),
    # Business Types URLs
    path("business-types/", business_types_list, name="business_types_list"),
    path("business-types/<int:pk>/", business_type_detail, name="business_type_detail"),
    # Prediction History URL
    path("prediction-history/", prediction_history, name="prediction_history"),
    # Neural Network Model Configuration URLs
    path("neural-network-config/", neural_network_config, name="neural_network_config"),
    # Data Visualization URL
    path("data-visualization/", data_visualization, name="data_visualization"),
    # Feedback Submission URL
    path("submit-feedback/<int:pk>/", submit_feedback, name="submit_feedback"),
    # Notification URLs
    path("notifications/", user_notifications, name="user_notifications"),
    # Data Source Integration URLs
    path("data-sources/", data_source_list, name="data_source_list"),
    path("data-sources/<int:pk>/", data_source_detail, name="data_source_detail"),
    # Risk Assessment URL
    path("calculate-risk/<int:pk>/", calculate_risk, name="calculate_risk"),
    # User Activity Log URLs
    path("user-activity-log/", user_activity_log, name="user_activity_log"),
    # Model Training Log URLs
    path("model-training-logs/", model_training_logs, name="model_training_logs"),
    # Authentication Token URLs
    path("generate-token/", generate_token, name="generate_token"),
    path("revoke-token/<int:pk>/", revoke_token, name="revoke_token"),
    # Privacy Settings URLs
    path("privacy-settings/", privacy_settings, name="privacy_settings"),
    # API Endpoint URLs (Optional)
    path("api-endpoint/", api_endpoint, name="api_endpoint"),
    # Admin Dashboard URLs (Optional)
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("manage-users/", manage_users, name="manage_users"),
    path("edit-user/<str:username>/", edit_user, name="edit_user"),
]


