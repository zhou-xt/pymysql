import pymysql
# 连接数据库
conn = pymysql.connect(host='localhost', port=3306,user='root',password='root',database='sakila', charset='utf8')
# 获取游标
cursor = conn.cursor()

# 查询数据
# 执行ＳＱＬ语句 返回值就是ＳＱＬ语句在执行过程中影响的行数
sql = "select * from country;"
row_count = cursor.execute(sql)
print("ＳＱＬ语句执行影响的行数%d" % row_count)

# 取出结果集中的所有数据 返回一行数据
for line in cursor.fetchall():
    print(line)

# 关闭游标
cursor.close()
# 关闭连接
conn.close()