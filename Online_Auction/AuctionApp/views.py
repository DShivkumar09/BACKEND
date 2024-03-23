# from django.shortcuts import render
# from django.http import HttpResponse
# from .tasks import My_task
# from django_celery_beat .models import PeriodicTask, IntervalSchedule

# def index(request):
#     My_task.deley()
#     return HttpResponse("Task_Stareted!!")

# def schedule_task(request):
#     interval,_ = IntervalSchedule.objects.get_or_create(
#         every = 30,
#         period = IntervalSchedule.SECONDS,
#     )

#     PeriodicTask.objects.get_or_create(
#         interval=interval,
#         name = "my-schedule",
#         task = "AuctionApp.Tasks.My_task"
#     )

#     return HttpResponse("Task scheduled!!")

# # Create your views here.
