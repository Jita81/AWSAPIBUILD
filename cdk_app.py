#!/usr/bin/env python3

import os
from aws_cdk import core as cdk
from microservice_stack import MicroserviceStack

class CDKApp(cdk.App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Retrieve environment variables
        service_name = os.environ["SERVICE_NAME"]
        aws_region = os.environ["AWS_REGION"]

        # Create the microservice stack
        MicroserviceStack(
            self,
            f"{service_name}-stack",
            service_name=service_name,
            env=cdk.Environment(region=aws_region),
        )


def main():
    app = CDKApp()
    app.synth()


if __name__ == "__main__":
    main()
