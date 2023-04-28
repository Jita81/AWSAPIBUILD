document.getElementById("deploy-form").addEventListener("submit", deployMicroservice);
document.getElementById("test-form").addEventListener("submit", testMicroservice);

async function deployMicroservice(event) {
  event.preventDefault();

  const serviceName = document.getElementById("service-name").value;
  const awsRegion = document.getElementById("aws-region").value;
  const otherParams = document.getElementById("other-params").value;

  const deployEndpoint = "/deploy";
  const requestBody = {
    service_name: serviceName,
    aws_region: awsRegion,
    other_params: otherParams,
  };

  try {
    const response = await fetch(deployEndpoint, {
      method: "POST",
      body: JSON.stringify(requestBody),
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (response.ok) {
      const jsonResponse = await response.json();
      alert(`Microservice deployed successfully: ${jsonResponse.message}`);
    } else {
      throw new Error(`Deployment failed: ${response.statusText}`);
    }
  } catch (error) {
    alert(`Error: ${error.message}`);
  }
}

async function testMicroservice(event) {
  event.preventDefault();

  const apiKey = document.getElementById("api-key").value;
  const testInput = document.getElementById("test-input").value;
  const apiEndpoint = document.getElementById("api-endpoint").value;

  try {
    const response = await fetch(apiEndpoint, {
      method: "POST",
      body: JSON.stringify({ input
