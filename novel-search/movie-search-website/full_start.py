import os
import sys
import subprocess


def run_django_commands():
    try:
        # 执行 migrate 命令
        print("正在执行数据库迁移...")
        migrate_process = subprocess.run(
            [sys.executable, 'manage.py', 'migrate'],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(migrate_process.stdout)

        # 执行 runserver 命令
        print("\n正在启动 Django 开发服务器...")
        print("请访问 http://127.0.0.1:8000/ 查看网站")
        print("按 Ctrl+C 停止服务器")

        server_process = subprocess.run(
            [sys.executable, 'manage.py', 'runserver'],
            check=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"执行命令时出错: {e.stderr}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n服务器已停止")
        sys.exit(0)


if __name__ == "__main__":
    run_django_commands()