import pandas as pd
import os


# -1-

def check_data(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.parquet'):
        df = pd.read_parquet(file_path)

    #טיפול בפורמט התאריך
    df['timestamp'] = pd.to_datetime(df['timestamp'], format="%d/%m/%Y %H:%M", errors='coerce')
    # המרת value למספר
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna(subset=['timestamp', 'value'])  # הסרת שורות עם ערך חסר
    df = df.drop_duplicates()
    return df

def calculate_hour_average(df):
    df['hour'] = df['timestamp'].dt.floor('h')  # עיגול ללמטה
    result = df.groupby('hour')['value'].mean().reset_index()
    result.columns = ['start_time', 'average']
    return result

# -2-

def split_by_day(df, output_folder='daily_files'):
    os.makedirs(output_folder, exist_ok=True)

    df['date'] = df['timestamp'].dt.date
    for date, group in df.groupby('date'):
        filename = f"{output_folder}/{date}.csv"
        group.drop(columns='date').to_csv(filename, index=False)

def calculate_hour_average_files(folder='daily_files'):
    all_results = []

    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df_day = pd.read_csv(os.path.join(folder, file))
            df_day['timestamp'] = pd.to_datetime(df_day['timestamp'], format="%Y-%m-%d %H:%M:%S")
            df_day['hour'] = df_day['timestamp'].dt.floor('h')
            hour_avg = df_day.groupby('hour')['value'].mean().reset_index()
            hour_avg.columns = ['start_time', 'average']
            all_results.append(hour_avg)

    final_df = pd.concat(all_results).sort_values(by='start_time').reset_index(drop=True)
    return final_df

# -3-

#אם הנתונים מגיעים בזרימה במקום מקובץ, אפשר לשמור לכל שעה את סכום הערכים וכמות הנתונים
#שהתקבלו עד כה. בכל פעם שמתקבל ערך חדש, נזהה לאיזו שעה הוא שייך, נוסיף אותו לסכום של אותה שעה
#ונעדכן את הכמות. כך נוכל לחשב את הממוצע של כל שעה בזמן אמת, בלי לעבור על כל הנתונים מחדש בכל פעם.
#

# -4-

#תומך בדחיסה חכמה שחוסכת מקום בדיסק ומשפרת ביצועים.
# מאפשר קריאה של עמודות ספציפיות בלבד, ולא את כל הקובץ, מה שחוסך בזיכרון ובזמן.
#מתאים לעבודה עם כמויות גדולות של מידע (Big Data) וביצועים טובים יותר מ־CSV.
#אחסון נתונים בפורמטים פתוחים ללא קשר למסד  נתונים ספציפי


if __name__ == "__main__":

    df_clean = check_data("time_series.csv")
    result = calculate_hour_average(df_clean)
    result.to_csv("hourly_averages.csv", index=False)

    split_by_day(df_clean)
    final_result = calculate_hour_average_files()
    final_result.to_csv("final_hour_averages_files.csv", index=False)
    print(final_result)


