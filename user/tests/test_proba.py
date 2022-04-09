# import email
# from re import S
# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse

# from rest_framework.test import APIClient #Имитируем улиент АПИ
# from rest_framework import status

# from user.tests.test_user_api import ME_URL #Статуст коды для http

# CREATE_USER_URL = reverse('user:create')

# TOKEN_URL = reverse('user:token')

# ME_URL = reverse('user:me')

# def create_user(**params):
#     """Функция для создания нового пользователя"""
#     return get_user_model().objects.create_user(**params)

# class PublicUserApiTests(TestCase):
#     """Проверяем работу пользователя Api (public)"""

#     def setUp(self):
#         self.client= APIClient()

#     def test_create_valid_user_success(self):
#         """Тест на создание уч. записи с корректными данными """
#         payload = {
#             'email':'test@mail.com',
#             'password':'testPass',
#             'name':'nik'
#         }

#         res = self.client.post(CREATE_USER_URL, payload)

#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         user = get_user_model().objects.get(**res.data)
#         self.assertTrue(user.check_password(payload['password']))
#         self.assertNotIn('password',res.data)

#     def test_user_exits(self):
#         """Тетт на создание учетной записи с уже существующим пользователем"""
#         payload = {'email':'test@mail.com','password':'testpassword'}
#         create_user(**payload)
#         res = self.client.post(CREATE_USER_URL, payload)

#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_password_too_short(self):
#         """Тест на создание уч. записи с паролем меньше 5 символов"""
#         payload = {'email':'test@mpt.ru','password':'pw'}
#         res = self.client.post(CREATE_USER_URL, payload)

#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#         user_exists = get_user_model().objects.filter( 
#             email = payload['email']
#         ).exists()
#         self.assertFalse(user_exists)

#     def test_create_token_user(self):
#         payload = {'email':'test@user.com','password':'testpass'}
#         create_user(**payload)
#         res = self.client.post(TOKEN_URL, payload)

#         self.assertIn('token',res.data)
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
    
#     def test_create_token_invalid_credentials(self):
#         create_user(email='test@user.com',password='testpass')
#         payload = {'email':'test@admin.ru', 'password': 'wrong'}
#         res = self.client.post(TOKEN_URL, payload)

#         self.assertNotIn('token', res.data)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_token_no_user(self):
#         payload= {'email':'test@admin.ru','password':'testpass'}
#         res = self.client.post(TOKEN_URL, payload)

#         self.assertNotIn('token', res.data)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_token_missing_field(self):
#         res = self.client.post(TOKEN_URL, {'email':'one','password':''})
#         self.assertNotIn('token',res.data)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
#     # def test_retrieve_user_unauthorized(self):

#     #     res = self.client.get(ME_URL)

#     #     self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
