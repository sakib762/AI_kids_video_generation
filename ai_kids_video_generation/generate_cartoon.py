import replicate

# Set your Replicate API token
replicate.Client(api_token="YOUR_API_TOKEN")  # Replace with your token

# Choose the model
model = replicate.models.get("cjwbw/anime-art-diffusion")
version = model.versions.get("7e3e8b8de45c23b58e57f0a27a49be6a63b43c3f042fd9e6b6b9dd6fa1ba4e7e")

# Run inference
output = version.predict(prompt="A baby lion learning to roar under the moonlight")

# Print or use the output URL(s)
print("Generated Image URL:", output)
