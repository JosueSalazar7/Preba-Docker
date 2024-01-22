from locust import HttpUser, task, beween

class MyUser(HttpUser):
    wait_time= beween(1,2)

    @task
    def index(self):
        response = self.client.get("http://app:5000/")