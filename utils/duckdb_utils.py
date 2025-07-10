import duckdb
import pandas as pd

def load_data_into_duckdb(conn, df):
    conn.register('student_data', df)

def query_kpis(conn):
    result = conn.execute("""
        SELECT
            ROUND(AVG(CAST(Exam_Score AS DOUBLE)), 2) AS average_grade,
            ROUND(100.0 * SUM(CASE WHEN CAST(Exam_Score AS DOUBLE) >= 50 THEN 1 ELSE 0 END) / COUNT(*), 2) AS pass_rate,
            ROUND(100.0 * SUM(CASE WHEN CAST(Exam_Score AS DOUBLE) < 50 THEN 1 ELSE 0 END) / COUNT(*), 2) AS fail_rate,
            COUNT(*) AS total_students
        FROM student_data
    """).fetchdf()

    return result.iloc[0].to_dict()
