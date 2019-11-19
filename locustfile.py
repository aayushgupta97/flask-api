from locust import Locust, TaskSet, task, HttpLocust


class MyTaskSet(TaskSet):
    @task
    def task1(self):
        self.client.get("/")

    @task
    def task2(self):
        self.client.get("/list_data")

    @task
    def task3(self):
        self.client.get("/fibonacci")
# @task(2)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
    stop_timeout = 600

# locust --host=http://localhost:8000
