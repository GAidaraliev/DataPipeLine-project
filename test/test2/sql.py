# import sqlfluff
#
# def upgrade() -> None:
#     op.execute("SET flatten_nested = 0;")
#     op.execute("""
#            CREATE TABLE IF NOT EXISTS events.credit_info_replica
#     ON CLUSTER default (
#         "event__id" String,
#         "event__time" DateTime(3),
#         "event_phone" String
#     )
#     ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}--{uuid}/events.credit_info_replica',
#     '{replica}'
#     )
#     ORDER BY (
#         "event__time",
#         "event__id"
#     )
#     PARTITION BY toYYYYMM(event__time)
#     """)
#
#     op.execute("""
#     CREATE TABLE IF NOT EXISTS events.credit_info
#     ON CLUSTER default
#     AS events.credit_info_replica
#     ENGINE = Distributed('default', 'events', credit_info_replica, rand());
#     """)
#
# def downgrade() -> None:
#     sql1 = """
#         DROP TABLE IF EXISTS events.credit_info ON CLUSTER default;
#     """
#     lint_sql = sqlfluff.lint(sql1, dialect='clickhouse')
#     print(lint_sql)
#     op.execute(sql1)
#     op.execute("DROP TABLE IF EXISTS events.credit_info_replica ON CLUSTER default;")
#
# sql1 = """DROP TABLE IF EXISTS events.credit_info ON CLUSTER default;
#     """
# lint_sql = sqlfluff.lint(sql1, dialect='clickhouse')
# print(lint_sql)


# from sqlfluff import lint
# import logging
# # Обычный однострочный или многострочный SQL
# sql = (
#     """
#     select  user_id,COUNT(*) as cnt
#     FROM analytics.events
#     WHERE dt >= '2025-01-01'
#     GROUP BY user_id
#     """
# )

# sql2 = """--sql
#     select user_id,COUNT(*) as cnt,
#     from analytics.events
#     WHEREd dt >= '2025-01-01'
#     GROUP BY user_id
#     """

# Линтинг
# violations = lint(sql, dialect="snowflake")   # или "bigquery", "postgres" и т.д.
# print(violations)


# def assert_sql_clean(sql: str, dialect: str = "bigquery"):
#     violations = lint(sql, dialect=dialect)
#     assert not violations, f"SQLFluff found issues:\n{violations}"
#
# assert_sql_clean(sql, dialect="snowflake")
def get_users() -> list[str]:
    bad_query = [
        """--sql 
        SELECT
            `name`,
            `count`
        WHERE age > 18
        ORDER BY `name`;
    """,
        """--sql 
    SELECT
        `name`,
        `count`,
        {country}
    WHERE age > 18
    ORDER BY `name`;
    """,
    ]
    return bad_query
