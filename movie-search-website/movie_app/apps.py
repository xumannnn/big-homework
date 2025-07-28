from django.apps import AppConfig

class MovieAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie_app'  # 应用的实际名称，和目录名对应
    verbose_name = "网文管理"  # 这里设置在后台显示的应用名称

# 然后在 movie_app 目录下的 __init__.py 文件中添加一行
default_app_config = 'movie_app.MovieAppConfig'