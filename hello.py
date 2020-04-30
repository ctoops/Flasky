from flask import Flask

app = Flask(__name__)  # 初始化，创建Flask实例


# 注册路由， index()为视图函数，保存URL到python函数的映射关系
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"


@app.route('/user/<name>')
def user(name):
    """动态路由，访问该地址时，则会根据名字显示对应欢迎信息
    装饰器中尖括号中的内容就是动态部分，任何能匹配静态部分的URL都会映射到该路由上
    调用视图函数时，Flask会将动态部分作为参数传入函数
    路由中的动态部分默认使用字符串，但可以使用类型定义
    e.g. /user/<int:id> 只会匹配动态批断id为整数的URL

    :param name:
    :return:
    """
    return '<h1>Hello, %s!</h1>' % name


@app.route('/account/<int:id>')
def account(id):
    return '<h1>Account is %s</h1>' % id


if __name__ == '__main__':
    # 程序实例用run方法启动Flask集成的开发Web服务器
    app.run(debug=True)
