from flask import Flask

app = Flask(__name__)  # 初始化，创建Flask实例


# 注册路由， index()为视图函数，保存URL到python函数的映射关系
@app.route('/')
def index():
    """

    :return:
    """
    return "<h1>Hello World!</h1>"


if __name__ == '__main__':
    # 程序实例用run方法启动Flask集成的开发Web服务器
    app.run(debug=True)