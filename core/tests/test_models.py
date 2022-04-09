from django.test import TestCase, tag
from django.contrib.auth import get_user_model


from core import models

def sample_user(email = 'test@admin.com',  password='testpass'):

    return get_user_model().objects.create_user(email,password)

class ModelTest(TestCase):
    def test_create_user_widh_email_successfull(self):
        email = 'test@test.com'
        password = 'TestPasswod123'

        user = get_user_model().objects.create_user(
            email = email,
            password=password

        )
        self.assertEquals(user.email , email)
        self.assertTrue(user.check_password(password))


    def test_tag_str(self):
        """Тест на текстовое представление модели"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Рыба'
        )

        self.assertEqual(str(tag),tag.name)
