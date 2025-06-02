from metaflow import FlowSpec, step, kubernetes, environment

class HelloArgoFlow(FlowSpec):

    @step
    def start(self):
        print("Starting the Metaflow-Argo example.")
        self.next(self.process)

    @kubernetes(image="python:3.10")
    @step
    def process(self):
        import time
        time.sleep(5)
        print("Processing step inside Kubernetes pod.")
        self.next(self.end)

    @step
    def end(self):
        print("Flow completed using Argo Workflows.")

if __name__ == "__main__":
    HelloArgoFlow()

