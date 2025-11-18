import billboard
from datetime import datetime

def get_birthdate_number_one(birthdate_str: str):
try:
  birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
except ValueError:
  raise ValueError("Birthdate must be in YYYY-MM-DD format.")

chart_date_str = birthdate.strftime("%Y-%m-%d")
chart = billboard.ChartData('hot-100', date=chart_date_str)

if len(chart) == 0:
  raise RuntimeError("No chart data found for that date.")

top_song = chart[0]

return {
   "title" : top_song.title,
  "artist" : top_song.artist,
  "chart_date" : chart.date
}
def main ():
  print("Billboard Birthday SOng Finder")
  birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ").strip()

try: 
  result = get_birthdate_number_one(birthdate_str)
except Exception as e:
  print(f"Error: {e}")
  return

print()
print(f"OPN the billboard Hot 100 chart dasted {result['chart_date']}:")
print(f"The #1 song was \"{result['title']}\" by {result['artist']}.")

if __name__ == "__main__":
  main()
  
