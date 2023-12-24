from django.test import TestCase
from .models import Country, Industry, InvestmentOpportunity
from django.contrib.auth.models import User
from django.urls import reverse
from .models import (
    Prediction,
    HistoricalData,
    Region,
    NeuralNetworkModelConfig,
    UserActivityLog,
    ModelTrainingLog,
    Notification,
    Feedback,
    DataSource,
    RiskAssessment,
    AuthenticationToken,
    PrivacySetting,
    HistoricalData,
    Prediction,
    InvestmentOpportunity,
)


class CountryModelTest(TestCase):
    def test_country_creation(self):
        country = Country.objects.create(name="Kenya")
        self.assertEqual(country.name, "Kenya")
        self.assertEqual(str(country), "Kenya")


class IndustryModelTest(TestCase):
    def test_industry_creation(self):
        industry = Industry.objects.create(name="Technology")
        self.assertEqual(industry.name, "Technology")
        self.assertEqual(str(industry), "Technology")


class InvestmentOpportunityModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        country = Country.objects.create(name="Kenya")
        industry = Industry.objects.create(name="Technology")

        self.investment_opportunity = InvestmentOpportunity.objects.create(
            title="Tech Startup",
            description="A promising tech startup opportunity",
            country=country,
            industry=industry,
            predicted_roi=10.5,
            user=user,
        )

    def test_investment_opportunity_creation(self):
        self.assertEqual(self.investment_opportunity.title, "Tech Startup")
        self.assertEqual(
            self.investment_opportunity.description,
            "A promising tech startup opportunity",
        )
        self.assertEqual(self.investment_opportunity.country.name, "Kenya")
        self.assertEqual(self.investment_opportunity.industry.name, "Technology")
        self.assertEqual(self.investment_opportunity.predicted_roi, 10.5)
        self.assertEqual(str(self.investment_opportunity), "Tech Startup")


class UserAuthenticationTests(TestCase):
    def test_user_registration(self):
        response = self.client.post(
            reverse("register_user"),
            {"username": "testuser", "password": "testpassword"},
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful registration and redirect

    def test_user_login_logout(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        response = self.client.post(
            reverse("login_user"), {"username": "testuser", "password": "testpassword"}
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful login and redirect
        response = self.client.get(reverse("logout_user"))
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful logout and redirect


class UserProfileTests(TestCase):
    def test_user_profile_creation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful
        response = self.client.get(reverse("view_profile"))
        self.assertEqual(
            response.status_code, 200
        )  # Check if the profile page is accessible

    def test_user_profile_update(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("edit_profile"), {"first_name": "John"})
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful profile update and redirect


class DashboardTests(TestCase):
    def test_user_dashboard(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("user_dashboard"))
        self.assertEqual(
            response.status_code, 200
        )  # Check if the dashboard page is accessible


class InvestmentOpportunityTests(TestCase):
    def test_investment_opportunity_creation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        country = Country.objects.create(name="Kenya")
        industry = Industry.objects.create(name="Technology")

        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.post(
            reverse("investment_opportunity_list"),
            {
                "title": "Tech Startup",
                "description": "A promising tech startup opportunity",
                "country": country.id,
                "industry": industry.id,
                "predicted_roi": 10.5,
            },
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful investment opportunity creation and redirect


class BusinessTypeTests(TestCase):
    def test_business_type_creation(self):
        industry = Industry.objects.create(name="Technology")
        response = self.client.post(
            reverse("business_types_list"),
            {"name": "Tech Business", "industry": industry.id},
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful business type creation and redirect


class PredictionTests(TestCase):
    def test_prediction_generation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        investment_opportunity = InvestmentOpportunity.objects.create(
            title="Tech Startup",
            description="A promising tech startup opportunity",
            country=Country.objects.create(name="Kenya"),
            industry=Industry.objects.create(name="Technology"),
            predicted_roi=10.5,
            user=user,
        )

        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.post(
            reverse("generate_prediction", args=[investment_opportunity.id])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful prediction generation and redirect

        prediction = Prediction.objects.get(
            investment_opportunity=investment_opportunity
        )
        self.assertIsNotNone(prediction)  # Check if the prediction is created
        self.assertEqual(
            prediction.confidence_level, 0.8
        )  # Replace with the expected confidence level


class HistoricalDataTests(TestCase):
    def test_historical_data_creation(self):
        historical_data = HistoricalData.objects.create(
            economic_indicator="GDP",
            value=100.5,
            region=Region.objects.create(name="Kenya"),
        )
        self.assertEqual(historical_data.economic_indicator, "GDP")
        self.assertEqual(historical_data.value, 100.5)


class RegionTests(TestCase):
    def test_region_creation(self):
        region = Region.objects.create(name="Kenya")
        self.assertEqual(region.name, "Kenya")
        self.assertEqual(str(region), "Kenya")


class NeuralNetworkModelConfigTests(TestCase):
    def test_model_config_creation(self):
        model_config = NeuralNetworkModelConfig.objects.create(
            layers=3, neurons_per_layer=100, activation_function="relu"
        )
        self.assertEqual(model_config.layers, 3)
        self.assertEqual(model_config.neurons_per_layer, 100)
        self.assertEqual(model_config.activation_function, "relu")


class UserActivityLogTests(TestCase):
    def test_user_activity_logging(self):
        user = User.objects.create_user(username="testuser", password="testpassword")

        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.get(reverse("user_dashboard"))
        self.assertEqual(
            response.status_code, 200
        )  # Check if the dashboard page is accessible

        user_activity_log = UserActivityLog.objects.filter(
            user=user, activity="Viewed Dashboard"
        ).first()
        self.assertIsNotNone(
            user_activity_log
        )  # Check if the user activity log is created


class NotificationTests(TestCase):
    def test_notification_creation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        notification = Notification.objects.create(
            user=user, message="New prediction available!", is_read=False
        )
        self.assertEqual(notification.user, user)
        self.assertEqual(notification.message, "New prediction available!")


class FeedbackTests(TestCase):
    def test_feedback_submission(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        investment_opportunity = InvestmentOpportunity.objects.create(
            title="Tech Startup",
            description="A promising tech startup opportunity",
            country=Country.objects.create(name="Kenya"),
            industry=Industry.objects.create(name="Technology"),
            predicted_roi=10.5,
            user=user,
        )

        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.post(
            reverse("submit_feedback", args=[investment_opportunity.id]),
            {"comment": "Great prediction!"},
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful feedback submission and redirect

        feedback = Feedback.objects.get(investment_opportunity=investment_opportunity)
        self.assertIsNotNone(feedback)  # Check if the feedback is created
        self.assertEqual(feedback.comment, "Great prediction!")


class DataSourceIntegrationTests(TestCase):
    def test_data_source_integration(self):
        data_source = DataSource.objects.create(
            name="Financial Database", url="http://example.com/financial_data"
        )
        self.assertEqual(data_source.name, "Financial Database")
        self.assertEqual(data_source.url, "http://example.com/financial_data")


class RiskAssessmentTests(TestCase):
    def test_risk_assessment_calculation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        investment_opportunity = InvestmentOpportunity.objects.create(
            title="Tech Startup",
            description="A promising tech startup opportunity",
            country=Country.objects.create(name="Kenya"),
            industry=Industry.objects.create(name="Technology"),
            predicted_roi=10.5,
            user=user,
        )

        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.post(
            reverse("calculate_risk_assessment", args=[investment_opportunity.id])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful risk assessment calculation and redirect

        risk_assessment = RiskAssessment.objects.get(
            investment_opportunity=investment_opportunity
        )
        self.assertIsNotNone(risk_assessment)  # Check if the risk assessment is created


class ModelTrainingLogTests(TestCase):
    def test_model_training_log_creation(self):
        model_training_log = ModelTrainingLog.objects.create(
            model_name="Neural Network Model", epochs=50, accuracy=0.95
        )
        self.assertEqual(model_training_log.model_name, "Neural Network Model")
        self.assertEqual(model_training_log.epochs, 50)
        self.assertEqual(model_training_log.accuracy, 0.95)


class AuthenticationTokenTests(TestCase):
    def test_token_generation_and_revocation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")

        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.get(reverse("generate_token"))
        self.assertEqual(
            response.status_code, 200
        )  # Check if the token generation page is accessible

        token = AuthenticationToken.objects.filter(user=user).first()
        self.assertIsNotNone(token)  # Check if the authentication token is generated

        response = self.client.post(reverse("revoke_token"))
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful token revocation and redirect
        token = AuthenticationToken.objects.filter(user=user).first()
        self.assertIsNone(token)  # Check if the authentication token is revoked


class PrivacySettingTests(TestCase):
    def test_privacy_settings(self):
        user = User.objects.create_user(username="testuser", password="testpassword")

        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.post(
            reverse("update_privacy_settings"), {"share_data": False}
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for successful privacy settings update and redirect

        privacy_setting = PrivacySetting.objects.get(user=user)
        self.assertFalse(
            privacy_setting.share_data
        )  # Check if the privacy setting is updated


class EdgeCasesTests(TestCase):
    def test_empty_data_set(self):
        # Test how the application handles cases where essential data sets are empty
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(
            response.status_code, 200
        )  # Check if the dashboard is accessible even with empty data sets

    def test_no_predictions_available(self):
        # Test the behavior when there are no predictions available for a specific user or scenario
        user = User.objects.create_user(username="testuser", password="testpassword")
        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.get(reverse("prediction_history"))
        self.assertEqual(
            response.status_code, 200
        )  # Check if the prediction history is accessible even with no predictions

    def test_zero_confidence_level(self):
        # Test the handling of predictions with a confidence level of zero
        user = User.objects.create_user(username="testuser", password="testpassword")
        investment_opportunity = InvestmentOpportunity.objects.create(
            title="Tech Startup",
            description="A promising tech startup opportunity",
            country=Country.objects.create(name="Kenya"),
            industry=Industry.objects.create(name="Technology"),
            predicted_roi=10.5,
            user=user,
        )
        prediction = Prediction.objects.create(
            investment_opportunity=investment_opportunity, confidence_level=0.0
        )
        self.assertEqual(
            prediction.confidence_level, 0.0
        )  # Check if the platform handles zero confidence level
    def test_empty_data_set(self):
        # Test how the application handles cases where essential data sets are empty
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(
            response.status_code, 200
        )  # Check if the dashboard is accessible even with empty data sets

    def test_no_predictions_available(self):
        # Test the behavior when there are no predictions available for a specific user or scenario
        user = User.objects.create_user(username="testuser", password="testpassword")
        response = self.client.login(username="testuser", password="testpassword")
        self.assertTrue(response)  # Check if login is successful

        response = self.client.get(reverse("prediction_history"))
        self.assertEqual(
            response.status_code, 200
        )  # Check if the prediction history is accessible even with no predictions

    def test_zero_confidence_level(self):
        # Test the handling of predictions with a confidence level of zero
        user = User.objects.create_user(username="testuser", password="testpassword")
        investment_opportunity = InvestmentOpportunity.objects.create(
            title="Tech Startup",
            description="A promising tech startup opportunity",
            country=Country.objects.create(name="Kenya"),
            industry=Industry.objects.create(name="Technology"),
            predicted_roi=10.5,
            user=user,
        )
        prediction = Prediction.objects.create(
            investment_opportunity=investment_opportunity, confidence_level=0.0
        )
        self.assertEqual(
            prediction.confidence_level, 0.0
        )  # Check if the platform handles zero confidence level

    def test_invalid_user_inputs(self):
        # Evaluate the application's response to invalid or unexpected user inputs in forms
        invalid_input_data = {"invalid_field": "invalid_value"}
        response = self.client.post(reverse("some_form_view"), invalid_input_data)
        self.assertEqual(
            response.status_code, 400
        )  # Check if the platform returns a bad request for invalid input
