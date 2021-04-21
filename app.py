from flask import Flask, render_template
from dbcm import UseDatabase
from json import load
from triangle import *
from draw import draw_graph

app = Flask(__name__, template_folder='templates')


def get_triangle(cursor):
    SQL_el = 'SELECT id, n1, n2, n3 FROM `femdb`.`elements`;'
    SQL_p = '''SELECT x, y FROM `femdb`.`nodes`;'''

    cursor.execute(SQL_el)
    result_el = cursor.fetchall()

    cursor.execute(SQL_p)
    result_p = cursor.fetchall()
    keys_p = ['x', 'y']
    result_p = [dict(zip(keys_p, value)) for value in result_p]

    for res in result_el:
        points = []
        for i in range(1, 4):
            points.append(Point(res[i], result_p[res[i] - 1]['x'], result_p[res[i] - 1]['y']))
        triangles.append(Triangle(res[0], points[0], points[1], points[2]))

    triangles[0].allow_colors = 0
    for trian in triangles:
        trian.coloring()
    draw_graph()


with open('data_files/config.json') as f:
    dbconfig = load(f)


with UseDatabase(dbconfig) as cursor:
    get_triangle(cursor)


@app.route('/')
def main():
    return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True)
