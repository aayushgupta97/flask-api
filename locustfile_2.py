from locust import Locust, TaskSet, task, HttpLocust
# from werkzeug.wrappers import json
import json

class MyTaskSet(TaskSet):
    # @task
    # def my_task(self):
    #     print('executing task')

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

    #
    # @task
    # def task3(self):
    #     self.client.get("/fibonacci")


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
    stop_timeout = 100

# locust --host=http://localhost:8000
