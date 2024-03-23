from django.apps import AppConfig
from django.http import HttpResponse



class AuctionappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AuctionApp'
    
   
        
    def ready(self) -> None:
        from django_celery_beat .models import PeriodicTask, IntervalSchedule, SOLAR_SCHEDULES
        interval, _ = IntervalSchedule.objects.get_or_create(
            every=33,
            period = IntervalSchedule.SECONDS
    )
        PeriodicTask.objects.get_or_create(
        interval=interval,
        name = "my-schedule",
        task = "AuctionApp.tasks.my_task"
        )
        PeriodicTask.objects.get_or_create(
        interval=interval,
        name = "my-schedule1",
        task = "AuctionApp.tasks.my_task2"
        )
        return super().ready()

# observer = ephem.Observer()
        # observer.lat, observer.lon = 'your_latitude', 'your_longitude'  # Replace with your latitude and longitude
        # observer.date = ephem.Date(ephem.now())
        # solar_noon = observer.next_rising(ephem.Sun())
        #  from datetime import datetime, timezone
        # solar_noon_datetime = datetime.combine(solar_noon.date(), solar_noon.hour, solar_noon.minute, solar_noon.second, tzinfo=timezone.utc)

        # schedule, _ = CrontabSchedule.objects.get_or_create(
        #     hour=solar_noon_datetime.hour,
        #     minute=solar_noon_datetime.minute,
        #     second=solar_noon_datetime.second
        # )