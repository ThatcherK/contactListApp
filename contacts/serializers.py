from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerialzer(ModelSerializer):
    class Meta:
        model=Contact
        fields=['country_code','first_name','last_name','phone_number','contact_picture','is_favorite', 'id']