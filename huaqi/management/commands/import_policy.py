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
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # 创建 news_2024 对象
                news_entry = policy_2024()

                # 逐个字段赋值

                news_entry.Date = row['Date'] if row['Date'] else None
                news_entry.affect_currency = row['affect_currency'] if row['affect_currency'] else None
                news_entry.affect_country = row['affect_country'] if row['affect_country'] else None
                news_entry.text_vectors = row['text_vectors'] if row['text_vectors'] else None
                # 保存到数据库
                news_entry.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV file'))