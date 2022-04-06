JS_PATH=/home/website/mysite/algo_com_clock/static/js/
JS_PATH_DIST=${JS_PATH}dist/
JS_PATH_SRC=${JS_PATH}src/

# 在src目录下找到文件（-type f）且后缀名为.js 的文件，并且按字典序排序，且将所有文件的内容放到dist目录下的game.js中
find ${JS_PATH_SRC} -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}algoend.js

echo yes | python3 ../manage.py collectstatic # 打包所有app的static到项目根目录
