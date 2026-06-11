from garmindb.garmindb import GarminDb, MonitoringDb, ActivitiesDb
from garmindb.summarydb import GarminSummaryDb, DailySummaryDb, WeeklySummaryDb
from garmindb.garmindb import MonitoringHeartRate, DailySummary, Sleep, Weight
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

# Point to your DB directory (default location)
db_params = garmindb.ConfigManager.get_db_params()

garmin_db = GarminDb(db_params)
monitoring_db = MonitoringDb(db_params)
summary_db = GarminSummaryDb(db_params)
activities_db = ActivitiesDb(db_params)