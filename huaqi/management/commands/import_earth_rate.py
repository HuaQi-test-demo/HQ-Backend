import os
from django.core.management.base import BaseCommand
from huaqi.models import earth_rate
import openpyxl

class Command(BaseCommand):
    help = 'Import data from XLSX files in a folder to the earth_rate model'

    def add_arguments(self, parser):
        parser.add_argument('folder_path', type=str, help='Path to the folder containing XLSX files')

    def handle(self, *args, **options):
        folder_path = options['folder_path']
        self.stdout.write(self.style.SUCCESS(f"Importing data from {folder_path}"))

        for file_name in os.listdir(folder_path):
            if file_name.endswith('.xlsx'):
                file_path = os.path.join(folder_path, file_name)
                self.stdout.write(self.style.SUCCESS(f"Processing file {file_name}"))

                # 加载 Excel 文件
                workbook = openpyxl.load_workbook(file_path)
                sheet = workbook.active

                # 假设第一行为标题行
                headers = [cell.value for cell in sheet[1]]

                # 从第二行开始读取数据
                for row in sheet.iter_rows(min_row=2, values_only=True):
                    try:
                        # 创建 earth_rate 对象
                        earth_rate_obj = earth_rate(
                            date_time=row[headers.index('Date')],
                            country=row[headers.index('country')],
                            currency=row[headers.index('source')],
                            currency_sign=row[headers.index('symbol')],
                            currency1_name=row[headers.index('currency_1_name')],
                            currency_rate1=row[headers.index('currency_1_rate')],
                            currency2_name=row[headers.index('currency_2_name')],
                            currency_rate2=row[headers.index('currency_2_rate')],
                            currency3_name=row[headers.index('currency_3_name')],
                            currency_rate3=row[headers.index('currency_3_rate')],
                            currency4_name=row[headers.index('currency_4_name')],
                            currency_rate4=row[headers.index('currency_4_rate')],
                            currency5_name=row[headers.index('currency_5_name')],
                            currency_rate5=row[headers.index('currency_5_rate')],
                            currency6_name=row[headers.index('currency_6_name')],
                            currency_rate6=row[headers.index('currency_6_rate')],
                            currency7_name=row[headers.index('currency_7_name')],
                            currency_rate7=row[headers.index('currency_7_rate')],
                            currency8_name=row[headers.index('currency_8_name')],
                            currency_rate8=row[headers.index('currency_8_rate')],
                            currency9_name=row[headers.index('currency_9_name')] if 'currency_9_name' in headers else None,
                            currency_rate9=row[headers.index('currency_9_rate')] if 'currency_9_rate' in headers else None
                        )
                        earth_rate_obj.save()
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error importing row {row}: {e}"))

        self.stdout.write(self.style.SUCCESS("Data import completed"))