import csv
import os
from django.core.management.base import BaseCommand
from huaqi.models import policy_2024  # 替换为你的应用名称

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

class Command(BaseCommand):
    help = 'Import data from CSV file to policy_2024 table'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        with open(csv_file_path, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # 打印列名
            print("CSV file column names:", csv_reader.fieldnames)
            for row in csv_reader:
                news_entry = policy_2024()
                news_entry.Date = row.get('Date')  # 使用 get 方法避免 KeyError
                if not news_entry.Date:  # 如果 Date 列为空，跳过这一行
                    continue
                news_entry.affect_currency = row.get('affect_currency')
                news_entry.affect_country = row.get('affect_country')
                news_entry.text_vectors = row.get('text_vectors')
                news_entry.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV file'))