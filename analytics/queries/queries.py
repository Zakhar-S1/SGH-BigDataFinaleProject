GET_ALL_DATA = {
    'sql': '''select * from credit_card_customers''',
    'file_name_result': 'all_data'
}
GET_GENDER_INFO = {
    'sql': '''SELECT credit_card_customers."Gender", count(*) AS counter
                FROM credit_card_customers
                GROUP BY credit_card_customers."Gender"
                ORDER BY counter DESC''',
    'file_name_result': 'gender_info'
}
GET_INCOME_CATEGORY_INFO = {
    'sql': '''SELECT credit_card_customers."Income_Category", count(*) AS counter
                FROM credit_card_customers
                GROUP BY credit_card_customers."Income_Category"
                ORDER BY counter DESC''',
    'file_name_result': 'income_category_info'
}


