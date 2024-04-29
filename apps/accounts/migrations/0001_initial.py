# Generated by Django 4.2.11 on 2024-04-27 19:57

import apps.accounts.utils
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Unique email address",
                        max_length=255,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        help_text="Unique username associated with the account",
                        max_length=16,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_username",
                                message='Username must be alphanumeric or contain any of the following: "_"',
                                regex="^[a-zA-Z0-9_]*$",
                            ),
                            django.core.validators.MinLengthValidator(
                                limit_value=4,
                                message="Username must be at least 4 characters long",
                            ),
                        ],
                        verbose_name="Username",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name of the user",
                        max_length=120,
                        verbose_name="Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="User bio or description",
                        max_length=300,
                        verbose_name="Description",
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        help_text="Profile image or avatar",
                        null=True,
                        upload_to=apps.accounts.utils.upload_to_profile_images,
                        verbose_name="Profile image",
                    ),
                ),
                (
                    "theme",
                    models.CharField(
                        choices=[
                            ("light", "Light"),
                            ("dark", "Dark"),
                            ("system", "System"),
                        ],
                        default="system",
                        help_text="User website theme",
                        max_length=55,
                        verbose_name="Theme",
                    ),
                ),
                (
                    "email_verified",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user has verified their email address",
                        verbose_name="Email verified",
                    ),
                ),
                (
                    "is_marked_for_deletion",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user has marked their account for                                                 deletion",
                        verbose_name="Is marked for deletion",
                    ),
                ),
                (
                    "date_marked_for_deletion",
                    models.DateTimeField(
                        blank=True,
                        help_text="Server date and time when the user deleted their                                                    account",
                        null=True,
                        verbose_name="Date marked for deletion",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier for the account",
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "short_uuid",
                    models.CharField(
                        editable=False,
                        help_text="Short unique identifier for the account",
                        max_length=8,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=8,
                                message="Short UUID must be exactly 8 characters long",
                            )
                        ],
                        verbose_name="Short UUID",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Server date and time the account was created",
                        verbose_name="Date joined",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Server date and time the account last logged in",
                        verbose_name="Last login",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Account",
                "verbose_name_plural": "Accounts",
            },
        ),
    ]
