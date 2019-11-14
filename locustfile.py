from locust import Locust, TaskSet, task, HttpLocust


class MyTaskSet(TaskSet):
    # @task
    # def my_task(self):
    #     print('executing task')

    @task(6)
    def task1(self):
        self.client.get("/")

    @task(9)
    def task2(self):
        self.client.get("/list_data")

    @task(3)
    def task3(self):
        self.client.get("/fibonacci")


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
    stop_timeout = 1200

# locust --host=http://localhost:8000
