import postgresql
import queries


QUERIES_FOR_ANALYTICS = [
    queries.GET_ALL_DATA,
    queries.GET_GENDER_INFO,
    queries.GET_INCOME_CATEGORY_INFO
]


def main():
    db_manager = postgresql.PostgreSQLManager()
    db_manager.connect_to_db()
    for query in QUERIES_FOR_ANALYTICS:
        sql, filename = query.items()
        db_manager.execute_sql_to_xlsx(sql[1], filename[1])
    db_manager.close_connection()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
