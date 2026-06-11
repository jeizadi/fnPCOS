from garmindb.garmindb import Sleep, Activities

sleep_records = Sleep.get_for_period(garmin_db, start, end)
sleep_df = pd.DataFrame([{
    'date': s.day,
    'total_sleep': s.total_sleep,
    'deep_sleep': s.deep_sleep,
    'light_sleep': s.light_sleep,
    'rem_sleep': s.rem_sleep
} for s in sleep_records])

sleep_df.set_index('date').plot(kind='bar', stacked=True, figsize=(14, 5),
                                title='Sleep Breakdown')
plt.ylabel('Minutes')
plt.show()

acts = Activities.get_for_period(activities_db, start, end)
acts_df = pd.DataFrame([{
    'date': a.start_time,
    'sport': a.sport,
    'distance_km': a.distance,
    'duration_min': a.elapsed_time / 60 if a.elapsed_time else None,
    'avg_hr': a.avg_hr
} for a in acts])

print(acts_df.groupby('sport')[['distance_km', 'duration_min']].sum())