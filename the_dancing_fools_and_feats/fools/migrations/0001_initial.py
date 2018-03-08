# Generated by Django 2.0.3 on 2018-03-08 01:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DanceEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='User-facing name of the event', max_length=100)),
                ('occurrence', models.DateField(help_text='Example date of this event, used with frequency to anticipate when this event will occur in the future.')),
                ('website_url', models.URLField(help_text='Official website of this event', max_length=300)),
                ('location', models.CharField(help_text='Approximate location of this event, e.g. Newton, MA', max_length=60)),
                ('description', models.TextField(help_text='User-facing description of this event', max_length=300)),
                ('order', models.IntegerField(help_text='Visual order of the event compared to other events. Lower numbers will appear atop other events.')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyEvent',
            fields=[
                ('danceevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fools.DanceEvent')),
                ('frequency', models.DurationField(default=datetime.timedelta(30), editable=False)),
            ],
            bases=('fools.danceevent',),
        ),
        migrations.CreateModel(
            name='WeeklyEvent',
            fields=[
                ('danceevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fools.DanceEvent')),
                ('frequency', models.DurationField(default=datetime.timedelta(7), editable=False)),
            ],
            bases=('fools.danceevent',),
        ),
        migrations.CreateModel(
            name='YearlyEvent',
            fields=[
                ('danceevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fools.DanceEvent')),
                ('frequency', models.DurationField(default=datetime.timedelta(365), editable=False)),
            ],
            bases=('fools.danceevent',),
        ),
    ]
