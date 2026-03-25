from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# 数据库连接（后面你换成自己的 Render MySQL 信息）
def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='你的render数据库地址',
            database='你的库名',
            user='你的用户名',
            password='你的密码'
        )
        return connection
    except Error as e:
        print(e)
        return None

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 测试数据库是否连通
@app.route('/test-db')
def test_db():
    conn = create_db_connection()
    if conn:
        return "✅ 数据库连接成功！玉米基因系统正常运行。"
    else:
        return "❌ 数据库连接失败"

if __name__ == '__main__':
    app.run(debug=True)