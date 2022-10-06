"""This main module get it all together"""
import sql_work

if __name__ == '__main__':
    sql_work.creating_table()
    sql_work.show_all_data()
    sql_work.add_new_user("Garry", "1234")
