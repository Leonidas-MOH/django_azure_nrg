from .models import Task
from .models import TaskParam


def GetAzureFuncAddress(TaskId):
    tai = Task.objects.get(id=TaskId)
    try:
        pai = TaskParam.objects.get(task_id=TaskId)
        site = tai.url.strip()+'?code='+ tai.code.strip() + '&' + pai.param_name.strip() + '=' + pai.param_value.strip()        
    except:
        site = tai.url.strip()+'?code='+ tai.code.strip()
    return site
