from celery import shared_task

@shared_task(bind=True)
def fun(self):
    print("You are in Fun function")
    return "done" 