# Generated by Django 3.2.19 on 2023-06-15 14:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import openedx_learning.lib.fields
import openedx_learning.lib.validators


def use_compressed_table_format(apps, schema_editor):
    """
    Use the COMPRESSED row format for TextContent if we're using MySQL.

    This table will hold a lot of OLX, which compresses very well using MySQL's
    built-in zlib compression. This is especially important because we're
    keeping so much version history.
    """
    if schema_editor.connection.vendor == 'mysql':
        table_name = apps.get_model("oel_contents", "TextContent")._meta.db_table
        sql = f"ALTER TABLE {table_name} ROW_FORMAT=COMPRESSED;"
        schema_editor.execute(sql)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oel_publishing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_digest', models.CharField(editable=False, max_length=40)),
                ('mime_type', openedx_learning.lib.fields.MultiCollationCharField(db_collations={'mysql': 'utf8mb4_unicode_ci', 'sqlite': 'NOCASE'}, max_length=255)),
                ('size', models.PositiveBigIntegerField(validators=[django.core.validators.MaxValueValidator(50000000)])),
                ('created', models.DateTimeField(validators=[openedx_learning.lib.validators.validate_utc_datetime])),
                ('file', models.FileField(null=True, upload_to='')),
                ('learning_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oel_publishing.learningpackage')),
            ],
            options={
                'verbose_name': 'Raw Content',
                'verbose_name_plural': 'Raw Contents',
            },
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('raw_content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='text_content', serialize=False, to='oel_contents.rawcontent')),
                ('text', openedx_learning.lib.fields.MultiCollationTextField(blank=True, db_collations={'mysql': 'utf8mb4_bin', 'sqlite': 'BINARY'}, max_length=100000)),
                ('length', models.PositiveIntegerField()),
            ],
        ),
        # Call out to custom code here to change row format for TextContent
        migrations.RunPython(use_compressed_table_format, reverse_code=migrations.RunPython.noop, atomic=False),
        migrations.AddIndex(
            model_name='rawcontent',
            index=models.Index(fields=['learning_package', 'mime_type'], name='oel_content_idx_lp_mime_type'),
        ),
        migrations.AddIndex(
            model_name='rawcontent',
            index=models.Index(fields=['learning_package', '-size'], name='oel_content_idx_lp_rsize'),
        ),
        migrations.AddIndex(
            model_name='rawcontent',
            index=models.Index(fields=['learning_package', '-created'], name='oel_content_idx_lp_rcreated'),
        ),
        migrations.AddConstraint(
            model_name='rawcontent',
            constraint=models.UniqueConstraint(fields=('learning_package', 'mime_type', 'hash_digest'), name='oel_content_uniq_lc_mime_type_hash_digest'),
        ),
    ]
