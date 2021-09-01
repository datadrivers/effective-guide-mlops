import os

from locust import HttpUser, task
import json
import random
import pandas as pd
import logging
from typing import List
import dotenv

dotenv.load_dotenv()

log = logging.getLogger()

data_path: str = os.getenv("LOAD_TEST_DATA_PATH")
test_data: pd.DataFrame = pd.read_csv(data_path, header=None)


class ModelCaller(HttpUser):
    @task
    def get_prediction(self):
        """randomly selects 1-10 rows from test_data df and requests predictions from API."""

        # randomly selecting n cases
        no_cases: int = random.randint(1, 10)
        sample_data: List[List] = test_data.sample(no_cases).values.tolist()
        payload = json.dumps({"data": f"{sample_data}"})
        log.info(
            f"Calling API with {no_cases} cases and the following payload: {payload}"
        )
        response = self.client.post("/dev", data=payload)
        log.info(
            f"Return Message. Status code: {response.status_code}, Message: {response.text}"
        )
