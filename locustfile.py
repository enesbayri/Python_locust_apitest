from locust import HttpUser, task, between

class WebServiceUser(HttpUser):
    wait_time = between(1, 3)  # İstekler arasındaki bekleme süresi (1-3 saniye)

    @task
    def test_api(self):
        self.client.get("/")