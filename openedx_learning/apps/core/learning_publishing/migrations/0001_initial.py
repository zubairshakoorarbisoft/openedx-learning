# Generated by Django 3.2.10 on 2022-01-19 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LearningContext",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("identifier", models.CharField(max_length=255, unique=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="LearningContextType",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("identifier", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="LearningContextVersion",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(db_index=True, max_length=255)),
                (
                    "learning_context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learning_publishing.learningcontext",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="LearningContextBranch",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("branch_name", models.CharField(max_length=100)),
                (
                    "learning_context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learning_publishing.learningcontext",
                    ),
                ),
                (
                    "version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="learning_publishing.learningcontextversion",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="learningcontext",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                to="learning_publishing.learningcontexttype",
            ),
        ),
        migrations.CreateModel(
            name="LearningAppVersionReport",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app_name", models.CharField(max_length=100)),
                ("num_critical", models.PositiveIntegerField()),
                ("num_errors", models.PositiveIntegerField()),
                ("num_warnings", models.PositiveIntegerField()),
                (
                    "version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learning_publishing.learningcontextversion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LearningAppContentError",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("error_code", models.CharField(max_length=100)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("critical", "critical"),
                            ("error", "error"),
                            ("warning", "warning"),
                        ],
                        max_length=10,
                    ),
                ),
                ("usage_key", models.CharField(max_length=255, null=True)),
                ("data", models.JSONField()),
                (
                    "app_version_report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learning_publishing.learningappversionreport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalLearningContextBranch",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("branch_name", models.CharField(max_length=100)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "learning_context",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="learning_publishing.learningcontext",
                    ),
                ),
                (
                    "version",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="learning_publishing.learningcontextversion",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical learning context branch",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalLearningAppVersionReport",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("id", models.BigIntegerField(blank=True, db_index=True)),
                ("app_name", models.CharField(max_length=100)),
                ("num_critical", models.PositiveIntegerField()),
                ("num_errors", models.PositiveIntegerField()),
                ("num_warnings", models.PositiveIntegerField()),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "version",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="learning_publishing.learningcontextversion",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical learning app version report",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddConstraint(
            model_name="learningcontextbranch",
            constraint=models.UniqueConstraint(
                fields=("learning_context_id", "branch_name"),
                name="one_branch_per_learning_context",
            ),
        ),
        migrations.AddConstraint(
            model_name="learningappversionreport",
            constraint=models.UniqueConstraint(
                fields=("app_name", "version"), name="one_report_per_app_and_version"
            ),
        ),
    ]
