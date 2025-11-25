import pandas as pd
from .models import KatahoWord

def import_kataho_excel(path):
    df = pd.read_excel(path)
    print("Rows in file:", len(df))

    imported = 0
    for _, row in df.iterrows():
        kataho = str(row.get("kataho_code"))
        roman = str(row.get("roman_code"))

        # update existing row or create new one
        obj, created = KatahoWord.objects.update_or_create(
            kataho_code=kataho,
            roman_code=roman,
            defaults={
                "type": row.get("type"),
                "plus_code": row.get("plus_code"),
                "hint": row.get("hint"),
                "kid": row.get("kid"),
                "hints": row.get("hints"),
                "meanings": row.get("meanings"),
                "created_at": row.get("created_at"),
                "updated_at": row.get("updated_at"),
            }
        )
        if created:
            imported += 1

    print("Imported or updated rows:", len(df))
    print("New rows added:", imported)
