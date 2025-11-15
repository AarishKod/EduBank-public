from django.db import models

class Partner(models.Model):
    ORGANIZATION_TYPES = (
        ("Consultative Partnerships", "Consultative Partnerships"),
        ("Contributory Partnerships", "Contributory Partnerships"),
        ("Operational Partnerships", "Operational Partnerships"),
        ("Collaborative Partnerships", "Collaborative Partnerships"),
    )

    RESOURCE_TYPES = (
        ("Financial Resources", "Financial Resources"),
        ("Physical Resources", "Physical Resources"),
        ("Human Capital", "Human Capital"),
        ("Networking Resources", "Networking Resources"),
        ("Educational Resources", "Educational Resources"),
        ("Technology Resources", "Technology Resources"),
        ("Marketing and Promotion Resources", "Marketing and Promotion Resources"),
        ("Community Engagement Resources", "Community Engagement Resources"),
    )

    partner_Name = models.CharField(max_length=100)
    organization_Type = models.CharField(max_length=50, choices=ORGANIZATION_TYPES)
    available_Resources = models.CharField(max_length=50, choices=RESOURCE_TYPES)
    email = models.EmailField()
    phone_Number = models.CharField(max_length=20)

    def __str__(self):
        return self.partner_Name
    
class OrgType(models.Model):
    ORGANIZATION_TYPES = (
            ("Consultative Partnerships", "Consultative Partnerships"),
            ("Contributory Partnerships", "Contributory Partnerships"),
            ("Operational Partnerships", "Operational Partnerships"),
            ("Collaborative Partnerships", "Collaborative Partnerships"),
    )
    organization_type = models.CharField(max_length=50, choices=ORGANIZATION_TYPES)

class AvaType(models.Model):
    RESOURCE_TYPES = (
                ("Financial Resources", "Financial Resources"),
                ("Physical Resources", "Physical Resources"),
                ("Human Capital", "Human Capital"),
                ("Networking Resources", "Networking Resources"),
                ("Educational Resources", "Educational Resources"),
                ("Technology Resources", "Technology Resources"),
                ("Marketing and Promotion Resources", "Marketing and Promotion Resources"),
                ("Community Engagement Resources", "Community Engagement Resources"),
    )
    available_resources = models.CharField(max_length=50, choices=RESOURCE_TYPES)
    
