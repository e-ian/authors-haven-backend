from rest_framework import status
from django.urls import reverse
from .base import BaseTest
from .test_data import (
    VALID_USER_DATA,
    EMPTY_EMAIL,
    EMPTY_USERNAME,
    EMPTY_PASSWORD,
    INVALID_EMAIL,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    EMPTY_SPACE_USERNAME,
    EMPTY_SPACE_EMAIL,
    SHORT_PASSWORD,
    PASSWORD_WITH_SPACE
)


class UserRegisterTest(BaseTest):
    """
    contains user login tests method
    """

    def test_register_user(self):
        """
        test user registration valid credentialsß

        """
        self.response = self.client.post(
            reverse('register-user'),
            data=VALID_USER_DATA,
            format='json'
        )
        self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(self.response.data["username"], "anyatijude")
        self.assertEquals(self.response.data["email"], "anyatijude@glo.com")

    def test_empty_username(self):
        """
        test user registration without username

        """
        self.response = self.client.post(
            reverse('register-user'),
            data=EMPTY_USERNAME,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            self.response.data["errors"]["username"], "Username should not be left empty")

    def test_invalid_username(self):
        """
        test user registration with invalid username

        """
        self.response = self.client.post(
            reverse('register-user'),
            data=INVALID_USERNAME,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            self.response.data["errors"]["username"], "Username should not be less than 4 characters")

    def test_empty_email(self):
        """
        test user registration without email

        """
        self.response = self.client.post(
            reverse('register-user'),
            data=EMPTY_EMAIL,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            self.response.data["errors"]["email"], "Email should not be left empty")

    def test_empty_password(self):
        """
        test user registration without password

        """

        self.response = self.client.post(
            reverse('register-user'),
            data=EMPTY_PASSWORD,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            self.response.data["errors"]["password"], "Please provide the password")

    def test_empty_space_username(self):
        """
        test user registration with username with empty space

        """

        self.response = self.client.post(
            reverse('register-user'),
            data=EMPTY_SPACE_USERNAME,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            self.response.data["errors"]["username"], "Username should not contain any spaces")

    def test_empty_space_email(self):
        """
        test user registration with email with empty space

        """

        self.response = self.client.post(
            reverse('register-user'),
            data=EMPTY_SPACE_EMAIL,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            self.response.data["errors"]["email"], "Email should not contain any spaces")

    def test_password_with_empty_space(self):
        """
        test user registration using password with empty space

        """

        self.response = self.client.post(
            reverse('register-user'),
            data=PASSWORD_WITH_SPACE,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            self.response.data["errors"]["password"], "Password should not contain any spaces")

    def test_invalid_password(self):
        """
        test user registration with invalid password

        """

        self.response = self.client.post(
            reverse('register-user'),
            data=INVALID_PASSWORD,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(self.response.data["errors"]["password"],
                          "Password should have atleast one lowercase character,one Uppercase character, one Integer and one Special character")

    def test_short_password(self):
        """
        test user registration with short password

        """

        self.response = self.client.post(
            reverse('register-user'),
            data=SHORT_PASSWORD,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(self.response.data["errors"]["password"],
                          "Password length should not be less than 8 characters or greater than 20 characters")

    def test_empty_invalide_email(self):
        """
        test user registration with invalid email

        """
        self.response = self.client.post(
            reverse('register-user'),
            data=INVALID_EMAIL,
            format='json'
        )
        self.assertEquals(self.response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            self.response.data["errors"]["email"], "Invalid email address")