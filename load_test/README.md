### Running Load Tests Against your Endpoint

Using the python library [Locust](https://locust.io/), It is very convenient to simulate load traffic on your endpoint. 
It can be used to find an optimal setup of resources and to get a feeling for typical response times and delays. 

The python script `locustfile.py` implements the `ModelCaller` class. When executing locust, a UI will be available on your local machine. 
In the UI, the number of concurrent users can be adapted to simulate varying numbers of traffic, each being an ins

For most cases, the load that can be produced on a local macine will not be sufficient