from django.core.management.base import BaseCommand
from movie_app.models import Movie
import csv
import os

class Command(BaseCommand):
    help = '从CSV文件导入数据'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help='CSV文件路径')

    def handle(self, *args, **options):
        path = options.get('path')
        if not path or not os.path.exists(path):
            self.stdout.write(self.style.ERROR('请提供有效的CSV文件路径'))
            return

        try:
            with open(path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                count = 0
                for row in reader:
                    # 确保CSV文件包含以下列：title, category, link, description, score
                    movie, created = Movie.objects.get_or_create(
                        title=row['title'],
                        defaults={
                            'category': row.get('category', '其他'),
                            'link': row.get('link', ''),
                            'description': row.get('description', ''),
                            'score': float(row.get('score', 0))
                        }
                    )
                    if created:
                        count += 1
                self.stdout.write(self.style.SUCCESS(f'成功导入 {count} 条网文数据'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'导入失败: {str(e)}'))    