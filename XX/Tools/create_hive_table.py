import pymysql


def get_table_info(table, schema='', ispartition=True):
    cols = []
    create_head = """ create  external  table  if  not  exists  {0}.{1}(\n""".format(schema, table)
    if ispartition:
        create_tail = """\npartitioned  by(inc_day  string)\nrow  format  delimited  fields  terminated  by  '\\t' \n location  '/hivetable/{0}';""".format(table)
    else:
        create_tail = """\nrow  format  delimited  fields  terminated  by  '\\t' \nlocation  '/hivetable/{0}';""".format(table)
    connection = pymysql.connect(host='192.168.1.44',user='root',password='rebind1234',db='sqoop',port=3306,charset='utf8')
    try:
        # 获取一个游标
        with connection.cursor(cursor=pymysql.cursors.DictCursor)  as  cursor:
            sql = 'SHOW  FULL  FIELDS  FROM {0}'.format(table)
            cout = cursor.execute(sql)  # 返回记录条数
            try:
                for row in cursor:  # cursor.fetchall()
                    cols.append(row['Field'])
                    if 'bigint' in row['Type']:
                        row['Type'] = "bigint"
                    elif 'int' in row['Type'] or 'tinyint' in row['Type'] or 'smallint' in row['Type'] or 'mediumint' in row['Type'] or 'integer' in row['Type']:
                        row['Type'] = "int"
                    elif 'double' in row['Type'] or 'float' in row['Type'] or 'decimal' in row['Type']:
                        row['Type'] = "double"
                    else:
                        row['Type'] = "string"
                    create_head += row['Field'] + '  ' + row['Type'] + '  comment  \'' + row['Comment'] + '\' ,\n'
            except:
                import traceback
                traceback.print_exc()
                print('程序异常!')
    finally:
        connection.close()
    create_str = create_head[:-2] + '\n' + ')' + create_tail
    return cols, create_str  # 返回字段列表与你建表语句


cols, create_str = get_table_info("customer")
print(create_str)
