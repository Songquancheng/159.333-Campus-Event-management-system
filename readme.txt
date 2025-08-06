First step :git clone https://github.com/Songquancheng/159.333-Campus-Event-management-system.git
Second step : cd 159.333-Campus-Event-management-system
3th : python -m venv .venv 创建虚拟环境
4th : .\.venv\Scripts\activate 激活
5th : pip install -r requirement 安装依赖
6th : python manage.py migrate 创建数据库结构
7th : python manage.py runserver 运行


如果不行，尝试一下管理员运行：Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process （临时管理员）
