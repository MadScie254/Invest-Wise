from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class InvestmentOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    predicted_roi = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    preferences = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class BusinessType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    industry = models.ForeignKey("Industry", on_delete=models.CASCADE)
    market_demand = models.TextField()
    historical_performance = models.TextField()

    def __str__(self):
        return self.name


class InvestmentOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    industry = models.ForeignKey("Industry", on_delete=models.CASCADE)
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    predicted_roi = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Prediction(models.Model):
    investment_opportunity = models.OneToOneField(
        InvestmentOpportunity, on_delete=models.CASCADE
    )
    confidence_level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.investment_opportunity.title} - Confidence: {self.confidence_level}"
        )


class HistoricalData(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    economic_data = models.TextField()
    financial_data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.region.name} - {self.timestamp}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    preferences = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class BusinessType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    industry = models.ForeignKey("Industry", on_delete=models.CASCADE)
    market_demand = models.TextField()
    historical_performance = models.TextField()

    def __str__(self):
        return self.name


class InvestmentOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    industry = models.ForeignKey("Industry", on_delete=models.CASCADE)
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    predicted_roi = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Prediction(models.Model):
    investment_opportunity = models.OneToOneField(
        InvestmentOpportunity, on_delete=models.CASCADE
    )
    confidence_level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.investment_opportunity.title} - Confidence: {self.confidence_level}"
        )


class HistoricalData(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    economic_data = models.TextField()
    financial_data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.region.name} - {self.timestamp}"


# Additional models
class NeuralNetworkModelConfig(models.Model):
    name = models.CharField(max_length=255)
    layers = models.PositiveIntegerField()
    activation_function = models.CharField(max_length=50)
    learning_rate = models.FloatField()
    training_iterations = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_opportunity = models.ForeignKey(
        InvestmentOpportunity, on_delete=models.CASCADE
    )
    feedback_text = models.TextField()
    rating = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class DataSource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    api_endpoint = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)


class RiskAssessment(models.Model):
    investment_opportunity = models.ForeignKey(
        InvestmentOpportunity, on_delete=models.CASCADE
    )
    risk_score = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class ModelTrainingLog(models.Model):
    neural_network_config = models.ForeignKey(
        NeuralNetworkModelConfig, on_delete=models.CASCADE
    )
    loss = models.FloatField()
    accuracy = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class AuthenticationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    expiration_time = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)


class PrivacySetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enable_data_sharing = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
