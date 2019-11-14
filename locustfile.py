from locust import Locust, TaskSet, task, HttpLocust


class MyTaskSet(TaskSet):
    # @task
    # def my_task(self):
    #     print('executing task')

    @task(3)
    def task1(self):
        self.client.get("/")

    @task(6)
    def task2(self):
        self.client.get("/list_data")


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
