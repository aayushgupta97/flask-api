from locust import Locust, TaskSet, task, HttpLocust
import json


class MyTaskSet(TaskSet):
    @task
    def post(self):
        payload = {"name": "productsss",
                   "description": "this is another product",
                   "price": 50,
                   "qty": 2
                   }
        headers = {'content-type': 'application/json'}
        self.client.post("/product", json.dumps(payload), headers=headers)

    @task
    def get(self):
        self.client.get("/product")


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 25000
    stop_timeout = 600

# locust -f locustfile_2.py --host=http://localhost:8000
