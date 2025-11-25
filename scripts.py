import os
import django
import pandas as pd

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SUggestion.settings")
django.setup()

from Suggestion_app.models import KatahoWord

# Read Excel
df = pd.read_excel('Katah0_codes_india.xlsx')
words = df['ColumnName']

# Insert into database
for w in words:
    KatahoWord.objects.create(text=w)

print(f"{KatahoWord.objects.count()} words loaded!")
