import json

import util.config as utilConfig
import util.dbHelper as utilDb
import util.file as fileUtil


def update():
    sBuild = ""
    sql_list = []
    table_conf = utilConfig.dbconnect("rm-bp18c5414gvi6244h7o.mysql.rds.aliyuncs.com",
			    3306,
			    "pvs", 
			    "sd989sdfSQ($ee", 
			    "information_schema")
    table_db = utilDb.dbHelper(table_conf)
    pv_conf = utilConfig.dbconnect("rm-bp18c5414gvi6244h7o.mysql.rds.aliyuncs.com",
			    3306,
			    "pvs", 
			    "sd989sdfSQ($ee", 
			    "pv_db")
    pv_db = utilDb.dbHelper(pv_conf)
    page_list = pv_db.query("select tableName,uniqueCode from kc_pv_page where isdelete=0 order by sortindex;")
    for page in page_list:
        print(page)
        table_name = page[0]
        page_name = page[1]

        if table_name is None:
            continue
        
        column_list = table_db.query("select column_name, CHARACTER_MAXIMUM_LENGTH from columns where table_name='" + table_name + "' order by column_name;")
        report_setting_list = pv_db.query("select FieldsName, maxLen from kc_pv_reportsettings where isdelete=0 and pagename='" + page_name + "';")
        for col in column_list:
            l = [elem for elem in report_setting_list if str.lower(elem[0]) == str.lower(col[0])]
            for x in l:
                if col[1]:
                    s = "update kc_pv_reportsettings set FieldsName='%s',maxLen=%s where PageName='%s' and FieldsName='%s';\n" % (col[0], col[1], page_name, x[0])
                    if s not in sql_list:
                        sql_list.append(s)
                        fileUtil.write(s, "./kangce/sql/itemfields/" + table_name + ".sql")
                        sBuild = sBuild + str(s) + "</br>"
                else:
                    s = "update kc_pv_reportsettings set FieldsName='%s' where PageName='%s' and FieldsName='%s';\n" % (col[0], page_name, x[0])
                    if s not in sql_list:
                        sql_list.append(s)
                        fileUtil.write(s, "./kangce/sql/itemfields/" + table_name + ".sql")
                        sBuild = sBuild + str(s) + "</br>"
                # i = pv_db.exec(s)
    return sBuild

def update_item_field():
    sBuild = ""
    pv_conf = utilConfig.dbconnect("rm-bp18c5414gvi6244h7o.mysql.rds.aliyuncs.com",
			    3306,
			    "pvs", 
			    "sd989sdfSQ($ee", 
			    "pv_db")
    pv_db = utilDb.dbHelper(pv_conf)
    page_list = pv_db.query("select tableName,uniqueCode from kc_pv_page where isdelete=0 order by sortindex;")
    sql_list = []
    for page in page_list:
        table_name = page[0]
        page_name = page[1]

        if table_name is None:
            continue

        item_field_list = pv_db.query("select fieldsname, subfieldsname from kc_pv_itemfields where  isdelete=0 and pagename='"+page_name+"';")
        report_setting_list = pv_db.query("select FieldsName, maxLen from kc_pv_reportsettings where isdelete=0 and pagename='" + page_name + "';")

        for item_field in item_field_list:
            l = [elem[0] for elem in report_setting_list if str.lower(elem[0]) == str.lower(item_field[0])]
            if l:
                s = "update kc_pv_itemfields set FieldsName='%s' where PageName='%s' and FieldsName='%s';\n" % (l[0], page_name, item_field[0])
                if s not in sql_list:
                    sql_list.append(s)
                    fileUtil.write(s, "./kangce/sql/itemfields/" + table_name + ".sql")
                    sBuild = sBuild + str(s) + "</br>"

            l = [elem[0] for elem in report_setting_list if str.lower(elem[0]) == str.lower(item_field[1])]
            if l:
                s = "update kc_pv_itemfields set subfieldsname='%s' where PageName='%s' and subfieldsname='%s';\n" % (l[0], page_name, item_field[1])
                if s not in sql_list:
                    sql_list.append(s)
                    fileUtil.write(s, "./kangce/sql/itemfields/" + table_name + ".sql")
                    sBuild = sBuild + str(s) + "</br>"
    # pv_db.exec_sqls(sql_list)
    return sBuild
